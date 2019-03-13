import data as data
import requests
from bs4 import BeautifulSoup
import json
import lxml

# Desenvolvido por: Felipe Ferreira
# Contato: felipeferreiraf@gmail.com



url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm'
r = requests.post(url, params = {'body' : 'UF' 'RS' 'SC'})


soup = BeautifulSoup(r.text, "lxml")

lista_estados = soup.find_all('body')

arquivo_json = open('cep.jsonl', 'w')
arquivo_json.write(str(lista_estados))
arquivo_json.close()

print(lista_estados)

#arquivo = open('cep.txt', 'w')
#arquivo.write(str(lista_estados))
#arquivo.close()
#print(lista_estados)

#print(lista_estados) , name_="UF", value_="RS"

#for lista_localidade in lista_estados :
 #   lista = lista_localidade.find_all('table', class_="tmptabela")
  #  for lista_dados in lista :
   #     print(lista)
