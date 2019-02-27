import tkinter as tk
from tkinter import *
import main as mn
from tkinter import filedialog as fd
from pathlib import Path
import sys		
	
def helloCallBack():
	filename = fd.askopenfilename(title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
	if filename!='':
		keywords=mn.main(filename)
		keywords_string=''
		keywords_string='\n'
		keywords_string=keywords_string.join(keywords)
		keywords_string+='\n*************************************************\n'
		T.insert(END, keywords_string)

root = tk.Tk()
S=tk.Scrollbar(root)
T = tk.Text(root, height=20, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
# Code to add widgets will go here...
file_button=tk.Button(root, text ="Select File",width=10, command = helloCallBack)
file_button.pack()

#filename = fd.askopenfilename(title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
#if filename!='':
#	B = Tkinter.Button(bottom, text ="Get Keywords", command = helloCallBack)
root.mainloop()
