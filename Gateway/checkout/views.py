from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
import stripe
# Create your views here.
stripe.api_key = settings.STRIPE_SECRET_KEY
@login_required
def checkout(request):
	publishkey = settings.STRIPE_PUBLISHABLE_KEY
	customer_id = request.user.userstripe.stripe_id

	if request.method == 'POST':
		token = request.POST['stripeToken']
		print token
		try:
			customer = stripe.Customer.retrieve(customer_id)
			customer.sources.create(source=token)
  			charge = stripe.Charge.create(
      			amount=1000, # amount in cents, again
      			currency="usd",
      			customer = customer,
      			description="Example charge"
  			)
		except stripe.error.CardError, e:
 		# The card has been declined
  			pass
	context = {'publishkey':publishkey}
	return render(request,'checkout.html', context)