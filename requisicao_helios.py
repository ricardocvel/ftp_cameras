# coding: UTF-8
#autor ----------------Ricardo Campos
# ricardocampos_pr@ive.com
# 45-998069358
# Empresa XPTI MG

import json
import requests
import base64
import os
from PIL import Image
#from graphic_engine.cut import listar_arq

erro_envio = ' REJEITADO'

# Função que recorta a imagem
def modifica_data(data_mo):
    fatia = data_mo.split('T')
    fatia2 = fatia[1].split('-')
    dat = fatia[0]+' '+fatia2[0]
    print(dat)

def listar_arq(plate):

    try:
        im = Image.open("fotos/" + plate+".jpg")  # abre o arquivo de entrada
        (width, height) = im.size  # obter o tamanho da imagem de entrada

            # print(im)
            # print(width)
            # print(height)

        box = (820, 80, 1700, 650) #esquerda,topo, direita, inferior
        region = im.crop(box)
        # cropped = im.crop((l, t, r, b))
        region.save("fotos/" + plate + ".jpg")

    except:
        print('imagem_vazia')

def requisicao_h(veiculo):   # placa, camera, data
    if veiculo[0] == 'No Plate':
        veiculo[1] = 'veiculo não enviado por não possuir placa valida'
        return(veiculo)


    url = 'https://putsreq.com/8FRtCTHChSrQ6NsNnebg'
    urls = 'https://helios.policiamilitar.mg.gov.br/v3/api/_track/register'

    headers = {'Authorization': 'Token fornecido pela PMMG)',
                 'Content-Type': 'application/json',
                 'CONTENT-LENGTH':'85'
            }

    listar_arq(veiculo[0])
    ba64 = b''
    with open("fotos/" + veiculo[0] + ".jpg", "rb") as img_file:

        ba64 = base64.b64encode(img_file.read())
    teste = (ba64.decode('utf-8'))
    print(teste)
    print(str(ba64))

    #dat = modifica_data(data_req[1])
    if veiculo[1] == 'LPR01.jpg':
        veiculo[1] = "camera01"

    # teste = b64.decode("utf-8")


    data = {'cam': veiculo[1],
                'dat': veiculo[2],
                'img': 'data:image/jpeg;base64,'+teste,
                'plc': veiculo[0]
                }
    print(data['img'])
    #("utf8") 'img': b64.decode
    data1 = {}

    r = requests.post(url, data=json.dumps(data), headers=headers)

    print(r.status_code)
    print(r.text)

    veiculo[1] = str(r.status_code) + str(r.text)
    #veiculo[1] = r.text   # placa, retorno, data
    return(veiculo)


listar_arq('teste')