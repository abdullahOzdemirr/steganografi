import cv2
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import customtkinter
from PIL import Image

def button2():
    global dosya_yolu
    dosya_yolu = filedialog.askopenfilename()
    if dosya_yolu!="":
        messagebox.showinfo("Bilgilendirme","Şifrelenmiş resim alındı.")
        resim = customtkinter.CTkImage(
            light_image=Image.open(f"{dosya_yolu}"),size=(500,300))
        img_lbl=customtkinter.CTkLabel(tk,image=resim,text="").place(x=700,y=80)
    else:
        messagebox.showinfo("Bilgilendirme","Şifrelenmiş resim alınmadı.")

def button():
    try:
        resim=cv2.imread(f"{dosya_yolu}")
        (y,x)=resim.shape[:2]
        metin=""
        binary=""
        sayac=0
        sayac2=0
        alt_satir_sayac=0
        for i in range(y):
            for j in range(x):
                pixel_deger=resim[i,j]
                for k in range(3):
                    binary+=str(pixel_deger[sayac2%3]%2)
                    sayac2+=1
                    sayac+=1
                    if sayac==8:
                        alt_satir_sayac+=1
                        y=chr(ikiliden_ascii(binary))
                        if y==":":
                            break
                        metin+=y
                        binary=""
                        sayac=0
                        if alt_satir_sayac==30:
                            metin+="\n"
                            alt_satir_sayac=0
                if y==":":
                    break
            if y==":":
                break
        lbl.configure(text=metin)
    except:
        messagebox.showinfo("Bilgilendirme","Şifrelenmiş resim alınmadı.")

def ikiliden_ascii(binary):
    sayac=0
    asci_kod=0
    for i in binary:
        if i=='1':
            x=1
            if sayac!=0:
                for j in range(sayac):
                    x*=2
            asci_kod+=x
        sayac+=1
    return asci_kod

tk=customtkinter.CTk()
tk.title("Steganografi Veri Okuma")
tk.geometry("1250x460")

customtkinter.CTkLabel(tk,text="Veri Okuma",font=("Verdana",28)).pack()
btn=customtkinter.CTkButton(master=tk,text="Resim seç",height=50,width=120,corner_radius=10,command=button2)
btn.place(x=250,y=100)
btn2=customtkinter.CTkButton(master=tk,text="Veri oku",height=50,width=120,corner_radius=10,command=button)
btn2.place(x=500,y=100)
customtkinter.CTkLabel(tk,text="Şifrelenmiş metin : ",font=("Verdana",24)).place(x=5,y=200)
lbl=customtkinter.CTkLabel(
    tk,text="",fg_color="transparent",
    text_color=("black","red"),
    font=("Verdana",24),
    justify="center")
lbl.place(x=235,y=200)

tk.mainloop()
