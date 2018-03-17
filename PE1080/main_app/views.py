from django.shortcuts import render

# Create your views here.
def index(request):
	user_name = "Matt Cain"
	status = "Awesome"
	context = { 'username':user_name, 'status':status }
	return render(request, 'index.html', context)
