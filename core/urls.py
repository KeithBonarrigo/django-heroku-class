from django.urls import path
from .views import list_clients, new_client, client_update, client_delete

urlpatterns = [
    path('', list_clients, name="client_list"),
    path('new/', new_client, name="client_create"),
    path('update/<int:id>/', client_update, name="client_update"),
    path('delete/<int:id>/', client_delete, name="client_delete"),

]