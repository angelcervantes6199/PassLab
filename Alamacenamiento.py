import json
import os
from Seguridad import generar_salt, hash_password, verificar_password
import re
RUTA_ARCHIVO = "Usuarios.json"


def cargar_usuarios() -> dict:
    if not os.path.exists(RUTA_ARCHIVO):
        return {}
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Si el archivo está corrupto, devolvemos un diccionario vacío
        return {}


def guardar_usuarios(usuarios: dict) -> None:
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)


def crear_usuario(username: str, password: str) -> tuple[bool, str]:
    usuarios = cargar_usuarios()

    if username in usuarios:
        return False, "El usuario ya existe."
    if not re.search(r"[!@#$%^&*()_\-\+=\[{\]};:'\",.<>/?]", password):
        return False, "La contraseña debe tener al menos 1 caracterespecial."
    if len(password) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres."
    

    salt = generar_salt()
    pwd_hash = hash_password(password, salt)

    usuarios[username] = {
        "salt": salt,
        "password_hash": pwd_hash
    }

    guardar_usuarios(usuarios)
    return True, "Usuario creado correctamente."


def autenticar_usuario(username: str, password: str) -> tuple[bool, str]:
    usuarios = cargar_usuarios()

    if username not in usuarios:
        return False, "El usuario no existe."

    datos = usuarios[username]
    salt = datos["salt"]
    hash_almacenado = datos["password_hash"]

    if verificar_password(password, salt, hash_almacenado):
        return True, "Login exitoso."
    else:
        return False, "Contraseña incorrecta."
