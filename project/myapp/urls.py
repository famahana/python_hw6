from django.urls import path
from . import views
urlpatterns = [ 
    path('',views.home),
    path('contacts',views.contacts),
    path('about',views.about),
    path('hw',views.hw),
    path('table',views.mult_table),
    path('programmer_day',views.programer_day)

    #path('about/<int:id>',views.about)
]
