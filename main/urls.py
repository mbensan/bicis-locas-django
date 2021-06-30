from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('ajax', views.index_ajax),
    path('new', views.save_biker),
    path('new-ajax', views.new_ajax),
    path('second/<name>', views.second)
]
