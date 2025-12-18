print('Ngo Xuan Lam')
print('245751030110040')
import tkinter as tk

def create_tkinter_window():
    window = tk.Tk()
    window.title("Ứng dụng Tkinter (Bài 4)")
    window.geometry('400x200')
    lbl = tk.Label(window, text="Trạng thái ban đầu...")
    lbl.pack(pady=20) 
    def clicked():

        lbl.configure(text="Nút đã được nhấn! bg/fg đã đổi.")
        btn.configure(bg="green", fg="white")
    btn = tk.Button(window, 
                    text="Nhấn vào đây", 
                    command=clicked,
                    bg="yellow", 
                    fg="black",
                    width=20,
                    height=2)
    btn.pack(pady=10)
    window.mainloop()
if __name__ == "__main__":
    create_tkinter_window()
