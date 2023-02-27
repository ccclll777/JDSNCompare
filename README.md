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

## 将两个平台的数据汇总到前端界面，进行价格比较
 项目技术栈
python语言开发后端，使用django框架（python3.7）
Html+css+javascript开发前端使用vue+iview框架
项目地址：http://39.105.44.114:38888/comparePrice/index.html
###首页
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200528230208372.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhaWR1XzQxODcxNzk0,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200528230328522.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhaWR1XzQxODcxNzk0,size_16,color_FFFFFF,t_70)
###点击相关商品，进入商品列表
可以按照价格，评论数排序，并且实现了分页功能，并且不同平台的商品有着不同的标记（苏宁易购 或者京东）
（1）按价格降序
![在这里插入图片描述](https://img-blog.csdnimg.cn/2020052823035890.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhaWR1XzQxODcxNzk0,size_16,color_FFFFFF,t_70)
（2）按评论数量降序
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200528230414262.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhaWR1XzQxODcxNzk0,size_16,color_FFFFFF,t_70)
（3）实现分页
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200528230449737.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhaWR1XzQxODcxNzk0,size_16,color_FFFFFF,t_70)
###搜索商品功能
可以根据品牌型号搜索，后端会自动对搜索的关键词和商品的品牌，商品的描述进行比对，选择编辑距离最小的进行输出（由于没有提前建好关键词索引，所以搜索比较慢，需要20s左右，以后加入索引可能会更快）
（1）搜索iPhone XS MAX
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200528230521153.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhaWR1XzQxODcxNzk0,size_16,color_FFFFFF,t_70)
（2）搜索华为 mate 30
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200528230536856.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhaWR1XzQxODcxNzk0,size_16,color_FFFFFF,t_70)
（3）搜索惠普（HP）光影精灵
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200528230551906.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhaWR1XzQxODcxNzk0,size_16,color_FFFFFF,t_70)
### 商品详情界面
（1）展示商品的详细信息
可以点击链接直接到售卖的店铺
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200528230615922.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhaWR1XzQxODcxNzk0,size_16,color_FFFFFF,t_70)
（2）商品比较
会查询出和这个手机型号相同或相似的手机品牌，可以进行比较
（后端实现为，先搜索品牌和型号，然后对比相似性，最后在对比商品描述的相似性，寻找相似商品）
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200528230632417.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhaWR1XzQxODcxNzk0,size_16,color_FFFFFF,t_70)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200528230642713.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhaWR1XzQxODcxNzk0,size_16,color_FFFFFF,t_70)
（3）绘制评论词云
将爬取到的评论信息绘制成词云，供用户查看。
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200528230703764.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhaWR1XzQxODcxNzk0,size_16,color_FFFFFF,t_70)
（4）展示爬取到的商品评论，并对整体已经每一句评论做了情感分析
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200528230717978.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2JhaWR1XzQxODcxNzk0,size_16,color_FFFFFF,t_70)
