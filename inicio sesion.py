 #inicio basico de interfas de inicio de secion,
 # contraseña de prueba, 1234

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("350x300")

def login():
    
    print("Bienvenido")
frame = customtkinter.CTkFrame(master=root)

frame.pack(pady=20, padx=60, fill="both", expand=True)

label =customtkinter.CTkLabel(master=frame, text="login")
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="login", command=login)
button.pack(pady=10, padx=8)

root.mainloop()