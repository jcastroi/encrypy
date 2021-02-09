import argparse
from cryptography.fernet import Fernet
import os
from datetime import date
import sys
def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key","-k", dest = "key", help = "llave para Encriptar/Desencriptar tus archivos")
    parser.add_argument("--file","-f", dest = "file", help = "archivo")
    parser.add_argument("--decrypt","-d", dest = "decrypt", nargs='?', default = False, help="Modo desencriptar")
    return parser.parse_args()

def make_key(key_name):
    key = Fernet.generate_key()
    with open(key_name,'wb') as key_file:
        key_file.write(key)
        
def get_key(key_file):
    return open(key_file,'rb').read()

def encriptador(file,key):
    key=Fernet(key)
    with open(file,'rb') as archivo:
        archivo_leido=archivo.read()
    archivo_encriptado=key.encrypt(archivo_leido)
    with open(file,'wb') as archivo:
        archivo.write(archivo_encriptado)
    return
        
def desencriptador(file,key):
    key=Fernet(key)
    with open(file,'rb') as archivo:
        archivo_leido=archivo.read()
    archivo_desencriptado = key.decrypt(archivo_leido)
    with open(file,'wb') as archivo:
        archivo.write(archivo_desencriptado)
    return

argument=parseArguments()

key_name = argument.key

if argument.key == None:
    if argument.decrypt != False:
        sys.exit('ERROR: es necesario el argumento --key -k')
    key_name='key_'+date.today().strftime("%d-%m-%Y")+'.key'
    print('creando el archivo:',key_name)
    make_key(key_name)

llave = get_key(key_name)
archivo=argument.file
print('llave: ',llave)
print('archivo: ',archivo)
if argument.file == None:
    PATH = ''
else:
    PATH = archivo + '\\'
    
if argument.decrypt == False:
    print('encriptando...')
    try:
        for fichero in os.listdir(path=archivo):
            nombre, ext = os.path.splitext(fichero)
            if ext == '' or ext =='.exe' or ext=='.key':
                continue
            else:
                try:
                    encriptador(PATH+fichero,llave)
                    print('se encripto el archivo: '+ fichero)
                except:
                    print('no se pudo encriptar el archivo: '+ fichero)
    except:
        encriptador(archivo,llave)
        print('se encripto el archivo: '+ archivo)
else :
    print('desencriptando...')
    try:
        for fichero in os.listdir(path=archivo):
            nombre, ext = os.path.splitext(fichero)
            if ext == '' or ext =='.exe' or ext=='.key':
                continue
            else:
                try:
                    desencriptador(PATH+fichero,llave)
                    print('se desencripto el archivo: '+ fichero)
                except:
                    print('no se pudo desencriptar el archivo: '+ fichero)
    except:
        desencriptador(archivo,llave)
        print('se desencripto el archivo: '+ archivo)
