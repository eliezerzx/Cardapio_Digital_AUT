from services import add_produtos
from services import add_bairros
from interfaces import interface
from utils import coordenadas
import sys
import time

# ----- BARRA DE CARREGAMENTO PARA TER UM  "TEMPO" DE CANCELAR CASO DIGITE OPCAO ERRADA -----
def barra_carregamento(texto="Carregando", duracao=2):
    total = 30  # tamanho da barra

    print(f"\n{texto}...\n")
    for i in range(total + 1):
        progresso = int((i / total) * 100)
        barra = "█" * i + "-" * (total - i)

        sys.stdout.write(f"\r[{barra}] {progresso}%")
        sys.stdout.flush()
        time.sleep(duracao / total)

    print("\n")
# ----- BARRA DE SAINDO -----
def barra_saindo(texto="Saindo", duracao=2):
    total = 30  # tamanho da barra

    print(f"\n{texto}...\n")
    for i in range(total + 1):
        progresso = int((i / total) * 100)
        barra = "█" * i + "-" * (total - i)

        sys.stdout.write(f"\r[{barra}] {progresso}%")
        sys.stdout.flush()
        time.sleep(duracao / total)

    print("\n")

interface.exibir_menu()

while True:
    interface.exibir_menu()
    opcao = input("Escolha a Opção: ")

    # ---- Executa opção "1" para rodar add.produtos.py
    if opcao == "1":
        barra_carregamento()
        add_produtos.cadastrar_produtos()
    
    # ---- Executa opção "2" para rodar add.bairros.py
    if opcao == "2":
        barra_carregamento()
        add_bairros.cadastrar_bairros()



    # ---- Executa opção "9" para rodar coordenada.py
    elif opcao == "9":
        coordenadas.coordenada()
        input("\nClique para Voltar...")

    # ---- Executa opção "0" para sair do programa.py
    elif opcao == "0":
        barra_saindo()
        break

    else:
        print("Opção inválida!")