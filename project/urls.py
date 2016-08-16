from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings  
from django.conf.urls.static import static
from app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #categories list view
    url(r'^category_list/' , 'app.views.category_list'),
    #items list view
    url(r'^item_list/', 'app.views.item_list'),
    #items detail view
    url(r'^item_detail/(?P<pk>\d+)/', 'app.views.item_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
