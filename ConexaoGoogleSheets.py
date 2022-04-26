import gspread
from google.oauth2 import service_account
import pandas as pd

scopes = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]
json_file = "credenciais.json"


def login():
    credenciais = service_account.Credentials.from_service_account_file(json_file)
    scoped_credentials = credenciais.with_scopes(scopes)
    gc = gspread.authorize(scoped_credentials)
    print('Login efeituado com sucesso!')
    return gc


def leitor(gc):
    planilha = gc.open("MediccontTestando")
    aba = planilha.worksheet("Dados")
    dados = aba.get_all_records()
    df = pd.DataFrame(dados)
    print('Dados lidos com sucesso!')
    return df


def escritor(lista, gc):
    planilha = gc.open('MediccontTestando')
    planilha = planilha.worksheet('Dados')
    planilha.append_row(lista, value_input_option='USER_ENTERED')
    print("Dados escritos na planilha com sucesso!")
