#!/usr/bin/env python3
"""Script to get missing 2015 work experience using selenium"""


import selenium.webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


url = "http://www.servidorespublicos.gob.mx/registro/datosAbiertos.jsf"
driver = selenium.webdriver.Firefox()
driver.implicitly_wait(10)
driver.get(url)
n_deps = range(326, 375)


for n in n_deps:
    print(f"Processing {n} institution")
    time.sleep(3)
    try:
        element_is_visible = EC.presence_of_element_located(
            (By.ID, "form:catDepcia_label"))
        deps = WebDriverWait(driver, 70).until(element_is_visible)
    except TimeoutException:
        print(f"Institution {n - 1} took to long to load!")
        print(f"Quitting before finishing")
        break
    deps.click()
    dep = driver.find_element_by_id(f"form:catDepcia_{n}")
    dep.click()
    year = driver.find_element_by_xpath("//li[@data-item-value='2015']")
    year.click()
    add = driver.find_element_by_xpath("//button[@title='Add']")
    add.click()
    time.sleep(1)
    search = driver.find_element_by_id("form:idBusqArch")
    search.click()
    try:
        element_is_visible = EC.element_to_be_clickable(
            (By.ID, "form:idButtonConfirmar"))
        confirm = WebDriverWait(driver, 70).until(element_is_visible)
    except TimeoutException:
        print(f"Institution {n} took to long to first confirm!")
        print(f"Quitting before finishing")
        break
    confirm.click()
    try:
        element_is_visible = EC.element_to_be_clickable(
            (By.ID, "form:idDtgrid23:5:idLinkFile"))
        exp = WebDriverWait(driver, 15).until(element_is_visible)
    except TimeoutException:
        print(f"Institution {n} took to long to show results!")
        try:
            driver.find_element_by_id("form:idDtgrid23:5:contadorTexto")
            print(f"No data found for institution {n}, skipping it!")
            continue
        except Exception:
            print("Quitting before finishing")
            break
    time.sleep(2)
    exp.click()
    try:
        element_is_visible = EC.element_to_be_clickable(
            (By.ID, "form:idButtonConfirmarZip"))
        confirm_zip = WebDriverWait(driver, 70).until(element_is_visible)
    except TimeoutException:
        print(f"Institution {n} took to long to first confirm zip file!")
        print(f"Quitting before finishing")
        break
    confirm_zip.click()
    print(f"Finished processing institution {n}")
    print('-' * 80)
driver.quit()
