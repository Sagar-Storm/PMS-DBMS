from django.shortcuts import render, get_object_or_404, redirect

ANONYMOUS_USER = 'AnonymousUser'
LOGGED_IN_ALREADY_MESSAGE = 'You are already logged in, please logout before you login '
NOT_PRIVILEGED_MESSAGE = 'You are not privileged to access this page' 
APPLICATION_SUBMITTED_SUCCESSFULLY_MESSAGE = 'Successfully submitted the application. Application status will be provided timely as it gets processed'
ALREADY_APPLIED_FOR_PASSPORT_MESSAGE = 'You have already applied for the passport. Please wait as we update the status about your application. bitch'


#status related constants

STATUS_1 = 'Your application is yet to be reviewed'
STATUS_2 = 'Your application has been reviewed and sent to the police department for further verification.'
STATUS_3 = 'Your application has been successfully verified by the police deparment. Shipping work is in progress'
STATUS_4 = 'Dispatched, your passport will arrive shortly!'
STATUS_5 = 'Application has been rejected by the administrator'
STATUS_6 = 'Application has been rejected by the police department'




def is_logged_in(request):
    if str(request.user) == ANONYMOUS_USER:
        return None
    return True

def set_message(request, message):
    request.session['message'] = message

def clear_message(request):
    request.session['message'] = None

def handle_redirection(request):
    if request.user.profile.type == 'u':
        return redirect('dashboard')
    elif request.user.profile.type == 'a':
        return redirect('dashboard_a')
    else :
        return redirect('dashboard_p')

def handle_already_logged_in_error(request):
    request.session['message'] = LOGGED_IN_ALREADY_MESSAGE
    return handle_redirection(request)

def handle_lacks_privileges_error(request):
    request.session['message'] = NOT_PRIVILEGED_MESSAGE
    return handle_redirection(request)


