from django.conf.urls import url
from .  import views

urlpatterns = [

    url(r'^$', views.homePage, name = 'home_page'),
    url(r'^register$', views.register_applicant, name = 'register_applicant'),
    url(r'^login$', views.login_applicant, name  = 'login_applicant'),

    url(r'^application_form$', views.submit_application, name = 'application_form'),
   url(r'^madmin/$', views.login_admin, name = 'login_admin'),
    url(r'^register_p$', views.register_police_officer, name  = 'register_police_officer'),
    url(r'^login_p$', views.login_police_officer, name  = 'login_police_officer'),

    url(r'^dashboard$', views.dashboard, name = 'dashboard'),
    url(r'^dashboard_a$', views.dashboard_a, name = 'dashboard_a'),
    url(r'^dashboard_p$', views.dashboard_p, name = 'dashboard_p'),


    url(r'^logouts$', views.logout_view, name = 'logout'),

    

        
        
    # url(r'^post/new/$', views.post_new, name = 'post_new'),
    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]