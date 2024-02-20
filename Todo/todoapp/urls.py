from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
app_name = "todo"

urlpatterns = [
    path('add/',views.TodoAdd,name="todoadd"),
    path('delete/<int:id>/',views.TodoDelete,name="tododelete"),
    path('update/<int:id>/',views.TodoUpdate,name="todoupdate"),
    path('detail/<int:id>/',views.TodoDetail,name="tododetail"),
    path('completed/<int:id>/',views.TodoCompleted,name="todocompleted"),

]
