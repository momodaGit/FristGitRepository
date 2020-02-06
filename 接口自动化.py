import requests 

url = 'https://www.baidu.com'

request = requests.get(url)

#打印访问地址的URL
print(request.url)

#打印访问的文本
print(request.text)

#打印返回状态码
print("返回数据相应码：",request.status_code)
