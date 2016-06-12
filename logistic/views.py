from django.core import urlresolvers
from django.views import generic

from logistic import forms
from logistic import models


class Index(generic.CreateView):
    template_name = 'logistic/index.html'
    form_class = forms.SimpleRequestForm
    model = models.SimpleRequestModel

    def get_success_url(self):
        return urlresolvers.reverse('logistic:message')


class MessageView(generic.TemplateView):
    template_name = 'logistic/message.html'
    timeout = 0
    message = None

    def get_context_data(self, **kwargs):
        context = super(MessageView, self).get_context_data(**kwargs)
        context['timeout'] = self.timeout
        context['message'] = self.message
        return context
