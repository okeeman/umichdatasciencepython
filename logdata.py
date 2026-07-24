import re

def logs():
    with open("logdata.txt", "r") as file:
        logdata = file.read()
        
    urls = re.findall(r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', logdata)

    user_names = re.findall(r'-\s(.*?)\s\[', logdata)

    times = re.findall(r'\[(.*?)]', logdata)

    requests = re.findall(r'\"(.*?)\"', logdata)

    log_data = []

    for url, user, time, request in zip(urls, user_names, times, requests):
        log_data.append({"host":url, "user_name":user, "time":time, "request":request})

    return log_data

if __name__ == '__main__':
    assert len(logs()) == 979

    one_item={'host': '146.204.224.152',
              'user_name': 'feest6811',
              'time': '21/Jun/2019:15:45:24 -0700',
              'request': 'POST /incentivize HTTP/1.1'}
    assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"
