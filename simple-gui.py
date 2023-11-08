import tkinter as tk

def print_hello():
    print("Hello World")

root = tk.Tk()
root.title("Simple GUI")

hello_button = tk.Button(root, text="Say Hello", command=print_hello)
hello_button.pack()

root.mainloop()