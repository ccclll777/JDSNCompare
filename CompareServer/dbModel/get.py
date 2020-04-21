
from fuzzywuzzy import process
from commentAnalysis import nlp_process
import MySQLdb


class dbGet:
    def __init__(self):
        self.conn = MySQLdb.connect(
            host='39.105.44.114',
            port=3306,
            user='jd_sn_p',
            passwd='jd_sn_p',
            db='jd_sn_p',
            charset='utf8'
        )
        self.cur = self.conn.cursor()

    '''
    返回商品列表 
    根据商品类型和不同的品牌 不同的平台
    分页查询 每次返回一页
    '''
    def getGoodsList(self,commodity_brand,commodity_type,limit,offset,tag):
        res = []
        # if(tag == '京东'):
        aa = self.cur.execute("select commodity_id,commodity_title,commodity_shop_name,commodity_price,comment_count,"
                              "commodity_pic from JDSNcommodity where commodity_brand = '{}' and commodity_type = '{}' and comment_count>100 and tag ='{}' and  commodity_price != '0.0' "
                              "order by comment_count limit {} offset {}".format(commodity_brand,commodity_type,tag,limit,offset))
        # else:
        #     aa = self.cur.execute(
        #         "select commodity_id,commodity_title,commodity_shop_name,commodity_price,commodity_comment_count,"
        #         "commodity_pic from JDSNcommodity where commodity_brand = '{}' and commodity_type = '{}' and commodity_price != '0.0' and commodity_comment_count>100 "
        #         "order by commodity_comment_count limit {} offset {}".format(commodity_brand, commodity_type, limit, offset))
        info = self.cur.fetchmany(aa)
        for item in info:
            t = {'commodity_id': item[0], 'commodity_title': item[1], 'commodity_shop_name': item[2], 'commodity_price': item[3],
                 'comment_count': item[4],'commodity_pic': item[5]}
            res.append(dict(t))
        return res

    '''
    返回商品列表的总大小
    根据商品类型和不同的品牌 不同的平台
    为分页查询 提供准备
    '''
    def getGoodsListSize(self, commodity_brand,commodity_type, tag):
        res = []
        # if (tag == '京东'):
        aa = self.cur.execute("select count(*) from JDSNcommodity where commodity_brand = '{}'and commodity_type = '{}' and comment_count>100  and tag ='{}'".format(commodity_brand,commodity_type,tag))
        # else:
        #     aa = self.cur.execute("select count(*) from SNcommodity where commodity_brand = '{}' and commodity_type = '{}' and commodity_comment_count>100  ".format(commodity_brand,
        #                                                                                    commodity_type))
        info = self.cur.fetchmany(aa)
        for item in info:
            t = {'getGoodsListSize': item[0]}
            res.append(dict(t))
        return res

    '''
    根据商品id获取商品的详细信息
    '''
    def getGoodInfo(self, commodity_id):
        res = []
        # if (tag == '京东'):
        aa = self.cur.execute(
                "select * from JDSNcommodity where commodity_id = '{}' ".format(commodity_id))
        info = self.cur.fetchmany(aa)
        for item in info:
                t = {'commodity_id': item[1], 'commodity_title': item[2], 'commodity_url': item[3],
                     'commodity_shop_name': item[4],
                     'commodity_price': item[5],
                     'commodity_brand': item[6], 'commodity_model': item[7], 'comment_count': item[8],
                     'commodity_pic': item[10], 'commodity_type': item[11]}
                res.append(dict(t))
        # else:
        #     aa = self.cur.execute(
        #         "select *  from SNcommodity where  commodity_id = '{}' ".format(commodity_id))
        #     info = self.cur.fetchmany(aa)
        #     for item in info:
        #         t = {'commodity_id': item[1], 'commodity_title': item[2], 'commodity_url': item[8],
        #              'commodity_shop_name': item[6],
        #              'commodity_price': item[3],
        #              'commodity_brand': item[4], 'commodity_model': item[5], 'comment_count': item[7],
        #              'commodity_pic': item[10], 'commodity_type': item[11]}
        #         res.append(dict(t))
        return res

    '''
    随机获取某条评论
    '''
    def getOneComment(self, commodity_id, tag):
        res = []
        if (tag == '京东'):
            aa = self.cur.execute(
                "select content from JDcomment where commodity_id = '{} '".format(commodity_id))
        else:
            aa = self.cur.execute(
                 "select content from SNcomment2 where commodity_id = '{}  '".format(commodity_id))

        info = self.cur.fetchmany(aa)

        if len(info) == 0:
            return res
        else:
        # for item in info:
            t = {'comment_content': info[0][0]}
            res.append(dict(t))
            return res

    '''
    根据店铺获取商品
    '''
    def getGoodsByShopName(self, commodity_id, tag):
        res = []
        # if (tag == '京东'):
        aa = self.cur.execute(
                "select commodity_id,commodity_price,commodity_url,commodity_model,commodity_pic from JDSNcommodity where commodity_shop_name = (select commodity_shop_name from JDSNcommodity where commodity_id = '{}') and tag = '{}' order by comment_count ".format(commodity_id,tag))
        # else:
        #     aa = self.cur.execute(
        #          "select commodity_id,commodity_price,commodity_url,commodity_model,commodity_pic from SNcommodity where commodity_shop_name = (select commodity_shop_name from SNcommodity where commodity_id = '{}')  order by commodity_comment_count".format(commodity_id))
        info = self.cur.fetchmany(aa)
        if len(info) < 20:

            for item in info:
                t = {'commodity_id': item[0], 'commodity_price': item[1], 'commodity_url': item[2],
                     'commodity_model': item[3],
                     'commodity_pic': item[4]}
                res.append(dict(t))
        else:
            for i in range(0,20):
                item = info[i]
                t = {'commodity_id': item[0], 'commodity_price': item[1], 'commodity_url': item[2],
                     'commodity_model': item[3],
                     'commodity_pic': item[4]}
                res.append(dict(t))

        return res

    '''
    根据商品id获取商品评论
    '''
    def getCommentBycommodity_id(self, commodity_id, tag,limit,offset):
        res = []
        if (tag == '京东'):
            aa = self.cur.execute(
                "select * from JDcomment where commodity_id = '{}' limit {} offset {}".format(commodity_id,limit,offset))
            info = self.cur.fetchmany(aa)
            for item in info:
                sentiments = nlp_process.snowanalysis(item[5])
                t = {'id': item[0], 'commodity_name': item[2], 'comment_time': item[3],
                     'label': item[4],
                     'content': item[5],'sentiments':sentiments }
                res.append(dict(t))
        else:
            aa = self.cur.execute(
                "select * from SNcomment2 where commodity_id = '{}' limit {} offset {}".format(commodity_id,limit,offset))
            info = self.cur.fetchmany(aa)
            for item in info:
                sentiments = nlp_process.snowanalysis(item[4])
                t = {'id': item[0], 'commodity_name': item[2], 'comment_time': item[3],
                     'content': item[4],
                     'label': item[5],'sentiments':sentiments  }
                res.append(dict(t))

        return res
    '''
    根据商品id 获取总评论数
    '''
    def getGoodsCommentSize(self, commodity_id, tag):
        res = []
        if (tag == '京东'):
            aa = self.cur.execute(
                "select count(*) from JDcomment where commodity_id = '{}' ".format(commodity_id))
        else:
            aa = self.cur.execute(
                "select count(*) from SNcomment2 where commodity_id = '{}' ".format(commodity_id))
        info = self.cur.fetchmany(aa)
        for item in info:
            t = {'getGoodsCommentSize': item[0]}
            res.append(dict(t))
        return res

    '''
    搜索与此商品品牌类似的商品
    '''
    def getLikelyGoods(self, commodity_id):
        goodsInfo = self.getGoodInfo(commodity_id)
        commodity_brand = goodsInfo[0]['commodity_brand']
        commodity_title = goodsInfo[0]['commodity_title']
        commodity_model = goodsInfo[0]['commodity_model']
        commodity_type = goodsInfo[0]['commodity_type']
        aa = self.cur.execute(
            "select * from JDSNcommodity where commodity_brand = '{}' and commodity_type = '{}' ".format(commodity_brand,commodity_type))
        info = self.cur.fetchmany(aa)
        list = []
        for item in info:
            list.append(item[7])
        list2 = process.extract(commodity_model,list,limit=7)
        list3 = []
        for i in list2:
            list3.append(i[0])
        res  = []
        for item in info:
            if item[7] in list3:
                t = {'commodity_id': item[1], 'commodity_title': item[2], 'commodity_url': item[3],
                     'commodity_shop_name': item[4],
                     'commodity_price': item[5],
                     'commodity_brand': item[6], 'commodity_model': item[7], 'comment_count': item[8],
                     'commodity_pic': item[10], 'commodity_type': item[11],'tag': item[12]}
                res.append(dict(t))
        return res
    '''
    根据品牌搜索商品
    '''
    def searchGoodsByBrand(self, commodity_brand):
        aa = self.cur.execute(
            "select commodity_id,commodity_title,commodity_shop_name,commodity_price,comment_count,"
            "commodity_pic,tag from JDSNcommodity where commodity_brand = '{}' limit 200".format(commodity_brand))
        info = self.cur.fetchmany(aa)
        res = []
        for item in info:
            t = {'commodity_id': item[0], 'commodity_title': item[1], 'commodity_shop_name': item[2],
                 'commodity_price': item[3],
                 'comment_count': item[4], 'commodity_pic': item[5],'tag':item[6]}
            res.append(dict(t))
        return res

    '''
       根据型号搜索商品
       
    '''
    def searchGoodsByModel(self, searchKey):
        res = []
        aa = self.cur.execute("select * from JDSNcommodity limit 5000 ")
        info = self.cur.fetchmany(aa)
        list = []
        for item in info:
            list.append(item[7])
            #根据编辑距离排序，搜索最相似的10条
        list2 = process.extract(searchKey, list, limit=10)
        list3 = []
        for i in list2:
            list3.append(i[0])

        for item in info:
            if item[7] in list3:
                t = {'commodity_id': item[1], 'commodity_title': item[2], 'commodity_url': item[3],
                         'commodity_shop_name': item[4],
                         'commodity_price': item[5],
                         'commodity_brand': item[6], 'commodity_model': item[7], 'comment_count': item[8],
                         'commodity_pic': item[10], 'commodity_type': item[11], 'tag': item[12]}
                res.append(dict(t))

        return res

