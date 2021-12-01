from os import times

import cv2
import numpy as np
from pyzbar.pyzbar import decode
from PIL import Image
import cv2
import time
import csv
import streamlit as st
import pandas as pd

present_students = set()

video = cv2.VideoCapture(0)

st.image('hero.png')
st.title('Attandance system')
st.subheader("Intructions for Usage :")
st.markdown("""
#### 1. Get Your QR Code.
#### 2. Click on Record button & scan the QR Code.
#### 3. Get your Attandance Recorded.
---""")

students =[]

sidebar = st.sidebar

sidebar.title('Present student list')


# for stu in present_students


with open('Book1.csv','r') as file:
    reader=csv.reader(file)
    for row in reader:
        students.append((row[1]))

print(f's : {students}')

run = st.checkbox('Record Your Attandance')
if run:
    while True:
        check,frame= video.read()
        d=decode(frame) 
        try:
            for obj in d:
                name=d[0].data.decode()
                name=name.strip()
                print(students)
                if name in students:
                    students.remove(name)
                    present_students.add(name)
                    
                    print('deleted.....')
                    st.subheader(f'Welcome {name}!')
                    st.success('Your Attandance has been recorded!')
                    st.subheader('Press Q to Quit Camera')
                    break

        except Exception as e:
            print(e)
            print('error')
            
        cv2.imshow('Attandance',frame)
        key=cv2.waitKey(1)
        if key==ord('q'):
            print(students)
            break

video.release()
cv2.destroyAllWindows()          

for stu in present_students:
    sidebar.subheader(stu)

showData = st.checkbox("Show Student list")
if showData:
    st.dataframe(pd.read_csv('Book1.csv'))     
     
