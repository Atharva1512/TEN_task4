from tkinter import *
from datetime import * 
import time
from tkinter import messagebox
import os,winsound

root=Tk()

root.geometry("400x600")
root.title("Alarm Clock")
root.configure(background="black")
root.resizable(0,0)

hr=IntVar()
mn=IntVar()
sc=IntVar()

def start():
    current_dt=datetime.now()
    cur_day=current_dt.strftime("%d,%B %Y")
    cur_time=current_dt.strftime("%H:%M:%S")
    tz=time.strftime("%Z")
    label1.config(text=cur_day)
    label2.config(text=cur_time)
    label2.after(200,start)
    label3.config(text=tz)

def message():
    alarm_time=alr.get()
    messagebox.showinfo("Alarm Clock",f"The Alarm Time is : {alarm_time}")

def set_alarm():
    alarm_time=alr.get()
    current_dt=datetime.now()
    cur_time=current_dt.strftime("%H:%M:%S")
    print(alarm_time)
    message()
    while(alarm_time != cur_time):
        current_dt=datetime.now()
        cur_time=current_dt.strftime("%H:%M:%S")
        label2.config(text=cur_time)
        label2.after(200)
        time.sleep(1)
    if alarm_time==cur_time:
        print("ALARM work Succesfully!!!")
        winsound.PlaySound("*",winsound.SND_ASYNC)
        alarm_status.config(text="Clock Alarmed Successfully!!")



label1=Label(root,text="",bg="black",font=("bold",25),fg="white",bd=40)
label1.grid(row=0,column=1)

label2=Label(root,font=("ds-digital",50,"bold"),bg="black",fg="Green",bd=50,text="")
label2.grid(row=1,column=1)

label3=Label(root,text="",bg="black",fg="White")
label3.grid(row=2,column=1)

alr_label=Label(root,text="Set Alarm Time: ",anchor="w")
alr_label.grid(row=3,column=1,pady=10)

alr=Entry(root)
alr.grid(row=4,column=1,pady=10)

but=Button(root,text="SET",command=set_alarm)
but.grid(row=5,column=1,pady=10)

alarm_status=Label(root,text="",bg="black",fg="wheat")
alarm_status.grid(row=6,column=1,pady=10)
start()

root.mainloop()