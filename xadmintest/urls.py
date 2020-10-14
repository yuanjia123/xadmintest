
from django.contrib import admin
from django.urls import path,include
import xadmin

urlpatterns = [
    path('student/', include('student.urls')),
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
]
