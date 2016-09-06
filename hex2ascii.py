#!/usr/bin/python

#This script converts hex strings to human-readable ASCII format from a file containing a list of hexdata
#Libraries

import binascii
import glob
import sys
import shutil
import time as t

#Variables
'''
opfname - Variable for printing date 
inputFile - Takes from argument the filename of the source file
date = for asining the date values
outputFile - New file object for new file to which the output has to be recorded
f - file contents for iteration
line - one line in file for iteration
ascii_data - the converted date which is to be output to screen & file'''

def banner(): #Function to print the banner
	print """
		  _               ____                _ _  
		 | |__   _____  _|___ \ __ _ ___  ___(_|_)
		 | '_ \ / _ \ \/ / __) / _` / __|/ __| | |
		 | | | |  __/>  < / __/ (_| \__ \ (__| | |
		 |_| |_|\___/_/\_\_____\__,_|___/\___|_|_|
		-------------------------------------------
		  GitHub - ravisankar90 - Version 1.0,2016
		-------------------------------------------"""
	
if len(sys.argv) == 1: #If condition for file not specified
	banner() #Print Banner
	print "This script converts hex strings to human-readable ASCII format from a file containing a list of hexdata"
	print 'Usage: %s [fileName]' % (sys.argv[0])
	exit() #Exits the program
else :
	banner()	
	inputFile = sys.argv[1] #Assigns argument 1(filename) to inputFile
	date = t.localtime(t.time()) #Assigns date to variable date
	opfname = '%d-%d-%d.txt'%(date[2],date[1],date[0]) #Takes day,month,year in DD-MM-YYYY format & assigns to opfname
	outputFile = open('hex2ascii-' + opfname,'w') #Creates newfile with filename "hex2ascii-DD-MM-YYYY.txt"
	with open(inputFile) as f: #Open inputFile as f & loops though lines
		print "\nThe corresponding ascii data are: \n"			
		for line in f: #Iteration begins, takes line in f
			ascii_data = binascii.unhexlify(line.split()[0]) #Takes one line from line and converts it to ASCII
			print ascii_data #Prints the ascii on screen
			outputFile.write(ascii_data + '\n') #Writes the ascii to the file
	print "\nThe output has been saved to hex2ascii-"+ opfname #Displays the filename to which output has been saved



