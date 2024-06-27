import django.shortcuts

def home(request):
    return django.shortcuts.render(request, 'home_page.html')

def guruh(request):
    return django.shortcuts.render(request, 'guruhlarim.html')

def kursatkich(request):
    return django.shortcuts.render(request, 'kursatkichlar.html')

def reyting(request):
    return django.shortcuts.render(request, 'reyting.html')

def sozlamalar(request):
    return django.shortcuts.render(request, 'sozlamalar.html')

def tulovlar(request):
    return django.shortcuts.render(request, 'tulovlar.html')
