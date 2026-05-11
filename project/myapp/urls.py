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
    path('registration',views.registration_form),
    path('restraunts',views.restraunt_),
    path('restraunts/delete/<int:id>', views.delete_restraunt),
    path('restraunts/update/<int:id>', views.update_restraunt),
    path('restraunts/search/', views.search_restraunt),
    #path('about/<int:id>',views.about)
]
