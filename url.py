import requests
import pyshorteners
import sys

print("......................................")
print("help commands")


print("..................................")
print("smart_url")
print("this tool help u to find where do the short url travel also it will help u to create a short url without "+"any ads")
print("installation: pip install pyshorteners \n pip install requests")

print("......................................")
print("-t - use this to track your url")
print("-c -use this to create your own short url")
print("......................................")
command = input("enter ur command:")
if '-c' in command:
    input_url = input("enter the url:")
    shortener = pyshorteners.Shortener()
    new_url = shortener.tinyurl.short(input_url)
    print("your new_url:"+new_url)

if '-t' in command:
    input_url = input("enter the url:")
    resp = requests.get(input_url)
    if resp.history:
        print('\nYes URL is Redirected or Shorten!')
        print('Here the following redirected chain...\n')
        for r in resp.history:
            print('|', r.status_code, '|', r.url, '|', r.reason)
        print('\nEND URL :', resp.url)
        print('Status Code :', resp.status_code, resp.reason)
    else:
        print('\nURL is Not Redirected or Shorten!')
        print('END URL :', resp.url)
        print('Status Code :', resp.status_code, resp.reason)


