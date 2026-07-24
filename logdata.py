import re
import json

def logs():
    with open("logdata.txt", "r") as file:
        logdata = file.read()
        #print(logdata)

    # YOUR CODE HERE
    # host names
    # not always 3 digits between the dots, can be 1-3
    urls = re.findall(r'(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', logdata)
    print(type(urls)) # list
    #print(urls)

    # usr names
    user_names = re.findall(r'-\s(.*?)\s\[', logdata)
    # this way captures a - where there is no user name.
    #print(user_names)

    times = re.findall(r'\[(.*?)]', logdata)
    # (.*?) Captures everything in a non-greedy manner (stops at the first closing bracket).
    #print(times)

    requests = re.findall(r'\"(.*?)\"', logdata)
    #print(requests)

    log_data = []

    for url, user, time, request in zip(urls, user_names, times, requests):
        log_data.append({"host":url, "user_name":user, "time":time, "request":request})

    #print(log_data)
    """"
    with open('logs.txt', 'w+') as f:
        for items in log_data:
            f.write('%s\n' % items)
    
    """
    return log_data

print(len(logs()))
print("before assert")
assert len(logs()) == 979
print("after assert") # didn't throw an exception

print("before 2nd assert")
one_item={'host': '146.204.224.152',
  'user_name': 'feest6811',
  'time': '21/Jun/2019:15:45:24 -0700',
  'request': 'POST /incentivize HTTP/1.1'}
assert one_item in logs(), "Sorry, this item should be in the log results, check your formating"
print("after 2nd assert")

if __name__ == '__main__':
    logs()
    print("Executed")