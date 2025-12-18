print('Ngo Xuan Lam')
print('245751030110040')
import tkinter as tk

def create_radio_button_form():
    root = tk.Tk()
    root.title("Lựa chọn Radio Button (Bài 8b)")
    root.geometry('300x200')
    v = tk.IntVar()
    v.set(1) 
    choices = [
        ("Lựa chọn 1", 1),
        ("Lựa chọn 2", 2),
        ("Lựa chọn 3", 3)
    ]
    result_label = tk.Label(root, text="Chưa có lựa chọn nào được xác nhận.", fg="blue")
    result_label.pack(pady=10)
    def on_click_me():
        current_choice_value = v.get()
        choice_text = next((text for text, val in choices if val == current_choice_value), "Không xác định")   
        message = f"Bạn đã chọn: {choice_text} (Giá trị: {current_choice_value})"
        result_label.configure(text=message, fg="red")
        print(message)
    for text, val in choices:
        tk.Radiobutton(root,
                       text=text,
                       padx=20,
                       variable=v,
                       value=val).pack(anchor=tk.W)
    click_button = tk.Button(root, text="Click Me", command=on_click_me)
    click_button.pack(pady=20)
    root.mainloop()
if __name__ == "__main__":
    create_radio_button_form()
