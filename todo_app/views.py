from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Todo
from .forms import TodoForm

# Create your views here.


def home(request):

	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			todo_list = form.save(commit=False)
			todo_list.author = request.user
			todo_list.save()
			return redirect('todo-home')

	form = TodoForm()

	if request.user.is_authenticated:
		todo_list = Todo.objects.filter(author=request.user).order_by("-date")
	
		data = {
				"forms": form,
				"list": todo_list,
		}
		
		return render(request, "todo_app/todo_home.html", data)

	else:
		data = {
				"forms": form,
		}
		
		return render(request, "todo_app/todo_home.html", data)


@login_required(login_url='login/')
def delete(request, item_id):
	item = Todo.objects.get(id=item_id)
	item.delete()

	return redirect('todo-home')


@login_required(login_url='accounts/login/')
def update(request, item_id):
	item = Todo.objects.get(id = item_id)
	form =TodoForm(request.POST or None, instance=item)

	if form.is_valid():
		form.save()
		return redirect("todo-home")

	context={
			'forms': form
	}

	return render(request, "todo_app/todo_update.html", context)