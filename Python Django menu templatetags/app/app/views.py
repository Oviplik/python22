from django.shortcuts import render
from .models import Menu, Post
from django.views.generic.detail import DetailView

def index(request):
    context = {
        'posts': Post.objects.all(),
        'menus': Menu.objects.all(),
        'title': 'Main'
    }
    return render(request, 'app/index.html', context=context)


def draw_menu(request, path):
    splitted_path = path.split('/')
    assert len(splitted_path) > 0, ('= Draw_menu function failed =')
    return render(request, 'app/index.html', {'menu_title': splitted_path[0], 'menu_item': splitted_path[-1]})

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'


