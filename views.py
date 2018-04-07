from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from .models import Applicant, Documents, Application
from .forms import  ApplicationForm, RegisterApplicantForm, LoginApplicantForm, LoginAdmin
from django.contrib.auth.decorators import login_required
from .router import *
# Create your views here.






def register_applicant(request):
    if is_logged_in(request):
         request.session['message'] = 'you are registered already, logout to register with different user'
         return redirect('home_page')

    if request.method == "POST":
        form  = RegisterApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['message'] = 'Registration Successful, Now you can login'
            return redirect("home_page")
    else :
        form = RegisterApplicantForm()    
    return render(request, 'pmsApp/applicant/register.html', {'form':form})

def login_applicant(request):
    if is_logged_in(request):
       return handle_already_logged_in_error(request)
    error = None
    if request.method == "POST":   
        form = LoginApplicantForm(request.POST or None)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data["username"], password = form.cleaned_data['password'])
            if user is not None and user.profile.type == 'u':
                login(request, user)
            
                return redirect('dashboard', permanent = True)
            else:
                error = 'incorrect username and password'
        else:
                error = 'invalid data entered'
    else:
        form = LoginApplicantForm()
    return render(request, 'pmsApp/applicant/login.html', {'form': form, 'error': error, 'user': 'Applicant'})


@login_required(login_url='/login')
def dashboard(request) :
    if request.user.profile.type == 'u':
        error = None
        message = request.session['message']
        request.session['message'] = None
        applicant = Applicant.objects.get(MailId = request.user.username)
        has_applied =  applicant.application
        if has_applied:
            status = applicant.status.status
        return render(request, 'pmsApp/applicant/dashboard.html', {"user": applicant, "message": message, "has_applied": has_applied , "status": status, "error": error})
    return handle_lacks_privileges_error(request)



# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'pmsApp/post_edit.html', {'form': form})

@login_required(login_url='/login')
def submit_application(request): 
    if request.user.profile.type == 'u':
        applicant = Applicant.objects.get(MailId = request.user.username)
        if  Application.objects.filter(ApplicantId = applicant).exists():
            request.session['message'] = ALREADY_APPLIED_FOR_PASSPORT_MESSAGE
            return redirect('dashboard')
        if request.method == "POST":
            form = ApplicationForm(request.POST or None)
            if form.is_valid():
                application  = form.save(commit = False)
                application.ApplicantId = Applicant.objects.get(MailId = request.user.username)
                application.status = STATUS_1
                form.save()
                request.session['message'] = APPLICATION_SUBMITTED_SUCCESSFULLY_MESSAGE
                return redirect('dashboard')
        else:
            form = ApplicationForm()
        return render(request, 'pmsApp/applicant/application_form.html', {'form': form})
    return handle_lacks_privileges_error(request)

@login_required(login_url='home_page')
def logout_view(request):
    profile = request.user.profile.type
    logout(request=request)
    request.session['message'] = 'Successfully logged out'
    if profile == 'a':
        return redirect('login_admin')
    elif profile == 'u':
        return redirect('login_applicant')
    else:
        return redirect('login_police_officer')

def login_admin(request):
    if is_logged_in(request):
        return handle_already_logged_in_error(request)
    error = None
    if request.method == "POST":   
        form = LoginApplicantForm(request.POST or None)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data["username"], password = form.cleaned_data['password'])
            if user is not None and user.profile.type == 'a':
                login(request, user)
                request.session['message'] = 'you are logged in, but at homepage'
                return redirect('dashboard_a')
            else:
                error = 'incorrect username and password'
        else:
                error = 'invalid data entered'
    else:
        form = LoginApplicantForm()
    return render(request, 'pmsApp/admin/login.html', {'form': form, 'error': error, 'user': 'Admin'})


@login_required(login_url='/login_admin')
def dashboard_a(request) :
    if request.user.profile.type == 'a':
       return render(request, 'pmsApp/admin/dashboard.html', {})
    handle_lacks_privileges_error(request)



def  login_police_officer(request):
    if is_logged_in(request):
       return handle_already_logged_in_error(request)
    error = None
    if request.method == "POST":   
        form = LoginApplicantForm(request.POST or None)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data["username"], password = form.cleaned_data['password'])
            if user is not None and user.profile.type == 'p':
                login(request, user)
                request.session['message'] = 'you are logged in, but at homepage'
                return redirect('dashboard_p')
            else:
                error = 'incorrect username and password'
        else:
                error = 'invalid data entered'
    else:
        form = LoginApplicantForm()
    return render(request, 'pmsApp/police/login.html', {'form': form, 'error': error, 'user': 'Admin'})

def  register_police_officer(request):
    if is_logged_in(request):
       return handle_already_logged_in_error(request)
    return render(request, 'pmsApp/police/register.html', {})


@login_required(login_url='/login_p')
def dashboard_p(request):
    if request.user.profile.type == 'p':
        return render(request, 'pmsApp/police/dashboard.html', {})
    return handle_lacks_privileges_error(request)



# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'pmsApp/post_edit.html', {'form': form})



# def post_detail(req, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(req, 'pmsApp/post_detail.html', {'post': post})


    