from .models import *

class CommonContextMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['post'] = Post.objects.filter(status='published')
        context['image'] = BlogImages.objects.all()
        return context