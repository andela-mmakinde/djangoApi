from django.conf.urls import url

from app import views

urlpatterns = [
    url(
        r'^api/v1/puppies/(?P<pk>[0-9]+)$',
        views.get_delete_update_puppy,
        name='get_delete_update_puppy'
    ),
    url(
        r'^api/v1/puppies/$',
        views.get_post_puppies,
        name='get_post_puppies'
    ),
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.number_two, name='view_two'),
    url(r'^user/$', views.getUser, name='profile'),
]
