from fbchat import Client
from fbchat.models import *
from getpass import getpass


#email = input("Email: ")
#password = getpass()

email = "ryanstartedthefire69@gmail.com"
password = "1Agas3rs"

client = Client(email, password)

if not client.isLoggedIn():
	print("fuck")

name = input("Input the users name: ")
users = client.searchForUsers(name)
user = users[0]

#print(user)

client.send(Message("Test from messenger API"), user.uid, thread_type=ThreadType.USER)



client.logout()