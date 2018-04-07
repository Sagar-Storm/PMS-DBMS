from django.contrib import admin

from .models import Applicant,  Application, Documents, Profile, Status

# Register your models here.
admin.site.register(Applicant)
admin.site.register(Application)
admin.site.register(Documents)
admin.site.register(Profile)
admin.site.register(Status)
