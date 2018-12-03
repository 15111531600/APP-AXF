from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^index/$',user_index,name='index'),
    url(r'^home/$',user_home,name='home'),
    url(r'^market/(\d+)/(\d+)/(\d+)/$',user_market,name='market'),
    url(r'^cart/$',user_cart,name='cart'),
    url(r'^mine/$',user_mine,name='mine'),
    url(r'^login/$',user_login,name='login'),
    url(r'^loginhandle/$',loginHandle,name='loginHandle'),
    url(r'^register/$',user_register,name='register'),
    url(r'^registerhandle/$',registerHandle,name='registerHandle'),
    url(r'^out/$',login_out,name='out'),
    url(r'^check/$',checkUserName,name='check'),
    url(r'^cartadd/$',cartadd,name='cartadd'),
    url(r'^cartdel/$',cartDel,name='cartDel'),
    url(r'^cartnumadd/$',cartNumAdd,name='cartNumAdd'),
    url(r'^cartnumreduce/$',cartNumReduce,name='cartNumReduce'),
    url(r'^cartselect/$',cartSelect,name='cartSelect'),
    url(r'^cartselectall/$',cartSelectAll,name='cartSelectAll'),
    url(r'^orderadd/$',orderAdd,name='orderAdd'),
    url(r'^changeorderstatus/$',changeOrderStatus,name='changeOrderStatus'),
    url(r'^orderunreceive/$',orderunreceive,name='orderunreceive'),
    url(r'^orderget/$',orderget,name='orderget'),
    url(r'^order/(\d+)/$',order,name='order'),
]