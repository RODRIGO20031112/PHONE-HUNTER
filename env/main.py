from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from data import obter_dados_do_csv
from selenium import webdriver
from tqdm import tqdm
import time
import csv

def salvar_resultados_em_csv(resultados, nome_arquivo):
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerows(resultados)

options = webdriver.ChromeOptions()
options.add_argument("--headless")

chrome_service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=chrome_service, options=options)

dados_csv = obter_dados_do_csv()
resultados = []

barra_progresso = tqdm(total=len(dados_csv), desc='Processando', position=0, leave=True)

for i in dados_csv:
    time.sleep(2)
    driver.get(f"https://www.google.com.br/maps/search/{i[0]}/@-23.4668482,-46.6746935,15z/data=!3m1!4b1?entry=ttu")
    elementos = driver.find_elements(By.CLASS_NAME, "UsdlK")

    for elemento in elementos:
        resultados.append([elemento.text])

    barra_progresso.update(1)

barra_progresso.close()

salvar_resultados_em_csv(resultados, 'resultados.csv')

driver.quit()