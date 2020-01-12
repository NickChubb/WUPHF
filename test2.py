from fbchat import Client
from fbchat.models import *
import wuphf as w

email = "ryanstartedthefire69@gmail.com"
password = "1Agas3rs"
name = "jordan"
msg = "HIHIHIHIHIHIHI"

#w.sendMsg(email, password, name, msg)

class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))

        # If you're not the author, echo
        if author_id != self.uid:
            self.send(message_object, thread_id=thread_id, thread_type=thread_type)


client = EchoBot(email, password)
client.listen()