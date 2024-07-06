from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index, name ='home'),
    path('recipe/<id>',views.delete_items),
    path('update_recipe/<id>',views.update_item),
    path('viewrecipe/<id>',views.viewRecipe),
    path('login/',views.user_login),
    path('signup/',views.signup),
    path('logout/',views.user_logout),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
