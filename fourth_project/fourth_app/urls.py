from django.urls import path
from fourth_app import views

#tempate_tagging
app_name = 'fourth_app'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
