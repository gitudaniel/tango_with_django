from django.conf.urls import url
from resourcy import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^restricted/$', views.restricted, name='restricted'),
    url(r'^categories/$', views.categories, name='category_listing'),
    url(r'^find_category/$', views.find_categories, name='find_category'),

    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category,
        name='show_category'),

    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',
        views.add_page,
        name='add_page'),

]
