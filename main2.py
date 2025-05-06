from tkinter import *
from tkinter import messagebox

def show():
    global photo
    photo = PhotoImage(file="img.png")
    label6.configure(image = photo)

def inf():
    s = edit4.get()
    if s == "111М":
        messagebox.showinfo("Про спеціальність", edit4.get() + '''\nСпеціальність 111 Математика\nОсвітня програма Комп’ютерна математика''')
    elif s == "СОМ":
        messagebox.showinfo("Про спеціальність", edit4.get() + '''\nСпеціальність 014 Середня освіта\nОсвітня програма Середня освіта. Математика, інформатика''')
    else:
        messagebox.showinfo("Про спеціальність", edit4.get() + "\nТакої спеціальності на факультеті немає")

root = Tk()

root.geometry("300x550+500+100")
root.title("Анкета")

label1 = Label(root, text="Прізвище:", padx=10, pady=10)
label1.grid(row=0, column=0)

edit1 = Entry(root, width=25)
edit1.grid(row=0, column=1)


label2 = Label(root, text="Ім'я:", padx=10, pady=10)
label2.grid(row=1, column=0)

edit2 = Entry(root, width=25)
edit2.grid(row=1, column=1)


label3 = Label(root, text="По батькові:", padx=10, pady=10)
label3.grid(row=2, column=0)

edit3 = Entry(root, width=25)
edit3.grid(row=2, column=1)

checkbutton1 = Checkbutton(root, text="ч")
checkbutton1.grid(row=3, column=1)

checkbutton2 = Checkbutton(root, text="ж")
checkbutton2.grid(row=4, column=1)

label4 = Label(text="Виберіть курс:")
label4.grid(row=5, column=1)

result1 = IntVar()
result1.set(1)

radiobutton1 = Radiobutton(root, text=1, variable=result1, value=1).grid(row=6, column=1)
radiobutton2 = Radiobutton(root, text=2, variable=result1, value=2).grid(row=7, column=1)
radiobutton3 = Radiobutton(root, text=3, variable=result1, value=3).grid(row=8, column=1)
radiobutton4 = Radiobutton(root, text=4, variable=result1, value=4).grid(row=9, column=1)

label5 = Label(text="Спеціальність", padx=10, pady=10)
label5.grid(row=10, column=0)

edit4 = Entry(root, width = 25)
edit4.grid(row=10, column=1)

button1 = Button(root, text="Про спеціальність", width=20, command=inf)
button1.grid(row=11, column=1)

label6 = Label()
label6.grid(row=2, column=3, rowspan=5)

button2 = Button(root, text="Фото", width=20, command=show)
button2.grid(row=12, column=1)

root.mainloop()
