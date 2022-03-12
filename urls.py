from django.urls import path
from cadastros import views
from cadastros.views import ClientesCad , ClientesListagem, ClientesUpdate, ClientesDelete



urlpatterns = [
    path('', views.abertura_modelform , name = 'index'),
    path('cadastros/', ClientesCad.as_view(), name = 'cadastros'),
    path('listagem/', ClientesListagem.as_view(), name = 'listagem'),
    path('update/<int:pk>', ClientesUpdate.as_view(), name = 'update'),
    path('deletar/<int:pk>', ClientesDelete.as_view(), name = 'deletar'),
]
