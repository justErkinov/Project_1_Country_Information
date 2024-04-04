"""
b=input("tosh qaychi yoki qogʻoz bittasini  kiriting: ")
b.lower()
c={"Tosh","Qaychi","Qogʻoz"}
d=list(c)
if b=="tosh":
 h=d[1:2]
 print(h)
 if h==b:
  print("Durrang: ")
 if h==b:
  print("Tabriklayman siz yutdingiz: ")
 if h==b:
  print("Afsuski yutqazdingiz: ") 
if b=="qaychi":
 h=d[1:2]
 print(h)
 if h==b:
  print("Afsuski yutqazdingiz: ")
 if h==b:
  print("Durrang")
 if h==b:
  print("Tabriklaymiz siz yutdingiz: ")
if b=="qogoz":
 h=d[1:2]
 print(h)
 if h==b:
  print("Tabriklayman siz yutdingiz: ")
 if h==b:
  print("Afsuski yutqazdingiz: ")
 if h==b:
  print("Durrang")
else:
 d=input("Siz bilan justErkinov bo'ldi: ")
 
 """



from tkinter import *
from tkinter import PhotoImage
import random

oyna=Tk()
oyna["bg"]="white"

main={"QAYCHI":"/storage/emulated/0/Pictures/Eraser/1708244357310.png","QUDUQ":"/storage/emulated/0/Pictures/Eraser/1708241222335.png","QOG'OZ":"/storage/emulated/0/Pictures/Eraser/1708248979909.png"}

bot_rasmi=PhotoImage(file="/storage/emulated/0/Pictures/4712126.png")

bot_maydoni=Label(image=bot_rasmi,
bg="gold",
width=1000,
height=700)

info=Label(text="",
font="TkCaptionFont",
bg="white")

user_rasmi=PhotoImage(file="/storage/emulated/0/Pictures/Eraser/1708241960814.png")

user_maydoni=Label(image=user_rasmi,
bg="skyblue",
width=1000)

bot_maydoni.pack()
info.pack()
user_maydoni.pack()

def user_tanlov(text):
 yangi_rasm=PhotoImage(file=main[text],height=500)
 user_maydoni.configure(image=yangi_rasm)
 user_maydoni.image=yangi_rasm
 
 bot_random=random.choice(list(main.keys()))
 bot_yangi_rasmi=PhotoImage(file=main[bot_random])
 bot_maydoni.configure(image=bot_yangi_rasmi)
 bot_maydoni.image=bot_yangi_rasmi
 
 if bot_random=="QAYCHI" and text=="QUDUQ":
  info["text"]="SIZ YUTDINGIZ"
 elif bot_random=="QAYCHI" and text=="QOG'OZ":
  info["text"]=="SIZ YUTQAZDINGIZ"
 elif bot_random=="QUDUQ" and text=="QAYCHI":
  info["text"]="SIZ YUTQAZDINGIZ"
 elif bot_random=="QUDUQ" and text=="QOG'OZ":
  info["text"]="SIZ YUTDINGIZ"
 elif bot_random=="QOG'OZ" and text=="QAYCHI":
  info["text"]="SIZ YUTDINGIZ"
 elif bot_random=="QOG'OZ" and text=="QUDUQ":
  info["text"]="SIZ YUTQAZDINGIZ"
 else:
  info["text"]="DURRANG"
 
 
for tugma in ["QAYCHI","QUDUQ","QOG'OZ"]:
 tugma=Button(text=tugma,
 bg="white",
 font="TkCaptionFont",
 command=lambda text=tugma: user_tanlov(text)).pack()

oyna.mainloop()