"""CompareServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from Service import view
from Service import GoodList

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^getGoodsList/', GoodList.getGoodsList),
    url(r'^getGoodsListSize/', GoodList.getGoodsListSize),
    url(r'^getGoodInfo/', GoodList.getGoodInfo),
    url(r'^getOneComment/', GoodList.getOneComment),
    url(r'^getGoodsByShopName/', GoodList.getGoodsByShopName),
    url(r'^getCommentBycommodityId/', GoodList.getCommentBycommodity_id),
    url(r'^getGoodsCommentSize/', GoodList.getGoodsCommentSize),
    url(r'^getLikelyGoods/', GoodList.getLikelyGoods),
    url(r'^searchGoods/', GoodList.searchGoods),
    url(r'^getCommentGrade/', GoodList.getCommentGrade),
    url(r'^getWordCloudPic/', GoodList.getWordCloudPic),


]
