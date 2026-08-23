from tkinter import *

w = Tk()
w.title("My Profile Card")
w.geometry("400x380")

Label(w, text="My Profile Card", fg="white", bg="purple", width = 40).grid(
    row=0, columnspan=2
)

Label(w, text="Name:").grid(row=1, column=0)
Entry(w, fg="blue", bg="lightyellow").grid(row=1, column=1)

Label(w, text="Hobby:").grid(row=2, column=0)
Entry(w, fg="blue", bg="lightyellow").grid(row=2, column=1)

f = Frame(w, relief=RAISED, borderwidth=3)
f.grid(row=3, columnspan=2)
Label(f, text="About Me:").pack()
Text(f, fg="green", bg="lightyellow", width=40, height=4).pack()

Button(w, text="Show My Card", bg="purple", fg="white").grid(row=4, columnspan=2)
w.mainloop()
