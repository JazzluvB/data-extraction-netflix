# Extracción de Datos - Catálogo de Netflix

## Descripción

Este proyecto realiza técnicas de **web scraping** para extraer información del catálogo público de Netflix.  
Se obtienen datos importantes como títulos, géneros y duración de películas y series.  

El objetivo es practicar la extracción, limpieza y organización de datos para un análisis inicial del contenido disponible en la plataforma.

---

## Tecnologías y herramientas utilizadas

- Python 3  
- Jupyter Notebook  
- Librerías: `requests`, `BeautifulSoup`, `pandas`  

---

## Proceso

1. Se realiza una petición HTTP para obtener el código HTML de la página de Netflix.  
2. Con BeautifulSoup se extraen los datos relevantes (títulos, géneros, duración).  
3. Los datos se almacenan y organizan en un DataFrame de pandas para facilitar su análisis.

---

## Resultados

- Se extrajeron aproximadamente **100 títulos** de películas y series.  
- Se identificaron los géneros predominantes y la duración promedio de los contenidos.

---

## Aprendizajes

- Manejo básico de técnicas de **web scraping** con Python.  
- Limpieza y manipulación de datos con pandas.  
- Organización de información para análisis posteriores.  

---

## Cómo ejecutar este proyecto

Para correr el proyecto, instala las librerías necesarias ejecutando en la terminal:

```bash
pip install requests beautifulsoup4 pandas