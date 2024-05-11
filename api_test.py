import requests

active_url = "http://127.0.0.1:8000/item"
headers = {
    "Host": "127.0.0.1",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309092b) XWEB/8555 Flue",
    "Content-Type": "application/json",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Language": "zh-CN,zh;q=0.9",
}
sign_data1 = {"name": "zx","price": 11.3,"id": "s21","msg": 2024}
sign_data = {"person":{"name": "zx","desc": "11.3","age": 21,"year": 2024}}
sign_data2 = {"name": "zx","desc": "11.3","age": 21,"year": 2024}
#签到
sign_response = requests.post(active_url, headers=headers, json=sign_data)
json_sign = sign_response.content.decode()
print(json_sign)
