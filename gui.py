import tkinter as tk
from tkinter import *
import rake as rake
from tkinter import filedialog as fd
from pathlib import Path
import sys		
	
def helloCallBack():
	filename = fd.askopenfilename(title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
	if filename.split(".")[-1]=='txt':
		if filename!='':
			keywords=rake.rake(filename)
			#keywords_string=''
			keywords_string='\n'
			keywords_string=keywords_string.join(keywords)
			keywords_string+='\n*************************************************\n'
			T.insert(END, keywords_string)
	else:
		keywords_string="Invalid File"
		keywords_string+='\n*************************************************\n'
		T.insert(END, keywords_string)

root = tk.Tk()
S=tk.Scrollbar(root)
T = tk.Text(root, height=20, width=50)
S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
file_button=tk.Button(root, text ="Select File",width=10, command = helloCallBack)
file_button.pack()
root.mainloop()
