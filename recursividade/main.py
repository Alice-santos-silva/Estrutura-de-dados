# recursividade - quando a função chama a si mesma por um número indefinido de vezes
import os

meses_sistema = ["jan2022","fev2022","mar2022","abr2022","mai2022","jun2022","jul2022","ago2022","set2022","out2022","nov2022","dez2022","jan2021","fev2021","mar2021","abr2021","mai2021","jun2021","jul2021","ago2021","set2021","out2021","nov2021","dez2021","jan2020","fev2020","mar2020","abr2020","mai2020","jun2020","jul2020","ago2020","set2020","out2020","nov2020","dez2020","jan2019","fev2019","mar2019","abr2019","mai2019","jun2019","jul2019","ago2019","set2019","out2019","nov2019","dez2019","jan2018","fev2018","mar2018","abr2018","mai2018","jun2018","jul2018","ago2018","set2018","out2018","nov2018","dez2018","jan2017","fev2017","mar2017","abr2017","mai2017","jun2017","jul2017","ago2017","set2017","out2017","nov2017","dez2017"]
print(len(meses_sistema))

arquivos_extraidos = []

def pegar_arquivos_pastas(pasta):
    lista_arquivos = os.listdir(pasta)
    # se tiver txt e vendas no nome do arquivo vou pegar o nome do mês
    for arquivo in lista_arquivos:
        if ".txt" in arquivo and "Vendas" in arquivo:
            # significa que eu quero pegar o nome do mes:
            nome_mes = arquivo.split()[-1].replace(".txt", "")
            arquivos_extraidos.append(nome_mes)
        elif ".txt" not in arquivo: # se é uma pasta
            pegar_arquivos_pastas(f'{pasta}/{arquivo}')
    pass

pegar_arquivos_pastas("Arquivos")
print(arquivos_extraidos)
print(len(arquivos_extraidos))

for mes in meses_sistema:
    if mes not in arquivos_extraidos:
        print(mes)

