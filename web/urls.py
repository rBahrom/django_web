from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('guruh/', guruh, name='guruh'),
    path('kursatkich/', kursatkich, name='kursatkich'),
    path('reyting/', reyting, name='reyting'),
    path('sozlamalar/', sozlamalar, name='sozlamalar'),
    path('tulovlar/', tulovlar, name='tulovlar'),
]
