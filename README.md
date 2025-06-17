# TuPrimeraPaginaDelArco

Este proyecto es una aplicación web estilo blog, desarrollada en Django, donde se pueden consultar, crear y gestionar películas del cine argentino. Cuenta con funcionalidades de autenticación, perfiles de usuario, mensajería interna y CRUD completo del modelo principal.

---

## 🔧 Tecnologías utilizadas

- Python 3
- Django 5.2
- SQLite3
- HTML / CSS (básico)
- Bootstrap (opcional)
- Django CKEditor

---

## 🎬 Funcionalidades principales

- Registro, login, logout de usuarios
- Perfil de usuario con avatar, nombre, apellido, email y biografía
- Edición del perfil y cambio de contraseña
- CRUD de películas (título, director, descripción enriquecida, imagen, **año de estreno**)
- Búsqueda de películas por título
- Reseñas de usuarios por película
- Mensajes entre usuarios
- Vista de inicio y vista "Acerca de mí"
- Validación de login para crear/editar/borrar
- Plantilla base con herencia (`base.html`) y navegación
- CBV, mixins y decoradores utilizados correctamente
- Mensajes si no hay resultados en la búsqueda o en el listado
- Rutas organizadas por apps (`cine`, `perfiles`, `mensajes`)

---

## 🗂 Estructura del proyecto

- `cine`: manejo de películas (modelo principal)
- `perfiles`: vistas de registro, login, perfil y edición de usuario
- `mensajes`: envío, lectura y bandeja de entrada de mensajes
- `templates`: herencia de diseño con navbar y diseño responsive
- `media`: carpeta local donde se guardan las imágenes (avatar y películas)

---

## 🚫 Archivos excluidos del repositorio

En `.gitignore` se excluyeron los siguientes archivos y carpetas:

- `__pycache__/`
- `db.sqlite3`
- `/media/`

---

## 📦 Instalación y ejecución

1. Clonar el repositorio  
   `git clone https://github.com/crstnd9/TuPrimeraPaginaDelArco`

2. Crear un entorno virtual  
   `python -m venv env`

3. Activar el entorno virtual  
   - En Windows: `env\Scripts\activate`  
   - En Linux/macOS: `source env/bin/activate`

4. Instalar dependencias  
   `pip install -r requirements.txt`

5. Correr migraciones  
   `python manage.py migrate`

6. Levantar el servidor  
   `python manage.py runserver`

7. Acceder desde el navegador a  
   `http://localhost:8000/`

---

## 📧 Autor

Proyecto individual realizado por: **Cristian Del Arco**
