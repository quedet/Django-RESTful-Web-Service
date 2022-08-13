from django.urls import path

from api.views import toys_detail, toys_list

app_name = 'api'

urlpatterns = [
    path('toys/', toys_list, name='toys_list'),
    path('toys/<int:pk>/', toys_detail, name='toys_detail')
]