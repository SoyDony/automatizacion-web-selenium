Automatización y Monitoreo Web con Python & Selenium 🚀🐍
¡Hola! 👋 Este proyecto es una demo simple pero funcional de automatización y monitoreo web usando Python y Selenium, aplicada a una web que desarrollé anteriormente. Está pensado como punto de partida para tareas de automatización, pruebas básicas y generación de reportes visuales.

¿Qué hace? 🔍
Este script automatiza una serie de acciones sobre la página Little Lemon (https://soydony.github.io/Little-Lemon/index.html): abre la página principal, navega al formulario de contacto, completa y envía datos de prueba, simula un error intencional buscando un elemento inexistente, toma capturas si algo falla y guarda los resultados en CSV y HTML.

¿Por qué este proyecto? 💡
Quería mostrar mis primeras habilidades en automatización web con Selenium, pruebas controladas y scripting básico, reportes automatizados con visualización y registro de errores con capturas. Ideal para aprender, experimentar o compartir en GitHub y LinkedIn como ejemplo práctico.

Requisitos 🛠️
Python 3.7 o superior.
Microsoft Edge WebDriver (https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) — no olvides ajustar la ruta del driver en el script monitor.py.
Librerías necesarias: pip install -r requirements.txt

Instalación y uso 🚀
Cloná el proyecto:
git clone https://github.com/SoyDony/automatizacion-web-selenium.git
cd automatizacion-web-selenium

Instalá las dependencias:
pip install -r requirements.txt

Ejecutá el script principal:
python monitor.py

¿Qué vas a ver? 👀
Al ejecutar el script, se generarán automáticamente:

reporte_observabilidad.csv → Registro de resultados

reporte_observabilidad.html → Visualización amigable en navegador

screenshots/ → Capturas de pantalla si ocurre un error

También verás en consola el paso a paso y los mensajes de estado.

Estructura del proyecto 📂
automatizacion-web-selenium/
├── monitor.py (script principal)
├── requirements.txt (dependencias)
├── README.md (este archivo)
├── .gitignore (archivos/carpetas ignoradas)
└── screenshots/ (capturas si hay errores, se crea automáticamente)

Tips de personalización 🎨
Probalo con otras URLs y adaptá los selectores.
Sumá más validaciones o simulá distintos errores.
Ajustá los time.sleep() según el sitio web.
Útil como base para un sistema de monitoreo propio.

.gitignore recomendado 🧽
Incluí este contenido en .gitignore para evitar subir archivos temporales:
pycache/
.pyc
screenshots/
reporte_observabilidad.

requirements.txt 📦
Debe incluir:
selenium
pandas

Licencia 📄
MIT — Libre para usar, modificar y compartir ⭐

¡Gracias por leer! 🙌
Si te gustó este proyecto o querés dar sugerencias, conectate conmigo en LinkedIn o dejá una ⭐ en el repo.
¡Feliz automatización! 🧪⚡️🐍


