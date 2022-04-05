from django.conf.urls import url
from Tissue.views import about,contact,rupesh11add,rupesh11list,rupesh11delete,rupesh11edit,banana,flower

urlpatterns= [
    url(r'^$',rupesh11list,name='rupesh11list'),
    url(r'^about/$',about,name='about'),
    url(r'^contact/$',contact,name='contact'),
    url(r'^add/$',rupesh11add,name='rupesh11add'),
    url(r'^edit/(?P<pk>\d+)$',rupesh11edit,name='rupesh11edit'),
    url(r'^delete/(?P<pk>\d+)$',rupesh11delete,name='rupesh11delete'),
    url(r'^banana/$',banana,name='banana'),
    url(r'^flower/$',flower,name='flower'),

    ]
