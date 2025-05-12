import cv2
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import customtkinter
from PIL import Image

def karakterden_ikili(karakter):#karakterin ikili halinin tersini verir.Bu veriyi okurken işi kolaylaştırıyor
    asci_kod=ord(karakter)#karakterin ascii kodunu alma
    binary=""
    sayac=0
    while sayac!=8:#Her karakter için 8 bit ayırma
        binary+=str(asci_kod%2)
        asci_kod=int(asci_kod/2)
        sayac+=1
    return binary

def button2():
    global dosya_yolu#veri yazarken alacğım dosya uzantısı için bu değişkeni kullandım
    dosya_yolu = filedialog.askopenfilename()
    if dosya_yolu!="":
        messagebox.showinfo("Bilgilendirme","Şifrelencek resim alındı.")
        resim = customtkinter.CTkImage(
            light_image=Image.open(f"{dosya_yolu}"),size=(500,300))
        img_lbl=customtkinter.CTkLabel(tk,image=resim,text="").place(x=720,y=100)
    else:
        messagebox.showinfo("Bilgilendirme","Şifrelencek resim alınmadı.")

def button():
    #try:#eğer dosya uzantısı boşsa hata vermemesi için hata ayıklama
        resim=cv2.imread(f"{dosya_yolu}")
        (y,x)=resim.shape[:2]
        metin=metin2.get()#entry alanından gelen veriyi atama
        if metin=="":
            messagebox.showinfo("Bilgilendirme","Şifrelencek metin alınmadı.")
            return
        metin+=":" #veriyi okurken durma işaretim
        binary=""
        sayac=0
        pixel_varMi=False
        for i in metin:#resmin içine gizlencek binary kodun tamamı
            binary+=karakterden_ikili(i)
        for i in range(y):
            for j in range(x):
                pixel_deger=resim[i,j]
                for k in range(3):
                    if binary[sayac]=='0':
                        if pixel_deger[sayac%3]%2!=0:
                            if pixel_deger[sayac%3]!=255:
                                pixel_deger[sayac%3]+=1
                            else:
                                pixel_deger[sayac%3]-=1
                    elif binary[sayac]=='1':
                        if pixel_deger[sayac%3]%2!=1:
                            pixel_deger[sayac%3]+=1
                    sayac+=1
                    if sayac>=len(binary):
                        pixel_varMi=True
                        break
                if sayac>=len(binary):
                    pixel_varMi=True
                    break
            if sayac>=len(binary):
                pixel_varMi=True
                break
        cv2.imwrite(f"{dosya_yolu}-sifreli.png",resim)
        if pixel_varMi==False:
            messagebox.showinfo("Bilgilendirme","Şifrelencek resimde yetersiz yer var, metin eksik şifrelendi")
        else:
            messagebox.showinfo("Bilgilendirme","Metin resmin içerisine gizlendi.")
            messagebox.showinfo("Bilgilendirme","Şifrelenen karakter sayısı : " + str((len(binary)/8-1)))
    #except:
     #   messagebox.showinfo("Bilgilendirme","Şifrelencek resim alınmadı.")
        
tk=customtkinter.CTk()
tk.title("Steganografi Veri Yazma")
tk.geometry("1250x460")

customtkinter.CTkLabel(tk,text="Veri Yazma",font=("Verdana",28)).pack()
lbl=customtkinter.CTkLabel(tk,text="Şifrelencek metin : ",font=("Verdana",24))
lbl.place(x=10,y=120)
metin2=customtkinter.CTkEntry(tk,width=450)
metin2.place(x=250,y=124)
btn=customtkinter.CTkButton(master=tk,text="Resim yükle",height=50,width=120,corner_radius=10,command=button2)
btn.place(x=180,y=220)
btn=customtkinter.CTkButton(master=tk,text="Veri yaz",height=50,width=120,corner_radius=10,command=button)
btn.place(x=380,y=220)

tk.mainloop()




