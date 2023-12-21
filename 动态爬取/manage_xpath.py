from lxml import etree

# # 解析本地文件第一种方式
# parser = etree.HTMLParser(encoding="utf-8")
# selector = etree.parse("./boke.html", parser=parser)
# result = etree.tostring(selector)
#
# print(selector)
# print(result)
#
# #解析本地文件或网络动态HTML
# f = open("./boke.html","r",encoding="utf-8")
# data = f.read()
# tree = etree.HTML(data)
# print(tree)

# 整合 建议使用HTML的方式
# tree = etree.HTML(open('./boke.html', 'r', encoding='utf-8').read())
# print(tree)

# 匹配所有的<a>
# //无论在哪里都匹配
tree = etree.HTML(open('./素材/豆瓣.html', 'r', encoding='utf=8').read())
# all_a = tree.xpath('//a')
# print(all_a[0])
# print(etree.tostring(all_a[0],encoding='utf-8').decode('UTF-8'))
# print(etree.tostring(all_a[1],encoding='utf-8').decode('UTF-8'))

# 获取第一个a标签中的文本内容
# 根据第一个节点a 在接着往下进行匹配
# print(all_a[0].xpath('./text()'))

# ul = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li[1]//text()')
# print(ul)
# print(etree.tostring(ul[0],encoding='utf-8').decode("UTF-8"))

# #拿到虚构类最后一个
# ul = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li[last()-1]//text()')
# print(ul)

# # 从第四个开始拿
# ul = tree.xpath('//ul[@class="cover-col-4 clearfix"]/li[position()>3]//text()')
# print(ul)

# 获取所有img标签
# img = tree.xpath('//img')

# #获取src属性
# img = tree.xpath('//a[@class="cover"]/img/@src')
# print(img)
# for i in img:
#     # print(etree.tostring(i,encoding='UTF-8').decode("UTF-8"))
#     print(i)

# # 获取所有price的值
# price = tree.xpath('//a[@price]//text()')
# for p in price:
#     print(p)

# 无论什么标签,只要有price都要
# print(tree.xpath('//*[@price]'))
# print(tree.xpath('//@price'))

# # | 或 匹配ID为test1或test2的
# test_or = tree.xpath('//div[@id="test1"] | //div[@id="test2"]')
# print(test_or)

# # and
# test_or = tree.xpath('//div[@id="test1" and @class="div1"]')
# print(test_or)

# # 查询包含
# div = tree.xpath('//div[contains(@id, "st1")]//text()')
# print(div)
