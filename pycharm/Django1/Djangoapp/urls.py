from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('nachal', views.nachal, name='nachal'),
    path('registr', views.registr, name='registr'),
    path('chats', views.chats, name='chats'),
    path('info', views.info, name='info'),
    path('news/<int:news_id>/', views.news, name='news')
]
