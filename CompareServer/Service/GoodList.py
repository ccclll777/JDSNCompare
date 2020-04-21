from django.http import HttpResponse
from django.utils.decorators import method_decorator
from commentAnalysis import nlp_process
from commentAnalysis import generate_wordcloud
from  dbModel import get
import json
from django.views.decorators.csrf import ensure_csrf_cookie
'''
返回商品列表 
根据商品类型和不同的品牌 不同的平台
分页查询 每次返回一页
'''
def getGoodsList(request):
    commodity_brand = request.GET.get('commodity_brand')
    print(commodity_brand)
    commodity_type = request.GET.get('commodity_type')
    limit = int(request.GET.get('limit'))
    offset = int(request.GET.get('offset'))
    tag = request.GET.get('tag')
    print(commodity_brand,commodity_type,limit,tag)
    res_list = get.dbGet().getGoodsList(commodity_brand,commodity_type,limit,offset,tag)
    res = json.dumps(res_list,ensure_ascii=False)
    return HttpResponse(res,content_type="application/json,charset=utf-8")
'''
返回商品列表的总大小
根据商品类型和不同的品牌 不同的平台
为分页查询 提供准备
'''
def getGoodsListSize(request):
    commodity_brand = request.GET.get('commodity_brand')
    commodity_type = request.GET.get('commodity_type')
    tag = request.GET.get('tag')
    res_list = get.dbGet().getGoodsListSize(commodity_brand, commodity_type, tag)
    res = json.dumps(res_list, ensure_ascii=False)
    return HttpResponse(res, content_type="application/json,charset=utf-8")
'''
根据商品id获取商品的详细信息
'''
def getGoodInfo(request):
    commodity_id = request.GET.get('commodity_id')
    print(commodity_id)
    tag = request.GET.get('tag')
    print(tag)
    res_list = get.dbGet().getGoodInfo(commodity_id)
    res = json.dumps(res_list, ensure_ascii=False)
    return HttpResponse(res, content_type="application/json,charset=utf-8")
'''
随机获取某条评论
'''
def getOneComment(request):
    commodity_id = request.GET.get('commodity_id')
    tag = request.GET.get('tag')
    res_list = get.dbGet().getOneComment(commodity_id,tag)
    res = json.dumps(res_list, ensure_ascii=False)
    return HttpResponse(res, content_type="application/json,charset=utf-8")
'''
根据店铺获取商品
'''
def getGoodsByShopName(request):
    commodity_id = request.GET.get('commodity_id')
    tag = request.GET.get('tag')
    res_list = get.dbGet().getGoodsByShopName(commodity_id,tag)
    res = json.dumps(res_list, ensure_ascii=False)
    return HttpResponse(res, content_type="application/json,charset=utf-8")

'''
根据商品id获取商品详细信息
'''
def getCommentBycommodity_id(request):
    commodity_id = request.GET.get('commodity_id')
    tag = request.GET.get('tag')
    limit = request.GET.get('limit')
    offset = request.GET.get('offset')
    res_list = get.dbGet().getCommentBycommodity_id(commodity_id,tag,limit,offset)
    res = json.dumps(res_list, ensure_ascii=False)
    return HttpResponse(res, content_type="application/json,charset=utf-8")
'''
根据商品id获取商品评论大小
'''
def getGoodsCommentSize(request):
    commodity_id = request.GET.get('commodity_id')
    tag = request.GET.get('tag')
    res_list = get.dbGet().getGoodsCommentSize(commodity_id,tag)
    res = json.dumps(res_list, ensure_ascii=False)
    return HttpResponse(res, content_type="application/json,charset=utf-8")
'''
    搜索与此商品品牌类似的商品
    '''

def getLikelyGoods(request):
    commodity_id = request.GET.get('commodity_id')
    res_list = get.dbGet().getLikelyGoods(commodity_id)
    res = json.dumps(res_list, ensure_ascii=False)
    return HttpResponse(res, content_type="application/json,charset=utf-8")

'''
物品搜索 根据关键字
'''
def searchGoods(request):
    searchKey = request.GET.get('searchKey')
    res_list = get.dbGet().searchGoodsByBrand(searchKey)
    if len(res_list) != 0:
        res = json.dumps(res_list, ensure_ascii=False)
        return HttpResponse(res, content_type="application/json,charset=utf-8")

    res_list = get.dbGet().searchGoodsByModel(searchKey)
    res = json.dumps(res_list, ensure_ascii=False)
    return HttpResponse(res, content_type="application/json,charset=utf-8")



'''
获取商品评论的情感分析总结果，分析商品的情感
'''
def getCommentGrade(request):
    commodity_id = request.GET.get('commodity_id')
    tag = request.GET.get('tag')
    res_list =nlp_process.process(commodity_id,tag)
    res = json.dumps(res_list, ensure_ascii=False)
    return HttpResponse(res, content_type="application/json,charset=utf-8")


'''
获取评论的词云  返回base64编码
'''

def getWordCloudPic(request):
    commodity_id = request.GET.get('commodity_id')
    tag = request.GET.get('tag')
    res =generate_wordcloud.draw_wordcloud(commodity_id,tag)
    resp =  HttpResponse(res, content_type="application/json,charset=utf-8")
    # resp["Access - Control - Allow - Origin"] = "*"
    # resp["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    # resp["Access-Control-Allow-Headers"] = "*"
    return resp