from django.shortcuts import render
from .models import Blog, Category, Tag, Comment
from user.models import Author
from utils.views import group_queryset

def index(request):
    header = Blog.objects.order_by('-id')[:5]
    resent_news = Category.custom.filter(name__in=['Politics','Technology'])
    blogs = Blog.objects.all()  
    business = Category.custom.get_category('Business')
    sport = Category.custom.get_category('Sport')
    gatgets = Category.custom.get_category('Gatgets')
    life_style = Category.custom.get_category('Life Style')
    travel = Category.custom.get_category('Travel')
    bus = Blog.objects.order_by('id')[:2]


    context = {
        'resent_news': resent_news,
        'header': header,
        'blogs': group_queryset(2,blogs),
        'business': business,
        'sport': sport,
        'gatgets': gatgets,
        'life_style': life_style,
        'travel': travel,
        'bus':bus
    }

    return render(request, 'index.html', context)



def page_404(request):
    return render(request, '404.html')


def authors(request):
    authors = Author.objects.all()
    contaxt = {
        'author': authors,
    }     
    return render(request, 'author.html',contaxt)


def blog_single(request):
    return render(request, 'blog_single.html')


def blog(request):

    blogs = Blog.objects.all()
    author = Author.objects.all()
    category = Category.custom.all()
    comments = Comment.objects.all()

    title = request.GET.get("title")

    if title:
        blogs = blogs.filter(title__icontains = title)

 
    contaxt = {
        'author':author,
        'blogs': blogs,
        'comments': comments,
        'category': category,
        'title':title
     
    }

    return render(request, 'blog.html',contaxt)

def contact(request):
    return render(request, 'contact.html')


def gallery_single(request):
    return render(request, 'gallery_single.html')


def gallery(request):
    return render(request, 'gallery.html')

def life_style(request):
    return render(request, 'life_style.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def sport(request):
    sport = Category.custom.get_category('Sport')

    context = {
        'sport':sport
    }

    return render(request, 'sport.html',context)


def technology(request):
    return render(request, 'technology.html')



