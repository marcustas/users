from django.shortcuts import render
from .models import CustomUser
from .forms import UserForm
from django.http import HttpResponseRedirect

# Create your views here.
def all_users(request):
	users = CustomUser.objects.all()
	return render(request, 'all_users.html', {'users': users})

def view(request, lid):
	user = CustomUser.objects.get(id=lid)
	return render(request, 'view.html', {'user': user})

def add(request):
	if request.method == 'GET':
		form = UserForm()
		return render(request, 'add.html', {'form': form})
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect('/')

def edit(request, lid):
	user = CustomUser.objects.get(id=lid)
	return render(request, 'add.html', {'user': user})

def delete(request, lid):
	user = CustomUser.objects.get(id=lid)
	if request.method == 'GET':
		return render(request, 'delete.html', {'user': user})
	if request.method == 'POST':
		user.delete()
		return HttpResponseRedirect('/')

