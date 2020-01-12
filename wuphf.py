from fbchat import Client, log
from fbchat.models import *
import requests

def sendMsg(email, password, name, msg):

	client = Client(email, password)

	if not client.isLoggedIn():
		print("Client not logged in.")

	users = client.searchForUsers(str(name))
	user = users[0]

	#print(user)

	client.send(Message(str(msg)), user.uid, thread_type=ThreadType.USER)

	client.logout()

def sendSms(email, password, phone, msg, sender):
	class EchoBot(Client):
	    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
	        self.markAsDelivered(thread_id, message_object.uid)
	        self.markAsRead(thread_id)

	        url = "https://xingluke.api.stdlib.com/hacks@dev/hello-world/"

	        data = {'x': 'x'}

	        requests.post(url, data)
			#requests.post(url, data={"phone": phone, "sender": sender, "sender": sender})
	        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
	        print(type(message_object))
	        print(message_object.text)
	        # If you're not the author, echo
	        if author_id != self.uid:
	            self.send(message_object, thread_id=thread_id, thread_type=thread_type)


	client = EchoBot(email, password)
	client.listen()
