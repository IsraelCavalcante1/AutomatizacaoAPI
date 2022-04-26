from selenium import webdriver
from time import sleep
import os
import ConexaoGoogleSheets
from selenium.webdriver.common.by import By
import testeGMAIL

driver = webdriver.Firefox()
driver.get(
    "https://www.amazon.com.br/ap/signin?_encoding=UTF8&openid.assoc_handle=brflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com.br%2Fgp%2Fyourstore%2Fhome%3Fie%3DUTF8%26action%3Dsign-out%26path%3D%252Fgp%252Fyourstore%252Fhome%26ref_%3Dnav_AccountFlyout_signout%26signIn%3D1%26useRedirectOnSuccess%3D1")

input_email = driver.find_element(By.ID, 'ap_email')
input_email.send_keys(os.environ['LOGIN'])

botao_continuar_login = driver.find_element(By.ID, 'continue')
botao_continuar_login.click()

input_password = driver.find_element(By.ID, 'ap_password')
input_password.send_keys(os.environ['SENHA'])

botao_fazer_login = driver.find_element(By.ID, 'signInSubmit')
botao_fazer_login.click()

minhas_compras = driver.find_element(By.ID, 'nav-orders')
minhas_compras.click()
sleep(5)
botao_dias = driver.find_element(By.ID, 'a-autoid-1-announce')
botao_dias.click()

botao_2021 = driver.find_element(By.ID, 'orderFilter_2')
botao_2021.click()
sleep(5)

dados = ["Nome", "Cidade e Estado", "Bairro", "Rua e Número", "CEP", "Número Pedido", "Data Pedido", "Valor do Pedido"]
gc = ConexaoGoogleSheets.login()
ConexaoGoogleSheets.escritor(dados, gc)
for indice_pedido in range(0, 4):
    div_pedido = driver.find_elements(By.CLASS_NAME, "a-vertical")
    div_pedido[indice_pedido].click()
    valor_pedido = driver.find_elements(By.CLASS_NAME, "a-text-bold")
    valor_pedido_final = valor_pedido[1].text.replace("R$", "")
    pedido_data_compra_numero = driver.find_elements(By.CLASS_NAME, "order-date-invoice-item")
    pedido_data_compra = pedido_data_compra_numero[0].text.replace("Pedido em", '')
    numero_pedido = pedido_data_compra_numero[1].text.replace("Pedido nº", '')
    nome_completo = driver.find_element(By.CLASS_NAME, "displayAddressFullName").text
    rua_numero = driver.find_element(By.CLASS_NAME, "displayAddressAddressLine1").text
    bairro = driver.find_element(By.CLASS_NAME, "displayAddressAddressLine2").text
    cidade_estado = driver.find_element(By.CLASS_NAME, "displayAddressCityStateOrRegion").text
    cep = driver.find_element(By.CLASS_NAME, "displayAddressPostalCode").text

    informacao_final = [nome_completo, cidade_estado, bairro, rua_numero, cep, numero_pedido, pedido_data_compra,
                        valor_pedido_final]

    ConexaoGoogleSheets.escritor(informacao_final, gc)
    driver.back()
    testeGMAIL.loginGMAIL(informacao_final)
