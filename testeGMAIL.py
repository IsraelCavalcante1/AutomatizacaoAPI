import smtplib
from unidecode import unidecode


def formatarMensagem(dados):
    mensagem =  f'''Ola, obrigado pela sua compra {dados[0]}
Cidade e Estado da compra:{unidecode(dados[1])}
Bairro: {unidecode(dados[2])}
Rua e Numero: {unidecode(dados[3])}
CEP: {unidecode(dados[4])}
Numero Pedido: {unidecode(dados[5])}
Data do Pedido: {unidecode(dados[6])}
Valor do Pedido: {unidecode(dados[7])}
Volte Sempre!'''
    return 'Subject: {}\n\n{}'.format("informacoes da sua compra! ", mensagem)


def loginGMAIL(mensagem):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("leopontorua@gmail.com", "hxhigowlicckdjkd")
    server.sendmail(
        "leopontorua@gmail.com",
        "mitocho06@gmail.com",
        formatarMensagem(mensagem))

    server.quit()
