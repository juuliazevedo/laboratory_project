import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()

# acessando o site
navegador.get("https://ingressodigital.com/")
navegador.maximize_window()
time.sleep(2)

# clicando no espaço de busca
navegador.find_element("class name", "form-control").click()

# digitando a cidade e clicando em buscar
navegador.find_element("id", "txt_busca").send_keys("Maceió")
botão_busca = navegador.find_element(By.XPATH, "//button[contains(text(), 'Buscar')]").click()
time.sleep(1)

# extrai os TÍTULOS de cada evento mostrado na página da cidade Maceió
titulos = navegador.find_elements(By.CLASS_NAME, "titulo-card")
lista_titulos = []
for titulo in titulos:
    nome = titulo.text
    lista_titulos.append(nome)

# extrai as CATEGORIAS de cada evento mostrado na página da cidade Maceió
categorias = navegador.find_elements(By.CLASS_NAME, "genero-evento-card")
lista_categorias = []
for categoria in categorias:
    genero = categoria.text
    lista_categorias.append(genero)

# variável que acessa cada evento para pegar as informações futuras (data, preços, horários)
card_eventos = navegador.find_elements(By.CLASS_NAME, "area-cont-card")

lista_valores = []
lista_datas = []
lista_horarios = []

for data in range(len(card_eventos)):
    # recarrega os eventos, pois depois do back() eles mudam
    card_eventos = navegador.find_elements(By.CLASS_NAME, "area-cont-card")  # variável é reiniciada
    evento = card_eventos[data]

    # traz o evento para a tela, com 1s para visualização e carregamento
    navegador.execute_script("arguments[0].scrollIntoView(false);", evento)
    time.sleep(1)

    # clica no card
    evento.click()
    time.sleep(1)

    # extrai os VALORES dos ingressos (do mínimo valor ao máximo valor)
    valores_elementos = navegador.find_elements(By.CLASS_NAME, "valores-ing")
    if valores_elementos:
        # pega o texto de todos os elementos de valor
        todos_valores = [elem.text for elem in valores_elementos]
        # junta todos os valores encontrados
        lista_valores.append(" / ".join(todos_valores))
    else:
        lista_valores.append("Valor não encontrado")

    # extrai as DATAS dos eventos
    data_especifica = navegador.find_elements(
        By.CSS_SELECTOR, "button.btn-datas.clicavelData")
    lista_datas_temp = []
    for i in data_especifica:
        tratado = i.text
        if tratado: 
            lista_datas_temp.append(tratado)
    lista_datas.append(" / ".join(lista_datas_temp))

    # extrai os HORÁRIOS de cada evento
    hora_especifica = navegador.find_elements(
        By.CSS_SELECTOR, "button.btn-datas.clicavelHora")
    lista_horarios_temp = []
    for j in hora_especifica:
        tratado = j.text.strip()
        # limpeza extra para prevenção, decorrente da necessidade nos testes realizados
        tratado = tratado.replace('/', '').strip()
        if tratado != '':  # se tratado não for str vazia, tratado é adicionado na lista
            lista_horarios_temp.append(tratado)

    # analise do uso do separador "/", caso lista tenha mais de 1 elemento
    if len(lista_horarios_temp) == 1:
        lista_horarios.append(lista_horarios_temp[0])
    elif len(lista_horarios_temp) > 1:
        lista_horarios.append(" / ".join(lista_horarios_temp))
    else:
        lista_horarios.append("")

    # volta para página com todos os eventos de maceió
    navegador.back()
    time.sleep(1)

dictDF = {'TÍTULO': lista_titulos,
          'CATEGORIA': lista_categorias,
          'DATA': lista_datas,
          'HORÁRIO': lista_horarios,
          'VALOR': lista_valores}
print(pd.DataFrame(dictDF))

df = pd.DataFrame(dictDF)
#df.to_csv("mcz_eventos.csv")
