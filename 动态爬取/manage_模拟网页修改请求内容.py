import requests
import json
url = ('https://dict.iciba.com/dictionary/word/suggestion?word=acvivat&nums=5&ck=709a0db45332167b0e2ce1868b84773e'
       '&timestamp=1697276843114&client=6&uid=123123&key=1000006&is_need_mean=1&signature'
       '=3e1b802888c7d95cf4180b6d8b22c5ad')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 '
                  'Safari/537.36 Edg/117.0.2045.60'
}

form_data = {
    "from": "en",
    'to': 'zh',
    'q': 'activate'
}

response = requests.post(url, params=form_data, headers=headers)
print(json.loads(response.content.decode('UTF-8')))