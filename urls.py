from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name='home'),
    path('v1/', views.v1, name='view 1'),
]
