import shelve,os
import tkinter as tk

import os
import shelve

def get_shelve_path():
    appdata_path = os.path.join(os.getenv("APPDATA"), "ToDo")
    os.makedirs(appdata_path, exist_ok=True)
    shelve_path = os.path.join(appdata_path, "todo_data")
    
    return shelve_path


def newlist(text):
    with shelve.open(get_shelve_path()) as file:
        lfile=file["lis"]
        lfile.append(text.capitalize())
        file["lis"]=lfile
        

                
                
def action():
    
    with shelve.open(get_shelve_path()) as file:
        if len(file)==0:
            file["lis"]=[]
        else:
            disptext=f'{"Your ToDo List":^40}'
            displabel.config(text=disptext)
            lfile=file["lis"]
            listtext=""
            idx=1    
            for f in lfile:
                listtext+=f"{idx}. {f}\n"
                idx+=1
            listlabel.config(text=listtext)
            
def inputop(event):       
    opt=inputbox.get()
    inputbox.delete(0,tk.END)
    if opt.isdigit():
        delete(opt)
    elif len(opt) > 2:
        newlist(opt)
        
    action()

def delete(opt):
    with shelve.open(get_shelve_path()) as file:
        lfile=file["lis"]
        if int(opt) <= len(lfile):
            lfile.pop(int(opt)-1)
            file["lis"]=lfile
    


window=tk.Tk()
window.config(padx=20,pady=20)
window.title("ToDo List")

displabel=tk.Label(text="")
displabel.grid(row=0,column=1)

listlabel=tk.Label(text="")
listlabel.grid(row=1,column=0,columnspan=3,sticky='w')

inputbox=tk.Entry()
inputbox.grid(row=2,column=0,columnspan=3,sticky='ew')
window.bind('<Return>',inputop)

action()

window.mainloop()
     
