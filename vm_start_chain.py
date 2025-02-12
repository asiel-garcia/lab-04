import paho.mqtt.client as mqtt
import time
import socket

#number = int(input("Enter start number: "))

def on_connect(client, userdata, flags, rc):
	print("connected to server with result code"+str(rc))
	client.subscribe("asielgar/pong")
	client.message_callback_add("asielgar/pong",on_message_from_pong)
	
	#client.publish("asielgar/ping",number)
	

def on_message(client, userdata, msg):
	print("default callback - topic: " +msg.topic +"  msg: "+str(msg.payload, "utf-8"))

def on_message_from_pong(client, userdata, message):
	
	number1 = int(message.payload.decode())+1
	time.sleep(1)
	print("custom callback - ping: "+ f"{number1}")
	client.publish("asielgar/ping", number1)
	
if __name__ == '__main__':
	ip_address = socket.gethostbyname(socket.gethostname())
	client = mqtt.Client()
	
	client.on_connect = on_connect
	
	client.connect("172.20.10.10", 1883, 60)
	
	client.loop_start()
	time.sleep(1)
	
	num = 0
	client.publish("asielgar/ping", num)
	print("publishing ping")
	while True:
		pass
