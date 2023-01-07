import requests

from env import line_token
# 修改為你要傳送的訊息內容
message = 'test!'
# 權杖內容
token = line_token


def lineNotifyMessage(token, msg):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers=headers, params=payload)
    return r.status_code


if __name__ == "__main__":
    lineNotifyMessage(token, message)