from datetime import datetime

def log_write(info_str):
    now = str(datetime.now())[:-4]
    with open('./ticketInfo/info.txt', 'a') as f:
        f.write("<" + now + "> " + info_str + '\n')

if __name__ == "__main__":
    log_write("test\ntest")