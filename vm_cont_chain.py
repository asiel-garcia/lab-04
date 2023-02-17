import paho.mqtt.client as mqtt

def on_connect(clients, userdata, flags, rc):
	print("connected to server with result code"+str(rc))
	
	client.subscribe("asielgar/ping")
	
	client.message_callback_add("user/ping",on_message_from_ping)

def on_message(client, userdata, msg):
	print("default callback - topic: " +msg.topic +"  msg: "+str(msg.payload, "utf-8"))
	
def on_message_from_ping(client, userdata, message):
	sentmsg = int(message.payload.decode())
	newmsg = sentmsg+1
	print("custom callback - pong: "+newmsg)
	
if __name__ == '__main__':
	client=mqtt.Client()
	client.on_connect=on_connect
	
	client.connect("pi@172.20.10.10", 1001, 60)
	
	client.loop_forever()
