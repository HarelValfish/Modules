import tkinter as tk

def greet():
    print("Hello world")

root = tk.Tk()
root.title("My first App with Python")

label = tk.Label(root, text="Welcome to DevOps Course")
label.pack()

label2 = tk.Label(root, text="Instructor: Lirone", fg="blue")
label2.pack()

button = tk.Button(root, text="Stop", width=25, command=greet)
button.pack()

root.mainloop()