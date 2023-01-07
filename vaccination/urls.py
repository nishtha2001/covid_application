from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search, name='search'),
    path('apply/', views.apply, name='apply'),
    path('logout/', views.logout, name='logout'),
    path('add_center/', views.add_center, name='add_center'),
    path('dosage/', views.dosage, name='dosage'),
    path('remove_center/', views.remove_center, name='remove_center'),
]



