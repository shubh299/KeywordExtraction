
def text_from_txt(file_path):
    f=open(file_path, "r")
    if f.mode=='r':
        return f.read()