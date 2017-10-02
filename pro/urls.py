from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = [
    # Examples:
    # url(r'^$', 'pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('glavnaya.urls')),
    url(r'^price/', include('price.urls')),
    url(r'^master/', include('master.urls')),
    url(r'^works/', include('works.urls')),
    url(r'^kontacts/', include('kontacts.urls')),
]

