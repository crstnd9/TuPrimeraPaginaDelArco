# TuPrimeraPaginaDelArco

Este proyecto fue desarrollado con Django como parte del curso de Python.  
La temática elegida es cine argentino.

El sitio permite:  
• Cargar directores  
• Cargar categorías (géneros de películas)  
• Cargar películas asociadas a un director y una categoría  
• Buscar películas por título  

---

## Qué incluye

- Patrón MVT (Modelo – Vista – Template)  
- Herencia de plantillas con `base.html`  
- Tres modelos: Director, Categoría y Película  
- Formularios para cada modelo  
- Formulario de búsqueda de películas  
- Proyecto completo en GitHub  

---

## Cómo ejecutar el proyecto

1. Clonar o descargar el repositorio  
2. Verificar que Python esté instalado  
3. Instalar Django con: **pip install django**  
4. Desde la carpeta del proyecto ejecutar: **python manage.py runserver**  
5. Abrir el navegador en: **http://127.0.0.1:8000/**  

---

## Orden sugerido para probar

1. Inicio – enlace principal  
2. Agregar director  
3. Agregar categoría  
4. Agregar película  
5. Buscar película  

---

## Estructura

- **cine/** – modelos, vistas, formularios, URLs y plantillas  
- **templates/** – archivos HTML  
- **PaginaDelArco/** – configuración del proyecto Django  
