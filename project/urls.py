from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings  
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^signup/$', 'app.views.signup'),
    url(r'^login_view/$', 'app.views.login_view'),
    url(r'^logout_view/$', 'app.views.logout_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
