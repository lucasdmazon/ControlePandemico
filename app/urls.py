from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:dado_id>', views.ver_aluno, name='ver_aluno'),
]