import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
	print("connected to server with result code"+str(rc))
	
	client.subscribe("asielgar/ping")
	
	client.message_callback_add("asielgar/ping",on_message_from_ping)

def on_message(client, userdata, msg):
	print("default callback - topic: " +msg.topic +"  msg: "+str(msg.payload, "utf-8"))

def on_message_from_ping(client, userdata, message):
	
	number = int(message.payload)
	time.sleep(1)
	print("custom callback - pong: "+str(number))
	client.publish(message.topic, number+1)
	
if __name__ == '__main__':
	client=mqtt.Client()
	client.on_message = on_message
	client.on_connect=on_connect
	
	client.connect("172.20.10.10", 1883, 60)
	
	client.loop_forever()
