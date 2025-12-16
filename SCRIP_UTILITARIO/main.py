
""""""
import os
import platform #To obtain informations about current System
import subprocess #to use commands Linux

OPERACOES_SISTEMA = {
    "Vendor" : subprocess.check_output(["cat", "/sys/class/dmi/id/sys_vendor"]).decode("utf-8").strip(),
    "Board_Name" : subprocess.check_output(["cat", "/sys/class/dmi/id/board_name"]).decode("utf-8").strip(),
    "RAM" : subprocess.check_output(["free", "-h"]).decode("utf-8").strip(),
}

def formatarOutput(OPERACOES_SISTEMA):
    resultado_formatado = ""
    for chave, valor in OPERACOES_SISTEMA.items():
        resultado_formatado += f"\n{chave}: {valor}\n"
    return resultado_formatado

#Usando modulo os 
print("Nome do sistema operacional:", os.name)

#Usando modulo platform
print("Sistema:", platform.system())
print("Plataform Machine", platform.machine())
print("Sistema:", platform.platform())
#print("Nome do sistema:", platform.uname())
print("Arquitetura:", platform.architecture())
print("Processador:", platform.processor())
print("Versão do sistema operacional:", platform.version())
print("RAM", platform.uname().machine)

formatado = formatarOutput(OPERACOES_SISTEMA)
print(formatado)
    