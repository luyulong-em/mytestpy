import requests

# 百度

url = 'http://www.baidu.com'

# 发送请求

resp = requests.get(url)
resp.encoding = 'utf-8'
print(resp)

with open('myBaidu.html', mode='w', encoding='utf-8') as f:
    f.write(resp.text)
    print('over!!')
