from django.shortcuts import render, get_object_or_404
from .forms import AdForm
from .models import Ad, Category


def index(request):
    ads = Ad.objects.all()
    context = {'title':'Главная страница, красивая', 'ads':ads}
    return render(request, 'main/index.html', context)

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            error = 'Ваше объявление размещено'
            form.save()
        else:
            error = 'Данные введены неправильно'
    form = AdForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def ad_list(request, category_slug = None):
    category = None
    categories = Category.objects.all()
    ads = Ad.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        ads = ads.filter(category=category)
    context = {'categories':categories, 'ads':ads}
    return render(request, 'main/list.html', context)

def ad_detail(request, id,slug):
    ad = get_object_or_404(Ad, id = id, slug = slug)
    context = {'ad':ad}
    return render(request, 'main/detail.html', context )

