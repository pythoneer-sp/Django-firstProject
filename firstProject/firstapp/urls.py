from django.urls import path
from . import views

app_name = 'firstapp'
urlpatterns = [
    path('',views.allapp, name='allapp'),
    path('<int:student_id>/', views.student_details, name='student_details'),
     path('store_forms/', views.store_view, name='store_forms'),
]