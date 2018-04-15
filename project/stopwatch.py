import tkinter as tk
penghitung = 0
def hitung(teks):
    def count():
        global penghitung
        penghitung += 1
        teks.config(text=str(penghitung))
        teks.after(1000, count)
    count()
root = tk.Tk()
teks = tk.Label(root, font = "Verdana 16 bold")
teks.pack()
hitung(teks)
tombol = tk.Button(root, text='Stop', width=25, command=root.destroy)
tombol.pack()
root.mainloop()
