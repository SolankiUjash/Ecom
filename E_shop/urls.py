
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import store_app
from . import views
urlpatterns = [
    # path("",include("store_app.urls")),
    path("base/",views.BASE,name="base"),
    path('admin/', admin.site.urls),
    path('',views.HOME,name="home"),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
