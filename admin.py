from django.contrib import admin

from .models import Applicant,  Application, Documents, Profile, Status, Admin, PoliceDepartment

class ApplicantAdmin(admin.ModelAdmin):
  #list_display =  ('Name', 'Venue', 'Date', 'Time')

# Register your models here.
admin.site.register(Applicant)
admin.site.register(Application)
admin.site.register(Documents)
admin.site.register(Profile)
admin.site.register(Status)
admin.site.register(Admin)
admin.site.register(PoliceDepartment)

#header for the site
admin.site.site_header = "Passport Management System"
admin.site.site_url  = None



