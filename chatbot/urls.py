from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name="home"),
    path("article/<int:article_id>",views.article),
    path("getResponse",views.getResponse,name="getResponse"),
    path("specialQuery",views.SpecialQuery,name="SpecialQuery")
]