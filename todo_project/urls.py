"""todo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from todo_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.task_view,name='task_view'),
    path('delete/<int:taskid>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('index/',views.TaskListView.as_view(),name='index'),
    path('detail/<int:pk>', views.TaskDetailview.as_view(), name='detail'),
    path('update/<int:pk>', views.TaskUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.TaskDelete.as_view(), name='delete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
