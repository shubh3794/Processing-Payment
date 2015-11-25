from django.shortcuts import render
from django.conf import settings
from .forms import contactForm
from django.core.mail import send_mail
# Create your views here.
def about(request):
	form = contactForm(request.POST or None)
	
	if form.is_valid():
		comment = form.cleaned_data['comment']
		name = form.cleaned_data['name']
		subject = 'message from mysite.com'
		body = '%s %s' %(comment,name)
		emailTo = [form.cleaned_data['email']]
		emailFrom = settings.EMAIL_HOST_USER
		send_mail(subject,body,emailFrom,emailTo, fail_silently = True)
		message = 'Thankyou, for the response'
		form = None
		context = {'form':form, 'Message':message}
	else:
		context = {'form':form, 'Message':None}
	template = 'contact.html'
	return render(request, template, context)