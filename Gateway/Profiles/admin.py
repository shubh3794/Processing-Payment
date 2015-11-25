from django.contrib import admin
from Profiles.models import Profiles
from Profiles.models import userStripe

class AdmProfile(admin.ModelAdmin) :
	class Meta:
		model = Profiles

class AdmUserStripe(admin.ModelAdmin):
	class Meta:
		model = userStripe

admin.site.register(Profiles,AdmProfile) 
admin.site.register(userStripe,AdmUserStripe)
# Register your models here.
