from django.urls import path


from web import views


urlpatterns = [
    path('', views.index),
    path('contacts', views.contacts),
    path('status', views.status),
    path('post', views.post),
    path('post_2', views.post_2),
    path('gallery', views.gallery),
    path('gallery/<int:pub_id>', views.publication),
    path('heroes', views.heroes),
    path('heroes/<int:pub_id>', views.hero),
    path('art', views.art),
    path('aboutwar', views.aboutwar),
    path('films', views.films),
    path('excursions', views.excursions),
    path('songs', views.songs),
]
