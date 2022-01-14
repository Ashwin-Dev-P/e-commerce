from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

		

urlpatterns = [
        path('',views.home,name='home'),
        path('index',views.home,name='home'),
        path('shop',views.shop,name='shop'),
        path('sign_up',views.sign_up,name='sign_up'),
        path('view/<int:id>',views.view,name='view'),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)