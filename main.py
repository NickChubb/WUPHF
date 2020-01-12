import wuphf as w
import requests as r
import json

url_rows = "https://chubb.api.stdlib.com/get-rows@dev/"
url_data = "http://chubb.api.stdlib.com/get-user-info@dev/?userNum=user"

ROW_DATA = {}

user_data = r.get(url_rows, ROW_DATA)
num_users = json.loads(user_data.text)['count']['count']

users = []
emails = []
passwords = []
phones = []

for i in range(1, num_users+1):
	users.append(r.get(url_data + str(i), ROW_DATA))
	emails.append(json.loads(users[i-1].text)['fb_user']['distinct']['values'])
	passwords.append(json.loads(users[i-1].text)['fb_pass']['distinct']['values'])
	phones.append(json.loads(users[i-1].text)['user_phone']['distinct']['values'])

	w.sendSms(emails[i-1], passwords[i-1], phones[i-1], "Facebook")
