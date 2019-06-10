from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Category
from .forms import commentForm, postForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.

def homepage(request):
	#print(request.user)
	post = Post.objects.all()
	feature = Post.objects.filter(featured = True)

	#userInfo = request.user
	#return HttpResponse("<h1>Hello World! My first Django Project")

	# We use render to view our full html page: rendering a template
	return render(request, 'index.html', {'post':post, 'feature':feature})


def lifestyle(request):
	post = Post.objects.order_by('-id')

	paginator = Paginator(post, 3)
	page = request.GET.get('page')
	post = paginator.get_page(page)

	return render(request, 'lifestyle.html', {'object':post}) 

def latest_blog(request):
	userInfo = request.user

	#post = Post.objects.all()
	post = Post.objects.order_by('-id')
	paginator = Paginator(post, 3)
	page = request.GET.get('page')
	post = paginator.get_page(page)
	form = commentForm()
	#comments = post.comments.all()
	#if form.is_valid():
			#comment = 
			#form.save()
			#form = commentForm()
			#comment.post = post
			#comment.author = request.user 
			#comment.save()
	return render(request, 'single.html', {'object':post, 'form':form})


def blog(request):

	posts = Post.objects.all()
	header = "This is My Blog"
	print(posts)


	return render(request, 'blog.html', {'titles':posts})


@login_required
def create_post(request):
	form = postForm(request.POST or None)
	if form.is_valid():
		post = form.save(commit=False)
		post.author = request.user
		post.save()
		#form = postForm()
		messages.success(request, 'Your Post has been created!')
		return redirect('blog')
	context = {
		'form': form
	}
	return render(request, "create_post.html", context)

def single_page(request, id):

	post = Post.objects.get(id=id)
	form = commentForm(request.POST or None)
	#header = "This is My Blog"
	comments = post.comments.all()
	active = post.comments.filter(active=True)
	if form.is_valid():
			
			comment = form.save(commit=False)
			form = commentForm()
			comment.post = post
			comment.author = request.user 
			comment.save()
	#if request.method == 'POST':
	#	form = commentForm(request.POST)
	#print(post)
	return render(request, 'single_page.html', {
		'post':post, 
		'comments': comments,
		'form':form,
		'active':active,})

def search_view(request):
	query = request.GET['query']
	posts = Post.objects.filter(title__icontains=query)|Post.objects.filter(body__icontains=query)
	feature = Post.objects.filter(featured = True)

	return render(request, 'search.html', {'post':posts, 'query':query, 'feature':feature})

