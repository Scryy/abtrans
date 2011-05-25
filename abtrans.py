#!/usr/bin/python3
"""
English to Al Bhed / Al Bhed to English translator. This was just for lulz, as I was incredibly bored one afternoon.
"""
from tkinter import *
from tkinter.filedialog import askopenfilename

english	 = b'abcdefghijklmnopqrstuvwxyz'
alBhed	 = b'ypltavkrezgmshubxncdijfqow'

def trans(message, inLang, outLang):
	transMeth = bytes.maketrans(inLang, outLang)
	print("Translation:\n" + message.translate(transMeth))

def srcFile():
	root = Tk()
	fName = askopenfilename()
	root.withdraw()
	rootFile = open(fName).read()
	root.destroy()
	return rootFile

def srcMsg():
	print("Enter what you need translated here: ")
	prompt = input("Text: ")
	return prompt



transOpts = {'1':'English to Al Bhed', '2':'Al Bhed to English'}
transSrc = {'1':'File Source', '2':'Prompt'}

print("Al Bhed translator\n\n")

for key in transOpts:
	print(key, transOpts[key])

while True:
	selection = input(">")
	
	#Just so that confusion is avoided the statemetns within this 
	#if block are relevent to English to Al Bhed
	
	if selection == '1': 
		for key in transSrc:
			print(key, transSrc[key])

		source = input(">")

		if source == '1':
			rootFile = srcFile()
			trans(rootFile, english, alBhed)
			
			break
		if source == '2':
			prompt = srcMsg()
			trans(prompt, english, alBhed)
			break
	
	#And these statements are relevant to Al Bhed to English
	
	if selection == '2':
		for key in transSrc:
			print(key, transSrc[key])

		source = input(">")

		if source == '1':
			rootFile = srcFile()
			trans(rootFile, alBhed, english)
			break
		if source == '2':
			prompt = srcMsg()
			trans(prompt, alBhed, english)
			break			
