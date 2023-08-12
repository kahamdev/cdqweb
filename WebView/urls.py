from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('events/',views.events,name='events'),
    path('brokers/',views.brokers,name='brokers'),
    path('non_real_estate/',views.non_real_estate,name='non_real_estate'),
    path('real_estate/',views.real_estate,name='real_estate'),
    path('real_tabs_1/',views.real_tabs_1,name='real_tabs_1'),
    path('real_tabs_2/',views.real_tabs_2,name='real_tabs_2'),
    path('real_tabs_3/',views.real_tabs_3,name='real_tabs_3'),
    path('real_tabs_4/',views.real_tabs_4,name='real_tabs_4'),
    path('non_real_tabs_1/',views.non_real_tabs_1,name='non_real_tabs_1'),
    path('non_real_tabs_2/',views.non_real_tabs_2,name='non_real_tabs_2'),
    path('non_real_tabs_3/',views.non_real_tabs_3,name='non_real_tabs_3'),
    path('non_real_tabs_4/',views.non_real_tabs_4,name='non_real_tabs_4'),
    path('broker_post/',views.broker_post,name='broker_post'),
    path('suscribe/',views.suscribe,name="suscribe"),
]
