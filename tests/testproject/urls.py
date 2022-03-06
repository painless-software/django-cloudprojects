from django.conf.urls import url
from django.contrib import admin

import cloudprojects

urlpatterns = [
    url('', cloudprojects.urls),
    url(r'^admin/', admin.site.urls),
]
