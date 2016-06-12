from django.conf.urls import url

from logistic import views

app_name = 'logistic'
urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^received/$', views.MessageView.as_view(message='Заявка успешно отправлена'), name='message'),
]
