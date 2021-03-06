from django.conf import settings
from django.db import models
from allauth.account.signals import user_logged_in, user_signed_up
import stripe
# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your models here.
class Profiles(models.Model):
	name = models.CharField(max_length = 1200)
	description = models.TextField(null=True, blank = True)
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null = True, blank = True)
	def __unicode__(self):
		return self.name

class userStripe(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	stripe_id = models.CharField(max_length = 200, null=True, blank=True)
	def __unicode__(self):
		if self.stripe_id:
			return str(self.stripe_id)
		else:
			return self.user.username

def clbk(sender,request,user,**kwargs):
	stripe_ac,created = userStripe.objects.get_or_create(user=user)
	if created:
		print "created for %s"%(user.username)

	if stripe_ac.stripe_id == None or stripe_ac.stripe_id == "":
		new_stripe_id = stripe.Customer.create(email = user.email)
		stripe_ac.stripe_id = new_stripe_id['id']
		stripe_ac.save()
	prof,cr = Profiles.objects.get_or_create(user=user)
	if cr:
		prof.name = user.username
		prof.save()

user_logged_in.connect(clbk)
user_signed_up.connect(clbk)	