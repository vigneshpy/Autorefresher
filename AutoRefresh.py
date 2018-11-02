from tkinter import *
from tkinter import messagebox


import pyautogui

a1= Tk()
def ref():
      try:
             e=e1.get()
             e=e-1
             r=pyautogui.moveTo(839,397,duration=1)
             r=pyautogui.rightClick(839,397)
             re=pyautogui.moveTo(887,460,duration=0.5)
             re=pyautogui.click(887,460)
             pyautogui.press('f5')
             while(e>0):
                   pyautogui.press('f5')
                   e=e-1
      except:
            messagebox.showerror("Invalid Input", "Enter Only Numbers")
            

e1=IntVar()
a1.title("Auto Refresher")
la=Label(text="Refresh Time ").grid(row=0,column=0)
e=Entry(textvariable=e1).grid(row=0,column=1)
but=Button(text="Start",command=ref).grid(columnspan=3)







