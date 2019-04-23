from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from movierater.api import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movierater.api.urls'))
]
