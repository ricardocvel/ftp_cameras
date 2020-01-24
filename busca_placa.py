# coding: UTF-8
#autor ----------------Ricardo Campos
# ricardocampos_pr@ive.com
# 45-998069358
# Empresa XPTI MG
#  ________  __   _______  _________       __        __   ________
# |   _____||__| |  _____| |__|__|  |  ___|  |      |  | |   __   |
# |_______  |  | |  |       _____|__| (_)-|  |  ____|__| |  |  |  |
# |   /\  \ |  | |  |____  |  |___| |__   |  | |  [ ]  | |  |__|  |
# |__/  \__\|__| |_______| |___________|  |__| |_______| |________|

from datetime import date, datetime
from requisicao_helios import requisicao_h
import os
import time

def listar_arq():
    veiculos = []
    path = "fotos/"
    dir = os.listdir(path)
    for file in dir:
        veiculos.append(data_name(file))
    return (veiculos)

def data_name(name):
    dados = [0, 1, 2]
    try:
        srt_name = str(name).split("_")
        dados[0] = srt_name[1]  # placa
        dados[1] = srt_name[4]  # camera
        dados[2] = modificadata(srt_name[0]) # data e hora
        if dados[0] == 'No Plate':
            os.link("fotos/" + name, "noplate/" + name)
            os.remove("fotos/" + name)
            logerro('placa não reconhecida',  'copiado para pasta: ', 'noplate')
        else:
            print(srt_name[1])
            os.rename("fotos/" + name, "fotos/" + srt_name[1] + ".jpg")
        return(dados)
    except Exception as e:
        print(' erro na leitura >>>>>>>>>' + name)
        print(e)
        print(name)
        teste = str(name).split("_")
        print(teste)
        return(dados)

def modificadata(data):
    ano = data[0:4]
    mes = data[4:6]
    dia = data[6:8]
    hora = data[8:10]
    minuto = data[10:12]
    segundo = data[12:14]
    data = ano + '-' + mes + '-' + dia + ' ' + hora + ':' + minuto + ':' + segundo
    return (data)

def logerro(erro, ip, porta): #tipo erro, dispositivo, placa
    hj = str(date.today())
    try:
        logtxt = open('log/log-' + hj + '.txt', 'a')
    except:
        logtxt = open('log/log-' + hj + '.txt', 'w')
        logtxt.close()
        logtxt = open('log/log-' + hj + '.txt', 'a')
    hora = str(datetime.today())
    logtxt.write(hora + ' - IP/PORTA: ' + ip + '-' + porta + '-  ERRO:' + erro + '\n')
    logtxt.close()

def log_placas(beckup):
    hj = str(date.today())
    try:
        logtxt = open('banco/log-' + hj + '.txt', 'a')
    except:
        logtxt = open('banco/log-' + hj + '.txt', 'w')
        logtxt.close()
        logtxt = open('banco/log-' + hj + '.txt', 'a')
    for i in beckup:  # placa, retorno, data
        if i == 'REJEITADO':
            pass
        else:
            logtxt.write( i[2]+ ' - placa: ' + i[0] + '  Status:' + i[1] + '\n')
    logtxt.close()

def apaga_veic(veiculo):
    for file in veiculo:
        try:
            os.remove('fotos/'+ file[0] + '.jpg' )
        except:
            print('arquivo' + file[0] + ' não encontrado.')

def apaga_veiculoname(name_veic):
    try:
        os.remove('fotos/' + name_veic + '.jpg')
    except:
        print('arquivo' + name_veic + ' não encontrado.')

while True:
    dicionario = []
    retorno = []
    try:
        dicionario = listar_arq()
    except Exception as e:
            print(e)
            print('Requisição desconhecida')
            tipoerro = str(e)
            dispo = 'erro na leitura de imagens'
            placa = 'Windows'
            logerro(tipoerro, dispo, placa)
    try:
        for i in dicionario:
            try:
                if i[0] == 0 :
                    pass
                else:
                    retorno.append(requisicao_h(i))
                    print(retorno[0], '=', retorno[1], ',', retorno[2])
            except Exception as e:
                print(e)
                print('Requisição desconhecida')
                tipoerro = str(e)
                dispo = i[1]
                placa = i[0]
                logerro(tipoerro, dispo, placa)

        log_placas(retorno)
        apaga_veic(retorno)
        print(retorno)
        time.sleep(5)
    except Exception as e:
            print(e)
            print('Requisição desconhecida')
            tipoerro = str(e)
            dispo = 'erro no ultimo processo '
            placa = 'request'
            logerro(tipoerro, dispo, placa)





