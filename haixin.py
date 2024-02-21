import requests

url = "https://cps.hisense.com/customerAth/activity-manage/activityUser/participate"

headers = {
    "Host": "cps.hisense.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309092b) XWEB/8555 Flue",
    "Content-Type": "application/json",
    "Origin": "https://cps.hisense.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://cps.hisense.com/static/game_playDiglett.shtml?code=a55ca53d96bd43be81c0df7ced7ef2b0",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "BIGipServerPOOL_DMZOCP_9080=!nN4jUYmcmFubc6YR4GLrgeLVCXJLUy11h0HR+eScO/NVNDpPF+EJzu8anRdQUJdIdsa0SMwobgUySfg=; TOKEN_ACTIVITY=MWFKSmdEQUlhYjRyd0s5ejJBeEZGSDU3U3dCQzlNT0cwTUZhQmVQVUtqamQxMW9xeVRNdnF1TVRwdVVtaXM4bmhud3Z2WXpMUXFXT1l1M3RNd3MyYlZvdi1LamlsUUJuQVVyazQ5OEVYNDZrNzY5Vk1aTlFqV242TjM1Znl5OW1mVGdKMXNNcTRHdVByWG9oMjI0cHNRZmFyWTFhTHBRUVFzQ1hiaXZGX09BQnluTXAzMG5YQVNzYmQyWEo1OVNCbHlGSmZNcmtqeQ; SCORE_CENTER_IAM_AUTH_ID=4c0aeb79-5756-4e41-b804-801021d930c4; SCORE_SCENTER=YXBpOmdhdGV3YXk6bG9naW46dXNlcjoxMDU2MzI4NzU=; BIGipServerPOOL_OCP_JUCLOUD_80=!pWFZcKtt0LTfwSIlLGyqlytKq47lSLkGKS/GKkm2Uju3d4BrpleZSAenLCV0TLsTAvKk8Y+lSeTRcwQ=",
    "Accept-Encoding": "gzip, deflate"
}
data = {"code":"a55ca53d96bd43be81c0df7ced7ef2b0","gameScore":"60","gameSignature":"b06c6dd5fdfc100595a3c8de37379da7"}
start_time = time.time()
total_requests = 0
success_count = 0
failure_count = 0
while True:
    response = requests.post(url, headers=headers, json=data)
    #time.sleep(0.4)  # 200毫秒延迟
    json_str = response.content.decode() 
    # 解析JSON字符串为Python字典
    result_data = json.loads(json_str)
    # 提取obtainScore和resultCode的值
    obtain_score = data["data"]["obtainScore"]
    result_code = data["resultCode"]
    print("打地鼠获得", obtain_score,"积分")
    if result_code == 0000:
        print("打地鼠获得", obtain_score,"积分")
    print("resultCode:", result_code)
