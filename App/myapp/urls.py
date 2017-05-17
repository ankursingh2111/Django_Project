from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.views.generic import ListView
from myapp.views import StaticView

from . import views
from . import models
urlpatterns =  [
    url(r'^hello/', views.hello, name = 'hello'),
    url(r'^hello1/', views.hello1, name = 'hello1'),
    url(r'^article/(\d+)/', views.Article, name = 'article'),
    url(r'^article1/(\d{2})/(\d{4})',views.Article1, name='article1'),
    url(r'^crudops',views.crudops, name='crudops'),
    url(r'^data',views.datamanipulation, name='data'),
    url(r'^static/',TemplateView.as_view(template_name = 'static.html')),
    url(r'^dreamreals/', ListView.as_view(model = models.Dreamreal, template_name = "dreamreal_list.html")),
    url(r'^connection/',TemplateView.as_view(template_name = 'login.html')),
    url(r'^login/', views.login, name = 'login'),
#    url(r'^profile/',TemplateView.as_view( template_name = 'profile.html')),
#    url(r'^saved/', 'SaveProfile', name = 'saved'),

]
