"""csquotes URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Allows users to go to any of the subpages directly from the route rather than having to preface it with /quotes/.
    # Note that "include" just roots a set of urls (those in genquotes.url) below those which are including them.
    url(r'^', include('genquotes.urls')),
    # Creates the path quotes/'subpage' from the root.
    url(r'^quotes/', include('genquotes.urls')),
    url(r'^admin/', admin.site.urls),


]
