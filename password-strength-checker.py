from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Password Strength Checker")
root.configure(bg = 'blue')
root.geometry('1300x800')

upl = Image.open("Password.png")
upl = upl.resize((224,168))
img = ImageTk.PhotoImage(upl)
lbl = Label(root, image = img, bg = 'light blue')
lbl.place(x = 250, y = 20)  

lbl1 = Label(root,text = "Welcome to Password Strength Checker!")
lbl2 = Label(root,text = "Enter Password to Check Strength")
pwEntr = Entry()

def CheckPw():
  password = pwEntr.get()
  lengthPw = len(password)
  global power
  power= 0
  strength = power
  
  if lengthPw <= 5:
    power  = "Weak"
  elif lengthPw >= 6 and lengthPw <= 8:
    power = "Medium"
  elif lengthPw > 8:
    power = "Strong"
  elif lengthPw > 12:
    power = "Very Strong"
  else:
    res = "Please enter an actual password."
  strength = power
  res = "Result of your password: "+strength+"."
  tb.insert(END, res)
tb = Text(bg = 'black', fg = 'white')
btn1 = Button(root,text = "Check Password",command = CheckPw,bg = 'black',fg = 'white')

lbl1.place(x = 240, y = 220)
lbl2.place(x = 260, y = 250)
pwEntr.place(x = 280, y = 300)
btn1.place(x = 300, y = 340)
tb.place(x = 100, y = 400)

root.mainloop()