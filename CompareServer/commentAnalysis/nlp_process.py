# coding=utf8

from snownlp import SnowNLP
import pymysql as pymysql


def read_data_jd(commodity_id):
    # 获取数据库链接

    connection = pymysql.connect(
        host='xxxxxx',
        port=3306,
        user='xxxxx',
        password='xxxxx',
        db='xxxxx'
    )
    try:
        # 获取会话指针
        with connection.cursor() as cursor:
            # 创建sql语句
            sql = "select content from JDcomment  where commodity_id=%s"

            # 执行sql语句
            cursor.execute(sql, commodity_id)
            datas = cursor.fetchall()

            # 提交数据库
            connection.commit()
    finally:
        connection.close()
    return datas
def read_data_sn(commodity_id):
    # 获取数据库链接

    connection = pymysql.connect(
        host='xxxxxx',
        port=3306,
        user='xxxxx',
        password='xxxxx',
        db='xxxxx'
    )
    try:
        # 获取会话指针
        with connection.cursor() as cursor:
            # 创建sql语句
            sql = "select content from SNcomment  where commodity_id=%s"

            # 执行sql语句
            cursor.execute(sql, commodity_id)
            datas = cursor.fetchall()

            # 提交数据库
            connection.commit()
    finally:
        connection.close()
    return datas

def process(skuid,tag):
    sum_sentiment = 0
    good_counter = 0
    just_so_so_counter = 0
    bad_counter = 0
    if tag == '京东':

        datas = read_data_jd(skuid)
    else:
        datas = read_data_sn(skuid)

    comments_concat = ""
    for data in datas:
        # print(data[3])
        comments_concat += data[0].replace("hellip", "").replace("rdquo", "")
        sentiment = SnowNLP(data[0]).sentiments
        if sentiment > 0.8:
            good_counter += 1
        elif sentiment > 0.4:
            just_so_so_counter += 1
        else:
            bad_counter += 1
        sum_sentiment += sentiment
        # print(data[3])
        # print(sentiment)
    # print("-----------------共计" + str(len(datas)) + "条评论------------------------")
    # print("-----------------0.8以上" + str(good_counter) + "条评论------------------------")
    # print("-----------------0.4-0.8  " + str(just_so_so_counter) + "条评论------------------------")
    # print("-----------------0.4以下" + str(bad_counter) + "条评论------------------------")
    # print("average sentiment is {}".format(sum_sentiment / len(datas)))

    # pic = draw_wordcloud(comments_concat)
    res = []
    if len(datas) != 0:
        t = {'totalCommentCounter': str(len(datas)), 'goodCommentCounter': str(good_counter), 'justSoSoCommentCounter': str(just_so_so_counter),
             'badCommentCounter': str(bad_counter),
             'averageCommentGrade': sum_sentiment / len(datas)}
    else:
        t = {'totalCommentCounter': 0, 'goodCommentCounter': 0,
             'justSoSoCommentCounter':0,
             'badCommentCounter': 0,
             'averageCommentGrade': 0}
    res.append(dict(t))
    return res


def snowanalysis(text):
        s = SnowNLP(text)
        return s.sentiments
# process(100000011349)


