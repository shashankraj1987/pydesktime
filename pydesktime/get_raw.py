import requests
# import json
from datetime import date

def todays_date():
    dt = str(date.today()).replace("-","")
    return dt


'''
Make API Calls Like a PRO - Python API Client x Shopify
--------------------------------------------------------
https://www.youtube.com/watch?v=E39a7kQfjSg

'''

def create_session():
    s = requests.Session()
    return s

def main():
    url = r"https://desktime.com/api/v2/json/employee?apiKey=ce473fa55599509ec8251b4841b7fbcf&id=489426&date="
    sess = create_session()
    print(url+todays_date())
    resp = sess.get(url+todays_date())
    # https://desktime.com/api/v2/json/employee?apiKey=ce473fa55599509ec8251b4841b7fbcf&id=489426&date=20230802
    print(resp)

if __name__ == "__main__":
    main()
