from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.index, name='index'),
    path('like/<int:quote_id>/', views.like, name='like'),
    path('dislike/<int:quote_id>/', views.dislike, name='dislike'),
    path('top/', views.top_quotes, name='top'),
]