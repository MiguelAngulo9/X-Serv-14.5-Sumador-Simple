#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import socket
import random

# Create a TCP objet socket and bind it to a port
# We bind to 'localhost', therefore only accepts connections from the
# same machine
# Port should be 80, but since it needs root privileges,
# let's use one above 1024

#creamos el socket
#Se lee así: del modulo socket utiliza el metodo socket (socket.socket)
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# Accept connections, read incoming data, and answer back an HTML page
#  (in an infinite loop)

sumando = 0;
try:

	while True:
		print 'Waiting for connections'
		(recvSocket, address) = mySocket.accept()
		print 'HTTP request received:'
		peticion = recvSocket.recv(1024)
		print peticion
		try:
			entero = int(peticion.split()[1][1:])
			
		except KeyError:
			continue
		print entero
		if (sumando == 0):
			sumando = entero;
			respuesta = "Dame otro";
		else:
			resultado = entero + sumando;
			respuesta = "El resultado de la suma es :" + str(entero) + "+" + str(sumando) + "=" + str(resultado);
			sumando = 0;
		
		NUMaleatorio = random.randint(0, 1000000000)
		recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" +
			    "<html><body><h1>Hola! " +
				respuesta + "</p>" + "</h1></body></html>" + "\r\n")
		recvSocket.close()
except KeyboardInterrupt:
	mySocket.close()

