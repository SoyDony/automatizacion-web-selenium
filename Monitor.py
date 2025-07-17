
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
import pandas as pd

# Ruta al msedgedriver
service = Service("C:\\Users\\Pc\\Desktop\\DANI\\WebDrivers\\msedgedriver.exe")
driver = webdriver.Edge(service=service)

# Lista para guardar resultados del monitoreo
resultados = []

def log_result(paso, estado, detalles=""):
    resultados.append({"Paso": paso, "Estado": estado, "Detalles": detalles})
    print(f"{paso}: {estado} {detalles}")

# Crear carpeta screenshots si no existe
os.makedirs("screenshots", exist_ok=True)

try:
    start = time.time()
    driver.get("https://soydony.github.io/Little-Lemon/index.html")
    carga = time.time() - start
    if carga > 5:
        log_result("ALERTA", "SLOW LOAD", f"La página demoró {carga:.2f}s")
    else:
        log_result("Abrir página principal", "OK", f"{carga:.2f}s")
    time.sleep(2)

    # Click en Contacto
    contacto = driver.find_element(By.LINK_TEXT, "Contacto")
    contacto.click()
    log_result("Click en enlace 'Contacto'", "OK")
    time.sleep(2)

    # Rellenar formulario
    driver.find_element(By.ID, "nombre").send_keys("Daniel")
    driver.find_element(By.ID, "email").send_keys("danielduran1516@gmail.com")
    driver.find_element(By.ID, "asunto").send_keys("Prueba de observabilidad")
    driver.find_element(By.ID, "mensaje").send_keys("Este mensaje fue enviado por Selenium.")
    log_result("Rellenar formulario de contacto", "OK")

    # --- PRUEBA INTENCIONAL DE ERROR ---
    elemento_buscado = "elemento_que_no_existe"
    try:
        driver.find_element(By.ID, elemento_buscado).click()
    except NoSuchElementException:
        detalle_error = f"Elemento no encontrado: ID='{elemento_buscado}'"
        log_result("Prueba error intencional", "FAIL", detalle_error)
        driver.save_screenshot("screenshots/error_intencional.png")

except Exception as e:
    log_result("ERROR general", "FAIL", str(e))
    driver.save_screenshot("screenshots/error_general.png")

finally:
    driver.quit()

    # Guardar reporte CSV
    df = pd.DataFrame(resultados)
    df.to_csv("reporte_observabilidad.csv", index=False)

    # Guardar reporte HTML 
    df.to_html("reporte_observabilidad.html", index=False)

    print("✅ Monitoreo finalizado. Revisa 'reporte_observabilidad.csv', '.html' y 'screenshots/'")
