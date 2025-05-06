from tkinter import *
from tkinter import messagebox

def show():
    global photo
    photo = PhotoImage(file="img.png")
    label5.configure(image = photo)

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


label1 = Label(root, text="Прізвище:")
label1.pack()

edit1 = Entry(root, width=25)
edit1.pack()


label2 = Label(root, text="Ім'я:")
label2.pack()

edit2 = Entry(root, width=25)
edit2.pack()


label3 = Label(root, text="По батькові:")
label3.pack()

edit3 = Entry(root, width=25)
edit3.pack()

checkbutton1 = Checkbutton(root, text="ч")
checkbutton1.pack()

checkbutton2 = Checkbutton(root, text="ж")
checkbutton2.pack()

label4 = Label(text="Виберіть курс:")
label4.pack()

result1 = IntVar()
result1.set(1)

radiobutton1 = Radiobutton(root, text=1, variable=result1, value=1).pack()
radiobutton2 = Radiobutton(root, text=2, variable=result1, value=2).pack()
radiobutton3 = Radiobutton(root, text=3, variable=result1, value=3).pack()
radiobutton4 = Radiobutton(root, text=4, variable=result1, value=4).pack()

label5 = Label(text="Спеціальність")
label5.pack()

edit4 = Entry(root, width = 25)
edit4.pack()

button1 = Button(root, text="Про спеціальність", width=20, command=inf)
button1.pack()

label6 = Label()
label6.pack()

button2 = Button(root, text="Фото", width=20, command=show)
button2.pack()


root.mainloop()
