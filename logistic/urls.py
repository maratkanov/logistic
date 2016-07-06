from django.conf.urls import url
from django.views.generic import TemplateView

from logistic import views

app_name = 'logistic'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^received/$', views.MessageView.as_view(message='Заявка успешно отправлена'), name='message'),
    url(r'^glogistics\.ru\.html/$', TemplateView.as_view(template_name='logistic/wo_sign.html'), name='wo_sign'),
]
