# Automatización y Monitoreo Web con Python & Selenium 🚀🐍

¡Hola! 👋 Este proyecto es una demo simple pero funcional de automatización y monitoreo web usando Python y Selenium, aplicada a una web que desarrollé anteriormente. Está pensado como punto de partida para tareas de automatización, pruebas básicas y generación de reportes visuales.

## ¿Qué hace? 🔍

Este script automatiza una serie de acciones sobre la página [Little Lemon](https://soydony.github.io/Little-Lemon/index.html):

- 🌐 Abre la página principal  
- 📋 Navega al formulario de contacto  
- ✍️ Completa y envía datos de prueba  
- ⚠️ Simula un error intencional buscando un elemento inexistente  
- 📸 Toma capturas si algo falla  
- 📊 Guarda los resultados en CSV y HTML  

## ¿Por qué este proyecto? 💡

Quería mostrar mis primeras habilidades en:

- Automatización web con **Selenium**  
- Pruebas controladas y scripting básico  
- Reportes automatizados con visualización  
- Registro de errores con capturas  

Ideal para aprender, experimentar o compartir en GitHub y LinkedIn como ejemplo práctico.

## Requisitos 🛠️

- Python 3.7 o superior  
- [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)  
  ⚠️ No olvides ajustar la ruta del driver en el script `monitor.py`  
- Librerías necesarias:

```bash
pip install -r requirements.txt
Instalación y uso 🚀
Cloná el proyecto:

bash
Copiar
Editar
git clone https://github.com/SoyDony/automatizacion-web-selenium.git
cd automatizacion-web-selenium
Instalá las dependencias:

bash
Copiar
Editar
pip install -r requirements.txt
Ejecutá el script principal:

bash
Copiar
Editar
python monitor.py
¿Qué vas a ver? 👀
Al ejecutar el script, se generarán automáticamente:

reporte_observabilidad.csv → Registro de resultados

reporte_observabilidad.html → Visualización amigable en navegador

screenshots/ → Capturas de pantalla si ocurre un error

También verás en consola el paso a paso y los mensajes de estado.

Estructura del proyecto 📂
bash
Copiar
Editar
automatizacion-web-selenium/
├── monitor.py            # Script principal
├── requirements.txt      # Dependencias
├── README.md             # Este archivo
├── .gitignore            # Archivos/carpetas ignoradas
└── screenshots/          # Capturas si hay errores (se crea automáticamente)
Tips de personalización 🎨
Probalo con otras URLs y adaptá los selectores

Sumá más validaciones o simulá distintos errores

Ajustá los time.sleep() según el sitio web

Útil como base para un sistema de monitoreo propio

.gitignore recomendado 🧽
Incluí este contenido en .gitignore para evitar subir archivos temporales:

markdown
Copiar
Editar
__pycache__/
*.pyc
screenshots/
reporte_observabilidad.*
requirements.txt 📦
Debe incluir:

nginx
Copiar
Editar
selenium
pandas
Licencia 📄
MIT — Libre para usar, modificar y compartir ⭐

¡Gracias por leer! 🙌
Si te gustó este proyecto o querés dar sugerencias, conectate conmigo en LinkedIn o dejá una ⭐ en el repo.

¡Feliz automatización! 🧪⚡️🐍
