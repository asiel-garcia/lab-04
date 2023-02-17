import paho.mqtt.client as mqtt
import time
import socket

def on_connect(client, userdata, flags, rc):
	print("connected to server with result code"+str(rc))

if __name__ == '__main__':
	ip_address = 0
	ip_address = socket.gethostbyname(socket.gethostname())
	client = mqtt.Client("asielgar")
	
	client.on_connect = on_connect
	
	client.connect("pi", 1001, 60)
	
	client.loop_start()
	time.sleep(1)
	
	while True:
		client.publish("asielgar/ping", 11, f"{ip_address}")
		print("publishing ping")
		time.sleep(4)
