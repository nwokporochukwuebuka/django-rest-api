"""django_api_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
#from test_app.views import Simple, SimpleGenericUpdate, SimpleGenerics
#from test_app.views import SimpleViewset
#from rest_framework.routers import DefaultRouter
from django.conf import settings
#from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


# Setting router
'''router = DefaultRouter()'''
#router.register("simple-viewset", SimpleViewset)





urlpatterns = [
    path('admin/', admin.site.urls),
    path('gateway/', include('gateway.urls')),
    path("user-main/", include("user.urls")),
    #path("simple/", include(router.urls))
    path("event-main/", include('event_controller.urls')),
    path('schema', get_schema_view(title="Event API", description="API for an event", version="1.0.0"), name="openapi-schema"),
    path('docs/', include_docs_urls(title="Event API"))
]


# Setting up the debug toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ]+ urlpatterns
'''path('simple/', Simple.as_view()),
    path('simple/<int:id>', Simple.as_view()),
    path('simple-generics', SimpleGenerics.as_view()),
    path('simple-generics/<int:id>', SimpleGenericUpdate.as_view()),'''
