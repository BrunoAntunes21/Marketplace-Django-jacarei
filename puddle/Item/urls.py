from django.urls import path
from Item import views
app_name='item'
urlpatterns=[

    path('<int:pk>/',views.details,name='details'),
]