# interfaz.py
import tkinter as tk
from tkinter import messagebox
from Alamacenamiento import crear_usuario, autenticar_usuario


def manejar_login():
    usuario = entry_usuario.get().strip()
    password = entry_password.get()

    if not usuario or not password:
        messagebox.showwarning("Campos vacíos", "Completa usuario y contraseña.")
        return       

    exito, mensaje = autenticar_usuario(usuario, password)

    if exito:
        messagebox.showinfo("Bienvenido", f"{mensaje} Hola, {usuario} 😎")
        # Aquí podrías abrir otra ventana o continuar con tu app principal
    else:
        messagebox.showerror("Error de login", mensaje)


def manejar_registro():
    usuario = entry_usuario.get().strip()
    password = entry_password.get()

    if not usuario or not password:
        messagebox.showwarning("Campos vacíos", "Completa usuario y contraseña.")
        return

    exito, mensaje = crear_usuario(usuario, password)

    if exito:
        messagebox.showinfo("Usuario creado", mensaje)
    else:
        messagebox.showerror("No se pudo crear", mensaje)


# ------- Ventana principal -------
ventana = tk.Tk()
ventana.title("Login seguro")
ventana.geometry("380x230")
ventana.resizable(False, False)

# Colores (puedes cambiarlos luego para personalizar)
ventana.configure(bg="#1e1e1e")

frame = tk.Frame(ventana, padx=20, pady=20, bg="#1e1e1e")
frame.pack(expand=True)

label_titulo = tk.Label(
    frame,
    text="Iniciar sesión",
    font=("Arial", 16, "bold"),
    bg="#1e1e1e",
    fg="white"
)
label_titulo.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Usuario
label_usuario = tk.Label(frame, text="Usuario:", bg="#1e1e1e", fg="white")
label_usuario.grid(row=1, column=0, sticky="e", pady=5)

entry_usuario = tk.Entry(frame, bg="#333333", fg="white", insertbackground="white")
entry_usuario.grid(row=1, column=1, pady=5)

# Contraseña
label_password = tk.Label(frame, text="Contraseña:", bg="#1e1e1e", fg="white")
label_password.grid(row=2, column=0, sticky="e", pady=5)

entry_password = tk.Entry(frame, show="*", bg="#333333", fg="white", insertbackground="white")
entry_password.grid(row=2, column=1, pady=5)


# Botones
btn_login = tk.Button(
    frame,
    text="Ingresar",
    command=manejar_login,
    bg="#0078D7",
    fg="white",
    activebackground="#005A9E"
)
btn_login.grid(row=3, column=0, pady=15, sticky="e", padx=5)

btn_registrar = tk.Button(
    frame,
    text="Registrar",
    command=manejar_registro,
    bg="#4CAF50",
    fg="white",
    activebackground="#388E3C"
)
btn_registrar.grid(row=3, column=1, pady=15, sticky="w", padx=5)

# Enter = login
ventana.bind("<Return>", lambda event: manejar_login())

ventana.mainloop()
