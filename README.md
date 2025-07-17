# Observabilidad Web con Python & Selenium 🚀🐍

¡Hola! 👋 Este proyecto es una demo simple pero potente de monitoreo y automatización web con **Python** y **Selenium**, aplicada a una web sencilla que desarrollé anteriormente.

Sirve como ejemplo para pruebas de **observabilidad web**, con reportes automatizados y manejo visual de errores.

---

## ¿Qué hace? 🔍

Este script automatiza una serie de acciones sobre la página [Little Lemon](https://soydony.github.io/Little-Lemon/index.html):

- 🌐 Abre la página principal.
- 📋 Navega al formulario de contacto.
- ✍️ Completa y envía datos de prueba.
- ⚠️ Simula un error intencional buscando un elemento inexistente.
- 📸 Toma capturas de pantalla si algo falla.
- 📊 Registra todo en archivos CSV y HTML.

---

## ¿Por qué este proyecto? 💡

Quería mostrar mis primeras habilidades en:

- Automatización con **Selenium**
- Pruebas automatizadas y controladas
- Generación de logs y reportes
- Observabilidad visual de fallas


---

## Requisitos 🛠️

- Python 3.7 o superior
- [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)  
  ⚠️ No olvides ajustar la ruta del driver en el script `monitor.py`
- Librerías necesarias:

```bash
pip install -r requirements.txt
```

---

## Instalación y uso 🚀

Cloná el proyecto:

```bash
git clone https://github.com/SoyDony/observabilidad-web-python-selenium.git
cd observabilidad-web-python-selenium
```

Instalá las dependencias:

```bash
pip install -r requirements.txt
```

Ejecutá el script principal:

```bash
python monitor.py
```

---

## ¿Qué vas a ver? 👀

Al ejecutar el script, se generarán automáticamente:

- 📁 `reporte_observabilidad.csv` → Registro de resultados
- 📁 `reporte_observabilidad.html` → Visualización amigable en navegador
- 📁 `screenshots/` → Capturas de pantalla (solo si ocurre un error)

También verás en consola cada paso del proceso y el resultado final.

---

## Estructura del proyecto 📂

```
observabilidad-web-python-selenium/
├── monitor.py            # Script principal
├── requirements.txt      # Dependencias
├── README.md             # Este archivo
├── .gitignore            # Archivos/carpetas ignoradas
└── screenshots/          # Capturas si hay errores (se crea al correr el script)
```

---

## Tips de personalización 🎨

- 🔁 Probalo con otras URLs y formularios
- ⚙️ Agregá validaciones y errores simulados
- ⏳ Ajustá `time.sleep()` según el rendimiento del sitio
- 📡 Base perfecta para un sistema de monitoreo real

---

## .gitignore recomendado 🧽

Incluí este contenido en `.gitignore`:

```
__pycache__/
*.pyc
screenshots/
reporte_observabilidad.*
```

---

## requirements.txt 📦

Este archivo debe incluir:

```
selenium
pandas
```

---

¡Gracias por pasar! 🙌  
Si te gustó este proyecto o querés dar feedback, no dudes en conectarte conmigo en [LinkedIn](https://www.linkedin.com/in/duran-daniel) o dejar una ⭐ en GitHub.

¡Feliz automatización! 🧪⚡️🐍
