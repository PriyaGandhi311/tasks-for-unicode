from django.conf.urls import url
from django.urls import path, include
from . import views

urlpatterns = [
    url(r'index/', views.index , name='index'),
    path('<int:n1>/<int:n2>/', views.adjs , name='adjs'),
    path('', views.add , name='add'),
    path('res',views.res, name='res')
]