from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('app1.urls', 'app1'), namespace='app1')),  # your app URLs
    path('accounts/', include('django.contrib.auth.urls')),      # add this line
]
