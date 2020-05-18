import requests
import xlwt
import pandas as pd
from bs4 import BeautifulSoup

url ="https://www.calendarr.com/brasil/datas-comemorativas-2021/"

site_em_html = requests.get(url)


soup = BeautifulSoup(site_em_html.text, 'html.parser')


tabela_datas_comemorativas = soup.select('.holidays-box-col2 .row')

mes = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']

dias = []
dia_feriado = []
meses = []
anos = []
dias_semanas = []
comemoracoes = []

for index,row in enumerate(tabela_datas_comemorativas):
    lista_feriados = row.select('ul',class_='list-holidays')
    for feriado in lista_feriados:
        feriados = feriado.select('li',class_='list-holiday-box')
        for f in feriados:
            dia = f.find('div',class_='list-holiday-dayweek').find('span',class_='holiday-day').get_text()
            if f.find('div',class_='holiday') is not None:
                dia_feriado.append('sim')
            else:
                dia_feriado.append('não')
            dias.append(dia)
            dia_semana = f.find('div',class_='list-holiday-dayweek').find('span',class_='holiday-weekday').get_text()
            dias_semanas.append(dia_semana)
            comemoracao = f.find('div',class_='list-holiday-title').get_text()
            comemoracoes.append(comemoracao.strip())
            meses.append(mes[index])
            anos.append(2021)

df = pd.DataFrame({
    "Ano":anos,
    "Mês":meses,
    "Dia":dias,
    "Dia da semana":dias_semanas,
    "Feriado":dia_feriado,
    "Comemoração":comemoracoes
})

df.to_excel("datas_comemorativas_2021.xls")

