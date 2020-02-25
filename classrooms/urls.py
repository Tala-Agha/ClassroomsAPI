
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from classroom_api import views_api
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('login/', TokenObtainPairView.as_view(), name='api-login'),
    path('register/', views_api.RegisterView.as_view(), name="api-register"),
    path('classroom/list/api', views_api.ClassroomList.as_view(), name="api-classroom-list"),
    path('classroom/detail/api/<int:classroom_id>', views_api.ClassroomDetail.as_view(), name="api-classroom-detail"),
    path('classroom/create/api', views_api.ClassroomCreate.as_view(), name="api-classroom-create"),
    path('classroom/update/api/<int:classroom_id>', views_api.ClassroomUpdate.as_view(), name="api-classroom-update"),
    path('classroom/delete/api/<int:classroom_id>', views_api.ClassroomDelete.as_view(), name="api-classroom-delete"),


    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
