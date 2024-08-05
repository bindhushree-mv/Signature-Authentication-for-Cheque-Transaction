from tkinter import filedialog
from tkinter.filedialog import askopenfile
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import cv2
#import matplotlib as plt
from PIL import Image, ImageTk


window= tk.Tk()
window.geometry("940x700+300+50")  # Size of the window 
window.resizable(False, False)
window.configure(bg='lightblue')
window.title('Signature verification')


lbltitle = Label(window, bd=0, relief=GROOVE, text="Signature Authentication For Cheque", fg="DeepSkyBlue4", bg="white", font=("times new roman", 30, "bold"))
lbltitle.pack(side=TOP, fill=BOTH, padx=20, pady=10)

frame = Frame(window, width=899, height=600, bg="alice blue")
frame.place(x=20, y=80)

udtitle = Label(window, bd=0, text="Upload Your Document Here...", fg="DeepSkyBlue3", bg="white", font=("times new roman", 20, "bold"))
udtitle.pack(side=TOP, fill=BOTH, padx=20, pady=10)

def upload_file():
    global img,filename1
    f_types = [('Jpg Files', '.jpg'),('PNG Files','.png')]   # type of files to select 
    filename1 = filedialog.askopenfilename(filetypes=f_types)
    
    img=Image.open(filename1) # read the image file
    img=img.resize((200,200)) # new width & height
    img=ImageTk.PhotoImage(img)
    e1 =tk.Label(frame)
    e1.place(x=50, y=90)
    e1.image = img # keep a reference! by attaching it to a widget attribute
    e1['image']=img
    
def upload_original_file():
    global img2,filename2
    f_types = [('Jpg Files', '.jpg'),('PNG Files','.png')]   # type of files to select 
    filename2 = filedialog.askopenfilename(filetypes=f_types)
    
    img2=Image.open(filename2) # read the image file
    img2=img2.resize((200,200)) # new width & height
    img2=ImageTk.PhotoImage(img2)
    e2 =tk.Label(frame)
    e2.place(x=640, y=90)
    e2.image = img2# keep a reference! by attaching it to a widget attribute
    e2['image']=img2
    
    
def check(image1,image2):
   gray_img1 = cv2.imread(image1, cv2.IMREAD_GRAYSCALE)

   gray_img2 = cv2.imread(image2, cv2.IMREAD_GRAYSCALE)
   detect = cv2.ORB_create()
   key_point1,descrip1 = detect.detectAndCompute(gray_img1,None)
   key_point2,descrip2 = detect.detectAndCompute(gray_img2,None)
   brute_force = cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
   no_of_matches = brute_force.match(descrip1,descrip2)
   no_of_matches = sorted(no_of_matches,key=lambda x:x.distance)
   distances = [m.distance for m in no_of_matches]
    
   distance = sum(distances) / len(distances)
   print(distance)
   diff=1/(1+distance)
   
   print(diff)
    
   if distance<=40 and distance!=0:  
    messagebox.showinfo("Authentic signature", f'Authentic signature Match percentage: {(1-diff)*100}')
   elif distance==0:  
    messagebox.showinfo("Authentic signature", f'Authentic signature Match percentage: {(diff)*100}')
   else:
    messagebox.showinfo("Forged signature", f'Forged signature Unmatch percentage: {(1-diff)*100}')
   
   
      




l1 = tk.Label(window,text='Upload Original Document',height=3,width=21,bg="alice blue",font=("times new roman", 14, "bold"))  
l1.place(x=50, y=400)

b1 = tk.Button(frame, text='Upload File',bg="midnightblue",fg="white",
   width=10,font=("times new roman", 14, "bold"),command = lambda:upload_file())
b1.place(x=70, y=420)
 
l2 = tk.Label(window,text='Upload Reference Signature',height=3,width=22,bg="alice blue",font=("times new roman", 14, "bold"))  
l2.place(x=644, y=400)
b2 = tk.Button(frame, text='Upload File',bg="midnightblue",fg="white", 
   width=10,font=("times new roman", 14, "bold"),command = lambda:upload_original_file())
b2.place(x=710,y=420) 
b3 = tk.Button(frame, text='Check authentication',height=1, 
   width=20,bg="brown",fg="white",font=("times new roman", 14, "bold"),command=lambda:check(filename1,filename2))
b3.place(x=342,y=500) 

window.mainloop()