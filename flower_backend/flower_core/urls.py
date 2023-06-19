from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    # Browsable urls that comes the DRF?
    path('api-auth/', include('rest_framework.urls')),

    # Admin site
    # path('admin/', admin.site.urls),

    # snippets test
    path('snippets/', include('snippets.urls')),

    # goal stuff
    path('api/', include('flower_web.urls'))
]
