import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    limpar_tela()
    print("""
╔══════════════════════════════════════════════════════════════╗
║        --- CARDAPIO DIGITAL AUTOMATION SYSTEM v1.0 ---       ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   [ GESTÃO DE CARDÁPIO ]                                     ║
║    [1] Criar Produtos                                        ║
║    [2] Criar Bairros                                         ║
║    [3] Criar Complementos                                    ║
║                                                              ║
║   [ FINANCEIRO / DESCONTOS ]                                 ║
║    [x] Em breve...                                           ║
║                                                              ║
║   [ CONFIGURAÇÕES TÉCNICAS ]                                 ║
║    [9] Pegar Coordenada (Setup)                              ║
║    [0] Sair do Programa                                      ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)