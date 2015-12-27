from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'page1.main.index', name='root'),
    url(r'^index$', 'page1.main.index', name='index'),
    url(r'^index.html$', 'page1.main.index', name='index'),
    url(r'^login$', 'page1.main.login', name='login'),
    url(r'^logout$', 'page1.main.logout', name='logout'),
    url(r'^loggedin$', 'page1.main.loggedin', name='loggedin'),
    # url(r'^$', 'page.views.home', name='home'),
    # url(r'^page/', include('page.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
