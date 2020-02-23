"""BOD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from user.urls import urlpatterns as user_urls
from admins.urls import urlpatterns as ad_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url(r'',include(user_urls, namespace='users'),name='users'),
	url(r'', include(('user.urls', 'users'), namespace='users')),
	url(r'^admin/', include(('admins.urls', 'admins'), namespace='admins')),
   # url(r'^admin/', include(ad_views, namespace='admins'),name='admins'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
