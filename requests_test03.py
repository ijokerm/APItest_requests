"""
案例2
【带 表单数据 的post请求】使用Requests库，完成 tpshop商城 登录接口调用。返回 ”验证码错误“ 即可。
"""
import requests

resp = requests.post(url="http://tpshop-test.itheima.net/index.php?m=Home&c=User&a=do_login&t=0.7094195931397276",
                    headers={"Content-Type": "application/x-www-form-urlencoded"},
                    data={"username": "13012345678", "password": "1234567", "verify_code":"8888"})

# 打印响应结果为json格式 --网站有误 无需访问
print(resp.json())