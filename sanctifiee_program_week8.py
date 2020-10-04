# Sanctifiee Musafiri 
# CIS 245-A345
# 10/4/2020
# Assignment 8.1 

import os #import the OS library

def makePath(filePath):
	if not os.path.exists(filePath):
		os.makedirs(filePath)

def getName():
	name = input("Enter your name: ")
	return name

def getAddress():
	address = input("Enter your address: ")
	return address

def getPhoneNumber():
	phoneNumber = input("Enter your phone number: ")
	return phoneNumber

def writeToFile(completePath,name,address,phoneNumber):
	with open(completePath, 'w') as fileHandle: #open file for writing at the path
		fileHandle.write(name+", "+address+", "+phoneNumber) #write data to file

def readFromFile(completePath):
	with open(completePath, 'r') as fileHandle: #open same file for reading at the same path
		info = fileHandle.read() #read data from the file
		print("\n\n The content of the file is \n")
		print(info)

def main():
	print ("Welcome to Sanctifiee’s program for directories and files management! ")
	filePath = input ("Enter the directory path where to save files: ")
	fileName = input ("Enter the name of the file you want to save: ")
	makePath(filePath)
	completePath = filePath+fileName
	name = getName()
	address = getAddress()
	phoneNumber = getPhoneNumber()
	writeToFile(completePath,name,address,phoneNumber)
	readFromFile(completePath)


main()