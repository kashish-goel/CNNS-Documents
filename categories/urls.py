from django.urls import path,include
from . import views

urlpatterns=[

    path('articles',views.articles,name="articles"),
    path('dataUsersWorkshop',views.dataUsersWorkshop,name='dataUsersWorkshop'),
    path('factsheets',views.factsheets,name='factsheets'),
    path('',views.report,name='index'),
    path('keyFindings',views.keyFindings,name='keyFindings'),
    path('presentations',views.presentations,name='presentations'),
    path('report',views.report,name='report'),
    path('stateAndDistrict',views.stateAndDistrict,name='stateAndDistrict'),
    path('thematicReport',views.thematicReport,name='thematicReport'),
   
]
 
