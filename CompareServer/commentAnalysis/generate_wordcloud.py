# encoding=utf8
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import imageio
import io
import base64
import pymysql
def read_data_jd(commodity_id):
    # 获取数据库链接

    connection = pymysql.connect(
        host='39.105.44.114',
        port=3306,
        user='jd_sn_p',
        password='jd_sn_p',
        db='jd_sn_p'
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
        host='39.105.44.114',
        port=3306,
        user='jd_sn_p',
        password='jd_sn_p',
        db='jd_sn_p'
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


def draw_wordcloud(commodity_id,tag):
    if tag == '京东':

        datas = read_data_jd(commodity_id)
    else:
        datas = read_data_sn(commodity_id)
        if len(datas) == 0:
            return
    comments_concat = ""
    for data in datas:
        # print(data[3])
        comments_concat += data[0].replace("hellip", "").replace("rdquo", "")
    font_path = "Hiragino Sans GB.ttc"
    weight = 800
    height = 300
    bg_img = imageio.imread("jdlogo.png")
    # wordcloud = WordCloud(font_path=font_path,
    #                       width=weight,
    #                       height=height,
    #                       background_color='white',
    #                       mask=bg_img).generate(comments_concat).to_image()
    wordcloud = WordCloud(font_path = font_path,
                          width=weight,
                          height=height,
                          background_color='white',
                          mask = bg_img ).generate(comments_concat)
    img = io.BytesIO()
    wordcloud.to_image().save(img, "PNG")

    img_base64 = base64.b64encode(img.getvalue()).decode("ascii")
    return img_base64
    # print(wordcloud)
    # plt.imshow(wordcloud, interpolation='bilinear')
    # plt.axis("off")
    # plt.show()

# draw_wordcloud("100000011349")