"""Automatizacion de formularios por deteccion de componentes en la pagina web"""

# External Libraries
import os
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def llenar_formulario(driver: webdriver, cols_name: list[str], registro: dict) -> None:
    """Llena el formulario con los datos del registro

    Args:
        driver (webdriver): Driver de selenium
        cols_name (list[str]): Nombres de las columnas del dataframe
        registro (dict): Registro a ingresar en el formulario

    """
    wait = WebDriverWait(driver, 10)
    elements = {
        val: wait.until(EC.presence_of_element_located((By.ID, val.lower())))
        for val in cols_name
    }

    for val in cols_name:
        elements[val].send_keys(str(registro[val]))

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@type="submit"]')))
    submit.click()


if __name__ == "__main__":
    path = "ArenaRPA\\Arena RPA FormData.xlsx"
    data = pd.read_excel(path, engine="openpyxl")
    cols_name = data.columns.to_list()

    #Ejecutar el navegador con:
    #"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222 --user-data-dir="C:\selenium"
    options = webdriver.EdgeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Edge(options=options)

    wait = WebDriverWait(driver, 10)
    start = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, '//a[contains(text(),"Start Challenge")]')
        )
    )
    start.click()

    for _, registro in data.iterrows():
        llenar_formulario(driver, cols_name, registro)

    driver.quit()
