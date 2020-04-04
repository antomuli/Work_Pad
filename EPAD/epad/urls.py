from django.conf.urls import url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import static
from django.conf.urls.static import static

urlpatterns=[
    url('dashboard/',views.dashboard,name='user-dashboard'),
    url('users/',views.registered_users,name='system_users'),
    url('user/activate/<int:id>',views.user_activate,name='activate_user'),
    url(r'user/deactivate/(\d+)',views.user_deactivate,name='deactivate_user'),
    url(r'^$',views.home,name='home'),
    url(r'user/assign_task/$',views.assign_task,name='assign_task'),
    url(r'rate/(\d+)',views.rate,name='rates'),
    url('profile/',views.profile,name = 'profile'),
    url(r'^logout/$',views.logout_request,name='logout'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)