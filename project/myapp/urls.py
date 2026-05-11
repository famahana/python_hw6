from django.urls import path
from . import views
urlpatterns = [ 
    path('',views.home),
    path('contacts',views.contacts),
    path('about',views.about),
    path('hw',views.hw),
    path('table',views.mult_table),
    path('programmer_day',views.programer_day),
    path('song_en',views.song_en),
    path('song_fr',views.song_fr),
    path('song_de',views.song_de),
    path('song_es',views.song_es),
    path('registration',views.registration_form)

    #path('about/<int:id>',views.about)
]
