# interfaz.py
import tkinter as tk
from tkinter import messagebox
from Alamacenamiento import crear_usuario, autenticar_usuario

# ------------------ Animaciones ------------------

def animar_entrada():
    """
    Hace la entrada suave: sube el frame y aumenta opacidad.
    """
    global alpha, y_pos
    if alpha < 1.0:
        alpha += 0.05
        ventana.attributes("-alpha", alpha)

    if y_pos > 0:
        y_pos -= 4
        frame.place(x=0, y=y_pos)

    if alpha < 1.0 or y_pos > 0:
        ventana.after(16, animar_entrada)

def shake_window():
    """
    Animación de temblor al fallar login.
    """
    x = ventana.winfo_x()
    y = ventana.winfo_y()
    secuencia = [(-12,0),(12,0),(-10,0),(10,0),(-6,0),(6,0),(0,0)]

    def mover(i=0):
        if i >= len(secuencia):
            return
        dx, dy = secuencia[i]
        ventana.geometry(f"+{x+dx}+{y+dy}")
        ventana.after(30, lambda: mover(i+1))

    mover()

def hover_boton(boton, color_in, color_out):
    boton.bind("<Enter>", lambda e: boton.config(bg=color_in))
    boton.bind("<Leave>", lambda e: boton.config(bg=color_out))

# ------------------ Lógica ------------------

def manejar_login():
    usuario = entry_usuario.get().strip()
    password = entry_password.get()

    if not usuario or not password:
        messagebox.showwarning("Campos vacíos", "Completa usuario y contraseña.")
        shake_window()
        return

    exito, mensaje = autenticar_usuario(usuario, password)

    if exito:
        messagebox.showinfo("Bienvenido", f"{mensaje} Hola, {usuario} 😎")
        # Aquí luego abrimos tu segunda ventana si quieres
    else:
        messagebox.showerror("Error de login", mensaje)
        shake_window()

def manejar_registro():
    usuario = entry_usuario.get().strip()
    password = entry_password.get()

    if not usuario or not password:
        messagebox.showwarning("Campos vacíos", "Completa usuario y contraseña.")
        shake_window()
        return

    exito, mensaje = crear_usuario(usuario, password)

    if exito:
        messagebox.showinfo("Usuario creado", mensaje)
    else:
        messagebox.showerror("No se pudo crear", mensaje)
        shake_window()

def toggle_password():
    global mostrando
    mostrando = not mostrando
    entry_password.config(show="" if mostrando else "*")
    btn_ver.config(text="🙈" if mostrando else "👁")

# ------------------ UI ------------------

ventana = tk.Tk()
ventana.title("Login Seguro")
ventana.geometry("960x760")
ventana.resizable(False, False)


# Fondo y opacidad inicial
ventana.configure(bg="#0f1115")
ventana.attributes("-alpha", 0.0)

# Frame principal (lo colocamos con place para animar)
frame = tk.Frame(ventana, bg="#0f1115")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Variables para animación
alpha = 0.0
y_pos = 40  # empieza más abajo
frame.place(x=0, y=y_pos, width=420, height=280)

# Tarjeta central
card = tk.Frame(frame, bg="#161a22", padx=20, pady=20)
card.place(relx=0.5, rely=0.5, anchor="center")

# Título
label_titulo = tk.Label(
    card, text="Iniciar sesión",
    font=("Segoe UI", 18, "bold"),
    bg="#161a22", fg="white"
)
label_titulo.grid(row=0, column=0, columnspan=3, pady=(0, 12))

# Usuario
label_usuario = tk.Label(
    card, text="Usuario",
    font=("Segoe UI", 11),
    bg="#161a22", fg="#c9d1d9"
)
label_usuario.grid(row=1, column=0, sticky="w")

entry_usuario = tk.Entry(
    card, font=("Segoe UI", 12),
    bg="#0f1115", fg="white",
    insertbackground="white",
    relief="flat", width=24
)
entry_usuario.grid(row=2, column=0, columnspan=3, pady=(2, 10), ipady=6)

# Password
label_password = tk.Label(
    card, text="Contraseña",
    font=("Segoe UI", 11),
    bg="#161a22", fg="#c9d1d9"
)
label_password.grid(row=3, column=0, sticky="w")

entry_password = tk.Entry(
    card, font=("Segoe UI", 12),
    bg="#0f1115", fg="white",
    insertbackground="white",
    relief="flat", width=21,
    show="*"
)
entry_password.grid(row=4, column=0, columnspan=2, pady=(2, 10), ipady=6, sticky="w")

mostrando = False
btn_ver = tk.Button(
    card, text="👁",
    font=("Segoe UI", 11),
    bg="#0f1115", fg="white",
    relief="flat", width=3,
    command=toggle_password
)
btn_ver.grid(row=4, column=2, padx=(6,0))

# Botones
btn_login = tk.Button(
    card, text="Ingresar",
    font=("Segoe UI", 11, "bold"),
    command=manejar_login,
    bg="#238636", fg="white",
    activebackground="#2ea043",
    relief="flat", padx=10, pady=6, width=12
)
btn_login.grid(row=5, column=0, pady=(8, 0), sticky="w")

btn_registrar = tk.Button(
    card, text="Registrar",
    font=("Segoe UI", 11, "bold"),
    command=manejar_registro,
    bg="#1f6feb", fg="white",
    activebackground="#388bfd",
    relief="flat", padx=10, pady=6, width=12
)
btn_registrar.grid(row=5, column=1, pady=(8, 0), sticky="e")

# Hover bonito
hover_boton(btn_login, "#2ea043", "#238636")
hover_boton(btn_registrar, "#388bfd", "#1f6feb")
hover_boton(btn_ver, "#1b1f2a", "#0f1115")

# Enter = login
ventana.bind("<Return>", lambda e: manejar_login())

# Arranca animación
animar_entrada()

ventana.mainloop()
