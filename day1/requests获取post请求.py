import requests

url = 'https://fanyi.baidu.com/sug'
data = {
    'kw': input('输入')
}
resp = requests.post(url, data)

print(resp.json())
