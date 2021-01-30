from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from sharing import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('upload/', views.upload),
    path('<uuid:uid>/', views.download),
    path('', views.index),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
