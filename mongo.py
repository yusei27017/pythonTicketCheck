import pymongo

from logWriter import log_write
from env import mongo_uri
conn = pymongo.MongoClient(mongo_uri)
db = conn.golangGinBlog
col = db.ticket

def insert_log(log):
    # for log in log_array:
    res = col.insert_one(log)

def find_log_by_link(link):
    try:
        results = col.find({'link': link})
        if any(results):
            # results is list, need use attr
            return False
        else:
            # 找不到log，網頁已更新，插入新資料並且通知
            return True
    except:
        log_write("[W] mongo search failed!!")


if __name__ == "__main__":
    bool_res = find_log_by_link('/activity/detail/22_tvl')
    print(bool_res)