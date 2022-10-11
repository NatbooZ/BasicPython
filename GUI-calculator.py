#GUI-Calculator.py

from  tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('โปรแกรมคำนวณราคาปลา รถขายมั่ว')
GUI.geometry('700x600')  #กำหนดขนาดของตัวโปรแกรม

bg = PhotoImage(file='ice-cream-icon.png')

BG = Label(GUI,image=bg)
BG.pack()

L = Label(GUI,text='กรุณากรอกจำนวนปลา (kg)',font=(None,20)) #none คือชื่อตัวอักษร font,20 คือขนาด
L.pack()

v_quantity = StringVar() # ตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_quantity, font = (None,20)) 
E1.pack()



def Cal():
	try:  #try ลองทำคำสั่งถ้าใช่จบโปรแกรม ถ้าไม่ใช่ไปที่ except เพื่อป้องกันการกรอกผิด
		quan = float(v_quantity.get())
		calc = quan * 39               #คิดราคากิโลละ 39 บาทต่อกิโล *จำนวนปลา
		messagebox.showinfo('ราคาทั้งหมด','ราคาปลาทั้งหมด {} บาท'.format(calc))
		v_quantity.set('1') #ค่า default หลังจากคำนวณเสร็จ
		E1.focus() #หลังจากจบการคำนวณแล้วจะกลับไปที่ E1

	except:
		messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
		v_quantity.set('1') #ค่า default หลังจากคำนวณเสร็จ
		E1.focus()


B = ttk.Button(GUI,text='คำนวณ',command=Cal)
B.pack(ipadx=30,ipady=20) #ipadx ขยายกว้าง x/y


GUI.mainloop()  #เพื่อให้โปรแกรมรันตลอดเวลา จะอยู่ท้าย GUI


