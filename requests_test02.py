"""
案例1
【带 查询参数 的get请求】使用Requests库，请求 tpshop商城 搜索商品接口。查询 iphone
"""
import requests
# 方法一
resp = requests.get(url="http://tpshop-test.itheima.net/Home/Goods/search.html?q=iPhone")
# 方法二
resp1 = requests.get(url="http://tpshop-test.itheima.net/Home/Goods/search.html",params={"q":"iPhone"})
print(resp1.text)