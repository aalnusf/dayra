from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static 
from django.conf import settings 
from app import views 


urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^category_list/' , 'app.views.category_list'),
    url(r'^item_list/', 'app.views.item_list'),
    url(r'^item_detail/(?P<pk>\d+)/', 'app.views.item_detail'),
    url(r'^signup/$', 'app.views.sign_up'),
    url(r'^login_view/$', 'app.views.login_view'),
    url(r'^logout_view/$', 'app.views.logout_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



