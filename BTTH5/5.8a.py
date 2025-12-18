print('Ngo Xuan Lam')
print('245751030110040')
import tkinter as tk

def create_personal_info_form():
    window = tk.Tk()
    window.title("Thông tin cá nhân")
    window.geometry('350x200')
    window.columnconfigure(1, weight=1) 
    tk.Label(window, text="Họ tên:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
    entry_name = tk.Entry(window)
    entry_name.grid(row=0, column=1, padx=10, pady=5, sticky=tk.EW)
    tk.Label(window, text="Ngày sinh:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
    entry_dob = tk.Entry(window)
    entry_dob.grid(row=1, column=1, padx=10, pady=5, sticky=tk.EW)
    tk.Label(window, text="MSSV:").grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
    entry_mssv = tk.Entry(window)
    entry_mssv.grid(row=2, column=1, padx=10, pady=5, sticky=tk.EW)
    tk.Label(window, text="Ngành học:").grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
    entry_major = tk.Entry(window)
    entry_major.grid(row=3, column=1, padx=10, pady=5, sticky=tk.EW)
    def submit_info():
        print(f"Thông tin đã nhập: {entry_name.get()}, {entry_mssv.get()}")   
    tk.Button(window, text="Submit", command=submit_info).grid(row=4, column=1, pady=10, sticky=tk.E)
    window.mainloop()
if __name__ == "__main__":
    create_personal_info_form()
