from fbchat import Client
from fbchat.models import *

def sendMsg(email, password, name, msg):

	client = Client(email, password)

	if not client.isLoggedIn():
		print("Client not logged in.")

	users = client.searchForUsers(str(name))
	user = users[0]

	#print(user)

	client.send(Message(str(msg)), user.uid, thread_type=ThreadType.USER)

	client.logout()

def sendSmS(email, password, phone, msg, sender)
