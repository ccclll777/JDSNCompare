# JDSNCompare
爬取京东苏宁商品信息（手机 笔记本电脑） 以及商品的评论   然后继承到web上，实现了价格评价的比较  并且对每件商品评论进行了情感分析，绘制了评论的词云
# JDSNSpider
使用scrapy爬取了京东苏宁的search页面搜索手机和笔记本电脑的信息，以及商品的详细信息，商品的图片，并且爬取了商品的评论
对于京东实现了扫码登陆，苏宁需要自己网页模拟登陆后，复制cookie到对应位置

# CompareWeb
使用vue+iview实现
将京东苏宁的商品信息展示，可以进行相似商品的价格的对比 查看评论的情感分析结果，查看评论的词云



# CompareServer
使用django实现
实现了后端的请求接口，实现了评论的情感分析（使用snownlp），以及词云的绘制 ，后期准备针对评论训练模型，实现情感的分类。

# 详细介绍
https://ccclll777.github.io/2020/05/28/Undergraduate-Curriculum-Design/CurriculumDesign-jdsnCompare/
