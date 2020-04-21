import socket

class network:
	connections = []

	def start_server(self, num_players):
		s = socket.socket()
		s.bind(('', 12345))  
		s.listen(5) 
		while True: 
			if len(self.connections) == num_players:
				return
			# Establish connection with client. 
			c, addr = s.accept()      
			print('Got connection from', addr)

			# send a thank you message to the client.  
			c.send('Thank you for connecting'.encode()) 
			self.connections.append(c)

	def connect_to_server(self):
		s = socket.socket()
		# connect to the server on local computer 
		s.connect(('127.0.0.1', 12345)) 
		  
		# receive data from the server 
		print(s.recv(1024))
		# close the connection 
		s.close()  