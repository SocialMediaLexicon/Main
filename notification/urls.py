from django.conf.urls import url
from notification.views import ShowNotifications

app_name="notification"
urlpatterns = [
    url('', ShowNotifications, name='show-notifications'),
]