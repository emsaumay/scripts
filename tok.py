import requests
import os

accesstoken = ""

def token():
    url = f"{os.environ['CP_API_URL']}/users/refreshAccessToken"

    payload = { "refreshToken": f"{os.environ['CP_RT']}" }
    headers = {
        "content-type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Api-Version": "31",
        "Connection": "keep-alive",
        "Origin": "https://web.classplusapp.com",
        "Referer": "https://web.classplusapp.com/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "accept-language": "en",
        "region": "IN",
        "sec-ch-ua": '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"'
    }

    response = requests.request("POST", url, json=payload, headers=headers).json()
    accesstoken = response['data']['token']
    print(accesstoken)

    short("bat", accesstoken)
    short("material", accesstoken)
    short("rep", accesstoken)

    with open("/config/workspace/classplus-chats/.env", 'r+') as d:
        d.write(f"TOKEN={accesstoken}")
        print("env updated")


def short(path, token):
    linkids = {
        "bat": "lnk_Cuw_2E1DD7",
        "rep": "lnk_Cuw_9dCPkoPNoQz",
        "material": "lnk_Cuw_2E1CDm"
    }

    url = f"https://api.short.io/links/{linkids[path]}"
    paths = {
        "bat": f"{os.environ['BAT']}",
        "material": f"{os.environ['MATERIAL']}",
        "rep": f"{os.environ['REP']}",
    }


    og = paths[path]

    payload = {
        "originalURL": f"{og}?token={token}",
        "path": f"{path}",
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": f"{os.environ['SHORT_AUTH']}"
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response)
    print(f"{path} updated")

token()