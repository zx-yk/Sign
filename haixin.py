import requests
import time
import json
import sys
active_url = "https://cps.hisense.com/customerAth/activity-manage/activityUser/participate"
getNum_url = "https://cps.hisense.com/customerAth/activity-manage/activityUser/getActivityInfo?code=a55ca53d96bd43be81c0df7ced7ef2b0"
add_url = "https://cps.hisense.com/customerAth/activity-manage/activityUser/partyExchange"

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
    "Cookie": "BIGipServerPOOL_DMZOCP_9080=!aAXEKnUbs0gx9QkR4GLrgeLVCXJLUz09oadC9gaZuDlLcwI05eRQ/A3usKMMQgzFjh7hd8hMnM3XGak=; TOKEN_ACTIVITY=MWFpYWtLQUowU3EzT1BMZmxYUVNLTHlRdVl1V3JNTWk2T3dtLXl3VHQ0Q2xROGQzLVFINHBqQk9aTVVaWHFZeGo4aVRNQTQ1d1M4YmNsLUM3QUxrbXZmeXd5S2diN0I5V18xSkkzNzB5Y0lQRnJzcGpRTzlRaFBZTml3aFI0YTF5OUtUbWtCOU5Lb3h1VFJTWlA1dzdfbE9SWTlUa01CcmxldnBaUmlxMHlPbDJVaFlQQ3dNM3UwYk1BNWhWWW9hVDJ3cnR5dVJ5Vw==; SCORE_CENTER_IAM_AUTH_ID=cc71eb82-a5f7-4476-84e7-99fc579eb655; SCORE_SCENTER=YXBpOmdhdGV3YXk6bG9naW46dXNlcjoxMDU2MzIxNTM=; BIGipServerPOOL_OCP_JUCLOUD_80=!wjePA/qhRmz3IAslLGyqlytKq47lSI/2iW462cTKa6ETdCTkbZjOtHspF/nlSINZWBEOsUFFJhN+5F0=",
    "Accept-Encoding": "gzip, deflate"
}
data = {"code":"a55ca53d96bd43be81c0df7ced7ef2b0","gameScore":"600","gameSignature":"9452bd1f3338bd2bf6df1a84b7b4e7bd"}
add_data = {"code":"a55ca53d96bd43be81c0df7ced7ef2b0"}
sign_data = {"code":"74f51fd29cea445e9b95eb0dd14fba40"}
#签到
sign_response = requests.post(active_url, headers=headers, json=sign_data)
json_sign = sign_response.content.decode()
# 解析JSON字符串为Python字典
result_sign = json.loads(json_sign)
# 提取obtainScore和resultCode的值
result_code = result_sign["resultCode"]
if result_code == "00000":
    obtain_score = result_sign["data"]["obtainScore"]
    print("签到获得", obtain_score, "积分")
elif result_code == "B0110":
    print("用户信息已过期")
    sys.exit()
elif result_code == "A0202":
    print("已签到")
else:
    print(sign_response.content.decode())
#打地鼠
while True:
    response = requests.post(active_url, headers=headers, json=data)
    # time.sleep(0.4)  # 200毫秒延迟
    json_str = response.content.decode()
    # 解析JSON字符串为Python字典
    result_data = json.loads(json_str)
    # 提取obtainScore和resultCode的值
    result_code = result_data["resultCode"]
    if result_code == "00000":
        obtain_score = result_data["data"]["obtainScore"]
        print("打地鼠获得", obtain_score, "积分")
        time.sleep(40)
        continue
    else:
        print("打地鼠次数不足，查询可否兑换")
        getNum_response = requests.get(getNum_url, headers=headers)
        # 解析JSON字符串为Python字典
        result_numData = json.loads(getNum_response.content.decode())
        # 提取obtainScore和resultCode的值
        result_num = result_numData["data"]["isExchange"]
        if result_num == 1:
            add_response = requests.post(add_url, headers=headers, json=add_data)
            result_addData = json.loads(add_response.content.decode())
            result_add = result_addData["resultCode"]
            if result_add == "00000" :
                print("兑换次数+1")
                time.sleep(30)
                continue
            else:
                time.sleep(30)
                continue
        else:
            print("兑换次数已达上限")
            break
print("运行结束")
