from django.contrib import admin
from django.urls import path
from demos.views import calculator
urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculator/', calculator),
]
