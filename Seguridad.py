import os #modulo que permite trabajar con el sistema operativo
import hashlib #modulo que permite crear hash's 
import base64 #siver para codificar y decodificar con base en el formato Base64
import hmac #combina la funcion hash

# Genera un salt aleatorio para cada usuario
def generar_salt():
    salt = os.urandom(16)  
    return base64.b64encode(salt).decode("utf-8")


# Aplica PBKDF2-HMAC-SHA256 a la contraseña con el salt
def hash_password(password: str, salt: str) -> str:
    password_bytes = password.encode("utf-8")  
    salt_bytes = base64.b64decode(salt.encode("utf-8"))

    dk = hashlib.pbkdf2_hmac("sha256", password_bytes, salt_bytes, 100_000)#Aplica PBKDF2-HMAC-SHA256 lo realiza 1k de veses 
    return base64.b64encode(dk).decode("utf-8")

# Compara una contraseña en texto contra el hash almacenado
def verificar_password(password: str, salt: str, hash_almacenado: str) -> bool:
    nuevo_hash = hash_password(password, salt)
    # compare_digest evita ataques de tiempo (timing attacks)
    return hmac.compare_digest(nuevo_hash, hash_almacenado)