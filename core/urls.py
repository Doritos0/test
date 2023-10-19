from django.urls import path
from .views import login, login_editar
urlpatterns=[
    path('login/', login, name="login"),
    path('login_editar/<username>', login_editar, name="login_editar"),
]