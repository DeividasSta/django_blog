from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:a_id>', views.details, name='details')
]
