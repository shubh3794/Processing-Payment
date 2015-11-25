from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
def Home(request):
	context = locals()
	return render(request, 'home.html', context)

def about(request):
	context = locals()
	return render(request, 'about.html', context)

@login_required
def profile(request):
	user = request.user
	context = {'user':user}
	return render(request,'profile.html', context)