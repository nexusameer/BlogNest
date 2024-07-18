from typing import Any
from django.shortcuts import render
from app.models import *
from django.views.generic import TemplateView, DetailView
from django.core.mail import send_mail
from django.db.models import Q

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        posts = Post.objects.filter(status='published')
        posts_with_first_image = []
        for post in posts:
            first_image = post.images.first()
            posts_with_first_image.append({
                'post': post,
                'first_image': first_image
            })
        
        context['posts_with_first_image'] = posts_with_first_image
        return context
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'post-details.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_post = Post.objects.filter(author=self.object.author).exclude(pk=self.object.pk)
        context['author_posts'] = author_post
        return context
    
    
class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context
    
    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = 'ameerk10fw@gmail.com'

        form_data = {
            'name' : name,
            'email' : email,
            'subject' : subject,
            'message' : message
        }
        email_message = '''
        From: {}\n
        Subject : {}\n
        Message : \n\t\t{}\n

        '''.format(form_data['name'], form_data['subject'], form_data['message'])
        
        send_mail(form_data['subject'], email_message, '', [email])
        return super().get(request, *args, **kwargs)