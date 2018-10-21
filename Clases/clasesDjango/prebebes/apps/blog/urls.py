from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('verPosts/',views.listadoPosts,name='listado'),
    path('post/<pk>',views.detalles,name='detalles'),
    path('post/nuevo/',views.nuevoPost,name = 'nuevo'),
    path('post/<pk>/modificar/', views.modificar, name='modificar'),
]
