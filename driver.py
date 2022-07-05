from tkinter import *
from tkinter import filedialog
import time
import cv2
import os
import sys

import tkinter as Tk
pathhhhhh=os.path.dirname(__file__)+"\\logic.py"
def browse_file():

    fname = filedialog.askopenfilename(filetypes=(
        ("jpg", "*.jpg"), ("All files", "*")))
    cmm="python "+pathhhhhh+" -i "   # adhaa commm

    cmmd=cmm+fname
    # print(cmmd)   debuggin urposes obnly
    os.system(cmmd)

def browse_cam():
    cap= cv2.VideoCapture(0)
    ret, frame = cap.read()

    while(True):
    
        ret, frame = cap.read()
        cv2.imshow('lol',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite('frame.jpg',frame)
            break
    
 
    cap.release()
    cv2.destroyAllWindows()
    cmmf="python "+pathhhhhh+" -i frame.jpg"
    
    os.system(cmmf)
root = Tk.Tk()
root.wm_geometry("350x160")
root.wm_title(" 20DCS0xx | Python Mini Project")
frame1 = Tk.Frame(root, width=400, height=350)
frame1.pack()
broButton = Tk.Button(master=frame1, text='Browse', width=10, command=browse_file)
broButton.pack(side=Tk.LEFT, padx=2, pady=2)
liveFromButton = Tk.Button(master=frame1, text='liveFromCam', width=10, command=browse_cam)
liveFromButton.pack(side=Tk.BOTTOM, padx=2, pady=10)
livelabel = Tk.Label(master=frame1, text='Press q to capture the video snap', width=100)
livelabel.place(relx = 0.5,
                   rely = 0.5,
                   anchor = 'center')
livelabel.pack(side=Tk.BOTTOM, padx=2, pady=15)
std = Tk.Label(master=frame1, text='Press esc to exit image window', width=100)
std.pack(side=Tk.BOTTOM, padx=2, pady=25)
Tk.mainloop()