from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name="home"),
    path("article/<int:article_id>",views.article),
    path("getResponse",views.getResponse,name="getResponse"),
    path("specialQuery",views.SpecialQuery,name="SpecialQuery"),
    path("dashbord",views.Dashbord,name="dashbord"),
    path("addevent",views.Addevent,name="Addevent"),
    path("collageinfo",views.Collage,name="collageinfo"),
    path("department",views.Department,name="department"),
    path("departmentinfo/",views.Department,name="departmentinfo"),
    path("admission",views.Addmission,name="admission"),
    path("admissioninfo/",views.Addmissioninfo,name="admissioninfo"),
    path("scholership",views.Scholership,name="scholership"),
    path("allevent",views.Allevent,name="allevent"),
    path("editevent/<x_id>",views.AlleventActionEdit,name="editevent"),
    path("deleteevent/<x_id>",views.AlleventActionDelete,name="deleteevent"),
    path("newEvent/",views.newEvent),
    path("setcollageinfo/",views.addCollageinfo)
]