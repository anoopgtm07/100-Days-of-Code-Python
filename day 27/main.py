import tkinter

window = tkinter.Tk()

window.title("My First Program")
window.minsize(height=400, width=500)

my_label = tkinter.Label(text="This is a Label.", font=("Arial", 24, "bold"))
my_label.pack()

window.mainloop()
