from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from .form import ProductForm
# Create your views here.

def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context = {
		'form': form
	}
	return render(request, "products/product_create.html", context)


def homepage(request):
	print(request.user)
	#posts = Post.objects.all()
	#header = "This is My Blog"
	#print(posts)
	userInfo = request.user

	#The code below is to just print out something(h1 tag) on the page.
	#return HttpResponse("<h1>Hello World! My first Django Project")

	# We use render to view our full html page: rendering a template
	return render(request, 'index.html', {})


def about(request):
	return render(request, 'about.html', {})

def contact(request):
	return render(request, 'contact.html', {})

def foods(request):
	return render(request, 'foods.html', {})


