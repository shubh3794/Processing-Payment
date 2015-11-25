from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe
# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY
@login_required
def checkout(request):
	publishkey = settings.STRIPE_PUBLISHABLE_KEY

	if request.method == 'POST':
		token = request.POST['stripeToken']
		print token
		try:
  			charge = stripe.Charge.create(
      			amount=1000, # amount in cents, again
      			currency="usd",
      			source=token,
      			description="Example charge"
  			)
		except stripe.error.CardError, e:
 		# The card has been declined
  			pass
	context = {'publishkey':publishkey}
	return render(request,'checkout.html', context)