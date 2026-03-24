from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import random

url = "https://forms.office.com/Pages/ResponsePage.aspx?id=nn_hqb6Q0EGE62pI6-n-wHbkgWfd36tGkC275PbXaFVUREkzVTgxWVpDOUZSVjAwNFpUSExaVkxaRi4u"

def llenar_encuesta():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(3) # Esperar a que cargue

    try:
        # 1. Buscar todos los campos de entrada de texto
        inputs = driver.find_elements(By.TAG_TYPE, "input")
        
        for ip in inputs:
            # Escribir algo aleatorio o basado en tus necesidades
            ip.send_keys("Dato Simulado " + str(random.randint(1, 100)))
            time.sleep(0.5)

        # 2. Localizar el botón de enviar (usualmente tiene el atributo data-automation-id="submitButton")
        boton_enviar = driver.find_element(By.XPATH, "//button[@data-automation-id='submitButton']")
        boton_enviar.click()
        
        print("Encuesta enviada con éxito")
    except Exception as e:
        print(f"Error: {e}")
    
    time.sleep(2)
    driver.quit()

# Ejecutarlo para tu muestra de 69
for i in range(30):
    print(f"Llenando encuesta {i+1}...")
    llenar_encuesta()