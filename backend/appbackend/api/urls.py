from django.urls import path
from . import views

urlpatterns = [
    path('add-form/',views.AddFormData.as_view(),name='add-form'),
    path('get-form/',views.GetFormData.as_view(),name='get-form'),
    path('del-form/',views.DeleteData.as_view(),name='del-form'),
]