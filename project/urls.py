from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings  
from django.conf.urls.static import static
from app import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #cart url

    url(r'^cart/(?P<pk>\d+)/', 'app.views.get_cart'),
    # url(r'^add_to_cart/(?P<pk>\d+)/', 'app.views.add_to_cart'),

    url(r'^admin/', include(admin.site.urls)),
    #categories list view
    url(r'^category_list/' , 'app.views.category_list'),
    #items list view
    url(r'^item_list/(?P<pk>\d+)', 'app.views.item_list'),
    #items detail view
    url(r'^item_detail/(?P<pk>\d+)/', 'app.views.item_detail'),
    url(r'^signup/$', 'app.views.signup'),
    url(r'^login_view/$', 'app.views.login_view'),
    url(r'^logout_view/$', 'app.views.logout_view'),
    url(r'^about_view/$', 'app.views.about_view'),
    url(r'^how_view/$', 'app.views.how_view'),
    url(r'^contact/$', 'app.views.contact'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
