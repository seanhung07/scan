import  urllib3.request
import requests
import re 
def main():
    ans = input("What information you went to get? \n1. Headers \n2. Dns information \n3. Links in URL \n4. GEO IP \nEnter the Number: ")
    if(ans==1):
        url = raw_input("Enter the url: ")
        header(url)
    elif(ans==2):
        url = raw_input("Enter the url: ")
        dns(url)
    elif(ans==3):
        url = raw_input("Enter the url: ")
        links(url)
    elif(ans==4):
        ip = raw_input("Enter the IP: ")
        geoip(ip)
def header(url):
    http = urllib3.PoolManager()
    url =  http.request('GET',url)
    print(url.headers)
def dns(url):
    result = requests.get("https://api.hackertarget.com/hostsearch/?q={}".format(url))
    print(result.text)
def links(url):
    links = requests.get("https://api.hackertarget.com/pagelinks/?q={}".format(url))
    print(links.text)
def geoip(ip):
    ip = requests.get("https://api.hackertarget.com/geoip/?q={}".format(ip))
    dataList = ip.text.split('\n')
    lat = float(str(dataList[-2].split(': ')[1]))
    long = float(str(dataList[-1].split(': ')[1]))
    print((lat,long))
    print(ip.text)
    print("https://www.google.com/maps/place/"+str(lat)+","+str(long))
main()