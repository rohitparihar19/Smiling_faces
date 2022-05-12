import cv2
import numpy as np
import dlib
from time import time
from tkinter import *
import tkinter as tk
from tkinter import Message, Text
import os
import shutil
import csv
from PIL import Image, ImageTk
import pandas as pd
import datetime
from time import time
import tkinter.ttk as ttk
import tkinter.font as font
from pathlib import Path
from PIL import ImageTk, Image

window = tk.Tk()
bgimg= ImageTk.PhotoImage(file = "P1Nzdt.jpg")
limg= Label(window, i=bgimg)
limg.pack()
window.title("Smile_Recogniser")
window.configure(background ='light grey')
window.grid_rowconfigure(0, weight = 1)
window.grid_columnconfigure(0, weight = 1)
message = tk.Label(
    window, text ="SMILE RECOGNITION SYSTEM",
    bg ="light blue", fg = "grey", width = 40,
    height = 3, font = ('Bauhaus 93', 30, 'bold'))

message.place(x = 300, y = 20)

message = tk.Label(
    window, text ="To stop the Feed please press 'q'",
    bg ="blue", fg = "white", width = 30,
    height = 3, font = ('time', 15, 'bold'))

message.place(x = 550, y = 500)

def smile(landmark):
        lips_width = abs(landmark.parts()[49].x - landmark.parts()[55].x)

        # Calculate jaw width
        jaw_width = abs(landmark.parts()[3].x - landmark.parts()[15].x)

        # Calculate the ratio of lips and jaw widths
        ratio = lips_width / jaw_width
        print(ratio)

        if ratio > 0.28:
            result = "Smile"
        else:
            result = "No Smile"
        return result

def Takevideo():
    cap = cv2.VideoCapture(0)

    detector = dlib.get_frontal_face_detector()

    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    while True:
        start_time = time()
        _ ,frame = cap.read()
        gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

        faces = detector(gray)
        for face in faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()
            # cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0),3)

            landmark = predictor(gray, face)
            
            for n in range(48,68):
                x = landmark.part(n).x
                y = landmark.part(n).y
                cv2.circle(frame,(x,y),3,(255,0,0),-1)

            result = smile(landmark)

            cv2.putText(frame, result, (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)


        cv2.imshow("Frame",frame)
        end_time = time()
        fps = 1/np.round(end_time - start_time, 3)
        cv2.putText(frame, f"FPS:{fps}", (50, 0), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        print(f"Frames Per Second : {fps}")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 

takevideo = tk.Button(window, text ="START",
command = Takevideo, fg ="grey", bg ="light green",
width = 10, height = 2, activebackground = "Red",
font =('Bauhaus 93', 20, ' bold '))
takevideo.place(x = 650, y = 400)

window.mainloop()    
