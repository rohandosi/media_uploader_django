from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from myproject.myapp.views import list
from django.contrib import admin
from django.contrib.auth import views
from myproject.myapp.forms import LoginForm



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('myproject.myapp.urls')),
    url(r'^listnew/$', RedirectView.as_view(url='/myapp/list/')),
    url(r'^login/', views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/', views.logout, {'next_page': '/login'}),
    url(r'^list/$', list, name='list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





