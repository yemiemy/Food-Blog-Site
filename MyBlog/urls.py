"""MyBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from pages import views
from blog import views
from blog.views import  latest_blog, blog, single_page, lifestyle, create_post, homepage, search_view
from pages.views import about, contact, foods, product_create_view
from users.views import register, profile
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homepage, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('home/', homepage, name ='home'),
    path('about/', about, name='about'),
    path('blog/', latest_blog, name='blog'),
    path('contact/', contact, name='contact'),
    path('foods/', foods, name='foods'),
    path('lifestyle/', lifestyle, name='lifestyle'),
    path('blogger/', blog, name='blogger'),
    path('create/', product_create_view, name='create'),
    path('blog/<int:id>', single_page, name='single_page'),
    path('create_post/', create_post, name='create_post'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
    path('search/', search_view, name='search')
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "ForTheLoveOfFood Admin"
admin.site.site_title = "ForTheLoveOfFood Admin Portal"
admin.site.index_title = "Welcome to ForTheLoveOfFood Portal"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)