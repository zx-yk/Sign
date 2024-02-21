import requests

url = "https://cps.hisense.com/customerAth/activity-manage/activityUser/getActivityInfo?code=74f51fd29cea445e9b95eb0dd14fba40"

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
    "Referer": "https://cps.hisense.com/static/game_sign.shtml?code=74f51fd29cea445e9b95eb0dd14fba40",
    "Accept-Encoding": "gzip, deflate",
    "Cookie": "BIGipServerPOOL_DMZOCP_9080=!aAXEKnUbs0gx9QkR4GLrgeLVCXJLUz09oadC9gaZuDlLcwI05eRQ/A3usKMMQgzFjh7hd8hMnM3XGak=; TOKEN_ACTIVITY=MWE2THNPQUVwOUlHS1g0bjN1aW5naHh0a2JabVhCUkRXMDN4SWhhQkxoeExaMVNFaHEwZURHZzY5Z2dQQWhNa0MtN3VFZDl6NjhaZmp3dmx6dlQwZ3hMc1A1bFd5Q2Jkd3VsbmRjR2xwOWlMOXdwX2YtZkxxaTl2NG5uMUI2alprWDc2TFZEMHhtTkhRRzVGNTJ0YkFyNUcyN3FDYmhQZzBPUWFxZkkyck9UQTFPNXM5Z3BteXdRcGtuMndrVWwxN21SMk83czlEVQ; SCORE_CENTER_IAM_AUTH_ID=cc71eb82-a5f7-4476-84e7-99fc579eb655; SCORE_SCENTER=YXBpOmdhdGV3YXk6bG9naW46dXNlcjoxMDU2MzIxNTM=; BIGipServerPOOL_OCP_JUCLOUD_80=!wjePA/qhRmz3IAslLGyqlytKq47lSI/2iW462cTKa6ETdCTkbZjOtHspF/nlSINZWBEOsUFFJhN+5F0=",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

response = requests.get(url, headers=headers)
print(response.content.decode())
