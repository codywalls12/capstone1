from django.urls import path
from . import views

app_name = "graph"

urlpatterns = [
    path("", views.index, name="index"),
    path("test", views.graph_creation, name="graph_creation"),
    path('about_us/', views.about_us, name='about_us'),

]