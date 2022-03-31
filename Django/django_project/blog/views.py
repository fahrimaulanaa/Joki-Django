from django.shortcuts import render
from matplotlib.style import context

# Create your views here.

posts = [
    {
        'author': 'Ardesty Sugiarto',
        'title': '  Cuci sepatu murah',
        'content': 'Cuci sepatu gosok',
        'date_posted': '31 March 2022',
    },
    {
        'author': 'Ardesty Sugiarto',
        'title': 'Cuci sepatu bersih',
        'content': 'Ini agak mahal tapi bersih kok',
        'date_posted': '01 April 2022',
    }
]

def home(request):
    context = {'posts' : posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})