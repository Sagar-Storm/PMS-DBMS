from django.conf.urls import url
from .  import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.homePage, name = 'home_page'),
     url(r'^register$', views.register_applicant, name = 'register_applicant'),
     url(r'^login$', views.login_applicant, name  = 'login_applicant'),
     url(r'^application_form$', views.submit_application, name = 'application_form'),
    url(r'^myadmin/$', views.login_admin, name = 'login_admin'),
     url(r'^register_p$', views.register_police_officer, name  = 'register_police_officer'),
     url(r'^login_p$', views.login_police_officer, name  = 'login_police_officer'),
     url(r'^dashboard$', views.dashboard, name = 'dashboard'),
     url(r'^dashboard_a/$', views.dashboard_a, name = 'dashboard_a'),

     #id is document id
     url(r'^dashboard_a/docs/(?P<id>\d+)/$', views.view_docs, name = 'docs'),

     #id is application id
     url(r'^dashboard_a/verify/(?P<id>\d+)/$', views.accept_application, name = 'verify_application'),

     #see if you need this feature of selecting the police station
     #url(r'^dashboard_a/police_station/(?P<id>\d+)/$', views.select_police_station, name = 'select_police_station'),
     url(r'^dashboard_a/reject/(?P<id>\d+)/$', views.reject_application, name = 'reject_application'),

     #id is application id
     url(r'^dashboard_a/dispatch/(?P<id>\d+)/$', views.dispatch_passport, name = 'dispatch_passport'),
     url(r'^dashboard_p$', views.dashboard_p, name = 'dashboard_p'),

     #id is application id
     url(r'^dashboard_p/clear/(?P<id>\d+)/$', views.clear_application, name = 'clear_application'),

    url(r'^dashboard_p/reject/(?P<id>\d+)/$', views.reject_application_by_police, name = 'reject_application_by_police'),
     
     url(r'^logouts$', views.logout_view, name = 'logout')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



