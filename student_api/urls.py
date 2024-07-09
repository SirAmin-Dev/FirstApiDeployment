from django.urls import path
from .views import StudentListEndPoint


urlpatterns=[
    path('students', StudentListEndPoint.as_view(), name= "students")
]