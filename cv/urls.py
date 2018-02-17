from django.conf.urls import url
from django.views.generic import TemplateView

# Create your urls here

urlpatterns = [ 
    url('^$', TemplateView.as_view(template_name='index.html')),
]
