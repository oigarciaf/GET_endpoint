from django.urls import path, url
from students import views

urlpatterns = [
    url(r'^students$',views.studentApi),
    url(r'^students/([0-9]+)$',views.studentApi)
]
