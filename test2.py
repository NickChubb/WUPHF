from fbchat import Client, log
from fbchat.models import *
import wuphf as w

email = "ryanstartedthefire69@gmail.com"
password = "1Agas3rs"
name = "jordan"
msg = "Sup"
phone = "17785499550"
sender = "jordan"
platform = "Facebook"

#w.sendMsg(email, password, name, msg)

w.sendSms(email, password, phone, sender, platform) 