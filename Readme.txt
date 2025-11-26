===========================================
      Proyecto: Login Seguro con Python
===========================================

Descripción
-----------
Este proyecto implementa un sistema de autenticación seguro usando Python. 
Incluye:

- Registro de usuarios
- Login con verificación segura
- Hashing de contraseñas con PBKDF2-HMAC-SHA256
- Salts aleatorios por usuario
- Interfaz gráfica moderna con animaciones (Tkinter)
- Archivo JSON para almacenamiento de usuarios

El objetivo es crear un sistema educativo y práctico sobre cómo funciona un
sistema de login seguro siguiendo buenas prácticas de ciberseguridad.


Estructura del Proyecto
-----------------------

1. Seguridad.py     (capa de seguridad y hashing)    :contentReference[oaicite:0]{index=0}
2. Almacenamiento.py (gestión de usuarios y JSON)     :contentReference[oaicite:1]{index=1}
3. Interfaz.py       (interfaz gráfica con Tkinter)   :contentReference[oaicite:2]{index=2}
4. Usuarios.json     (base de datos local)            :contentReference[oaicite:3]{index=3}


------------------------------------------
1. Seguridad.py  —  Capa Criptográfica
------------------------------------------

Aquí se manejan todas las funciones de seguridad del proyecto:

- generar_salt(): crea un salt aleatorio por usuario con os.urandom()
- hash_password(): genera un hash seguro con PBKDF2-HMAC-SHA256 (100 000 iteraciones)
- verificar_password(): compara hashes usando compare_digest (evita timing attacks)

Este archivo es responsable de asegurar las contraseñas antes de almacenarlas.


-----------------------------------------------------
2. Almacenamiento.py  —  Manejo del archivo JSON
-----------------------------------------------------

Este módulo se encarga del CRUD de usuarios:

- cargar_usuarios(): lee Usuarios.json y devuelve un diccionario
- guardar_usuarios(): escribe el diccionario de usuarios en JSON
- crear_usuario(): valida, genera salt, hashea y guarda usuarios
- autenticar_usuario(): compara contraseña ingresada con la almacenada

Validaciones implementadas:
- Mínimo 8 caracteres
- Al menos un carácter especial
- Usuario no repetido


----------------------------------------------------------
3. Interfaz.py  —  Interfaz
