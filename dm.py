from network import network
import threading


sock = network()
sock.start_server(input('How many players?'))

while True:
	