from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path(
        'san/<int:stadium_id>/',
        views.stadium_detail,
        name='stadium_detail'
    ),

    path(
        'lich/<int:field_id>/',
        views.field_schedule,
        name='field_schedule'
    ),
]