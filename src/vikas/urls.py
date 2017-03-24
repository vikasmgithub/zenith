from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
     url(r'^$', 'newsletter.views.home', name='home'),
     url(r'^carpenter/', 'newsletter.views.carpenter', name='carpenter'),
     url(r'^electrician/', 'newsletter.views.electrician', name='electrician'),
     url(r'^wallpaint/', 'newsletter.views.wallpaint', name='wallpaint'),
     url(r'^plumber/', 'newsletter.views.plumber', name='plumber'),
     url(r'^laundry/', 'newsletter.views.laundry', name='laundry'),
     url(r'^automobile/', 'newsletter.views.automobile', name='automobile'),
     url(r'^register/', 'newsletter.views.register', name='register'),
     # url(r'^contact-form/', 'newsletter.views.contactform', name='contact'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
] 

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)