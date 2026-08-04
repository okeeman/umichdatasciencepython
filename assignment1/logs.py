import re
def logs():
    with open("assets/logdata.txt", "r") as file:
        logdata = file.read()

    # One to three digits, escape literal dots.
    urls = re.findall(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', logdata)
    user_names = re.findall(r'-\s(.*?)\s\[', logdata)
    times = re.findall(r'\[(.*?)]', logdata)
    requests = re.findall(r'\"(.*?)\"', logdata)
  
    log_data = []
    for url, user, time, request in zip(urls, user_names, times, requests):
        log_data.append({"host": url, "user_name": user, "time": time, "request": request})
      
    return log_data
