import requests

url = "https://suggest.taobao.com/sug?k=1&area=c2c"

data = {
    'q': '电脑',
    'code': 'utf-8',
}
resp = requests.get(url, data)
with open('./淘宝.json', mode='w', encoding='utf-8') as f:
    f.write(resp.text)
print(resp.text)
