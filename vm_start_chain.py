import paho.mqtt.client as mqtt
import time
import socket

def on_connect(client, userdata, flags, rc):
	print("connected to server with result code"+str(rc))

if __name__ == '__main__':
	ip_address = socket.gethostbyname(socket.gethostname())
	client = mqtt.Client("asielgar")
	
	client.on_connect = on_connect
	
	client.connect("172.20.10.10", 1883, 60)
	
	client.loop_start()
	time.sleep(1)
	
	while True:
		number = int(input("Enter start number: "))
		client.publish("asielgar/ping", number)
		print("publishing ping")
		time.sleep(4)
