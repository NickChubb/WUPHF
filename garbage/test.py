import fbchat
from getpass import getpass 
username = str(input("Username: ")) 
client = fbchat.Client(username, getpass()) 
no_of_friends = int(input("Number of friends: ")) 
for i in range(0, no_of_friends): 
	name = str(input("Name: ")) 
	friends = client.fetch_all_users(self) # return a list of names 
	print(friends[0])
	friend = friends[0] 
	msg = str(input("Message: ")) 
	sent = client.send(friend.uid, msg) 
	if sent: 
		print("Message sent successfully!")
