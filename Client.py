<<<<<<< Updated upstream
=======
<<<<<<< HEAD

=======
>>>>>>> 22445102bf0b2d669fd993e20e5d55c6280826cb
>>>>>>> Stashed changes
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
import socket, threading, sys, traceback, os

from RtpPacket import RtpPacket

CACHE_FILE_NAME = "cache-"
CACHE_FILE_EXT = ".jpg"

class Client:
	INIT = 0
	READY = 1
	PLAYING = 2
	state = INIT

	SETUP = 0
	PLAY = 1
	PAUSE = 2
	TEARDOWN = 3

	def __init__(self, master, serveraddr, serverport, rtpport, filename):
		self.master = master
		self.master.protocol("WM_DELETE_WINDOW", self.handler)
		self.createWidgets()
		self.serverAddr = serveraddr
		self.serverPort = int(serverport)
		self.rtpPort = int(rtpport)
		self.fileName = filename
		self.rtspSeq = 0
		self.sessionId = 0
		self.requestSent = -1
		self.teardownAcked = 0
		self.connectToServer()
		self.frameNbr = 0

	# Initiation
	# THIS GUI IS JUST FOR REFERENCE ONLY, STUDENTS HAVE TO CREATE THEIR OWN GUI
	def createWidgets(self):
		"""Build GUI."""
		# Create Setup button
		self.setup = Button(self.master, width=20, padx=3, pady=3)
		self.setup["text"] = "Setup"
		self.setup["command"] = self.setupMovie
		self.setup.grid(row=1, column=0, padx=2, pady=2)

		# Create Play button
		self.start = Button(self.master, width=20, padx=3, pady=3)
		self.start["text"] = "Play"
		self.start["command"] = self.playMovie
		self.start.grid(row=1, column=1, padx=2, pady=2)

		# Create Pause button
		self.pause = Button(self.master, width=20, padx=3, pady=3)
		self.pause["text"] = "Pause"
		self.pause["command"] = self.pauseMovie
		self.pause.grid(row=1, column=2, padx=2, pady=2)

		# Create Teardown button
		self.teardown = Button(self.master, width=20, padx=3, pady=3)
		self.teardown["text"] = "Teardown"
		self.teardown["command"] =  self.exitClient
		self.teardown.grid(row=1, column=3, padx=2, pady=2)

		# Create a label to display the movie
		self.label = Label(self.master, height=19)
<<<<<<< Updated upstream
		self.label.grid(row=0, column=0, columnspan=4, sticky=W+E+N+S, padx=5, pady=5)

#PART1#
#########################################################################################################################################
	def setupMovie(self):
		"""Setup button handler."""
	#TODO

=======
<<<<<<< HEAD
		self.label.grid(row=0, column=0, columnspan=4, sticky=W+E+N+S, padx=5, pady=5) 
	
	#1#
	def setupMovie(self):
		"""Setup button handler."""
	#TODO
	
	#2#
=======
		self.label.grid(row=0, column=0, columnspan=4, sticky=W+E+N+S, padx=5, pady=5)

	def setupMovie(self):
		"""Setup button handler."""
	#TODO

>>>>>>> 22445102bf0b2d669fd993e20e5d55c6280826cb
>>>>>>> Stashed changes
	def exitClient(self):
		"""Teardown button handler."""
	#TODO
    
	#3#
	def pauseMovie(self):
		"""Pause button handler."""
	#TODO
<<<<<<< Updated upstream

	def playMovie(self):
		"""Play button handler."""
	#TODO


   #PART 2
	#########################################################################################################################################

	def listenRtp(self):
		"""Listen for RTP packets."""
		#TODO

	def writeFrame(self, data):
		"""Write the received frame to a temp image file. Return the image file."""
	#TODO

	def updateMovie(self, imageFile):
		"""Update the image file as video frame in the GUI."""
	#TODO


	def connectToServer(self):
		"""Connect to the Server. Start a new RTSP/TCP session."""
	#TODO

#PART 3
#################################################################################################################################################

=======
<<<<<<< HEAD
	
	#4#
	def playMovie(self):
		"""Play button handler."""
	#TODO
	
	#5#
	def listenRtp(self):		
		"""Listen for RTP packets."""
		#TODO

	#6#				
	def writeFrame(self, data):
		"""Write the received frame to a temp image file. Return the image file."""
	#TODO
	
	#7#
	def updateMovie(self, imageFile):
		"""Update the image file as video frame in the GUI."""
	#TODO
	
	#8#
	def connectToServer(self):
		"""Connect to the Server. Start a new RTSP/TCP session."""
	#TODO
	
	#9#
=======

	def playMovie(self):
		"""Play button handler."""
	#TODO

	def listenRtp(self):
		"""Listen for RTP packets."""
		#TODO

	def writeFrame(self, data):
		"""Write the received frame to a temp image file. Return the image file."""
	#TODO

	def updateMovie(self, imageFile):
		"""Update the image file as video frame in the GUI."""
	#TODO

	def connectToServer(self):
		"""Connect to the Server. Start a new RTSP/TCP session."""
	#TODO

>>>>>>> 22445102bf0b2d669fd993e20e5d55c6280826cb
>>>>>>> Stashed changes
	def sendRtspRequest(self, requestCode):
		"""Send RTSP request to the server."""
		#-------------
		# TO COMPLETE
		#-------------
<<<<<<< Updated upstream



	def recvRtspReply(self):
		"""Receive RTSP reply from the server."""
		#TODO

	def parseRtspReply(self, data):
		"""Parse the RTSP reply from the server."""
		#TODO

=======
<<<<<<< HEAD
		
	
	#10#
	def recvRtspReply(self):
		"""Receive RTSP reply from the server."""
		#TODO
	
	#11#
	def parseRtspReply(self, data):
		"""Parse the RTSP reply from the server."""
		#TODO
	
	#12#
=======



	def recvRtspReply(self):
		"""Receive RTSP reply from the server."""
		#TODO

	def parseRtspReply(self, data):
		"""Parse the RTSP reply from the server."""
		#TODO

>>>>>>> 22445102bf0b2d669fd993e20e5d55c6280826cb
>>>>>>> Stashed changes
	def openRtpPort(self):
		"""Open RTP socket binded to a specified port."""
		#-------------
		# TO COMPLETE
		#-------------
		# Create a new datagram socket to receive RTP packets from the server
		# self.rtpSocket = ...

		# Set the timeout value of the socket to 0.5sec
		# ...
<<<<<<< Updated upstream
=======
<<<<<<< HEAD
		
    #13#
=======
>>>>>>> Stashed changes


>>>>>>> 22445102bf0b2d669fd993e20e5d55c6280826cb
	def handler(self):
		"""Handler on explicitly closing the GUI window."""
		#TODO
