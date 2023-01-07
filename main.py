
import requests
import re

from logWriter import log_write
from mongo import insert_log, find_log_by_link
from lineNotify import lineNotifyMessage
from env import line_token, web_sid
# 權杖內容
token = line_token

if __name__ == "__main__":
    log_write("[I] PYTHON IS RUNNING...")

    sess = requests.Session()

    header = requests.utils.default_headers()
    header['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    # plz enter your SID
    user_cookie ={
        "SID" : web_sid
    }
    sess.cookies.update(
        user_cookie
    )
    res_html = sess.get("https://tixcraft.com/activity")

    tikct_html = res_html.text.replace('\n','')
    log_in_status = re.findall('(林藤恩)', tikct_html)
    if log_in_status is not None:
        info = "[I] login success!!"
    else:
        info = "[W] login failed!!"
    log_write(info)

   
    # origin
    match_pattern = 'class="fcTxt">(.*?)</tr>'
    tikct_data = re.findall(match_pattern, tikct_html)
    flag = False
    for tikct_detail in tikct_data:
        data = re.findall("<td>(.*?)</td>", tikct_detail)
        # print(data)
        link = re.findall('href="(.*?)"', data[1])[0]
        title = re.findall('">(.*?)</a>', data[1])[0]
        data_dict = {
            'date' : data[0],
            'link' : link,
            'title': title,
            'filed': data[2]
        }
        # 字典輸出，產出連結
        # print(data_dict)
        # print("https://tixcraft.com" + data_dict['link'].replace('detail', 'game'))
        if find_log_by_link(link):
            insert_log(data_dict)
            log_write("[I] new log was inserted, title is "+ title)
            flag = True
    if flag:
        lineNotifyMessage(token, "[I] website was update, plz check out website!")
    else:
        log_write("[I] the website is not up to date yet...")
        