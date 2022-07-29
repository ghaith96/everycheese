from django.urls import path

from .views import CheeseDetails, CheeseListView, CheeseCreateView

app_name="cheeses"
urlpatterns=[
    path(
        route='',
        view=CheeseListView.as_view(),
        name='list',
    ),
    path(
        route='add/',
        view=CheeseCreateView.as_view(),
        name='add',
    ),
    path(
        route='<slug:slug>/',
        view=CheeseDetails.as_view(),
        name='detail',
    ),
]
