from utils import somErro
import pyautogui
import pyperclip
import time

# Configurações iniciais
pyautogui.PAUSE = 0.8  

def cadastrar_produtos():
    try:
        # Note que mudei para 'data/produtos.txt' conforme sua árvore de arquivos anterior
        with open('data/produtos.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print("Erro: O arquivo data/produtos.txt não foi encontrado.")
        return

    print("Iniciando em 5 segundos... Mantenha o navegador aberto e maximizado!")
    time.sleep(5)

    for linha in linhas:
        if not linha.strip():
            continue
            
        partes = linha.split('|')
        if len(partes) < 3:
            continue
            
        nome = partes[0].strip()
        descricao = partes[1].strip()
        preco = partes[2].strip()

        # --- PREENCHIMENTO ---
        # 1. Nome
        pyautogui.moveTo(563, 313, duration=0.1)
        pyautogui.tripleClick()
        pyperclip.copy(nome)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('tab')

        # 2. Descrição
        pyperclip.copy(descricao)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('tab')

        # 3. Preço
        pyperclip.copy(preco)
        pyautogui.hotkey('ctrl', 'v')
        
        # 4. Scroll 
        #pyautogui.scroll(-3000) 
        #time.sleep(1) 

        # 5. Enviar
        pyautogui.click(977, 985) 
        time.sleep(1) # Espera carregar

        # 6. Gerenciar Produtos
        pyautogui.click(542, 202)
        time.sleep(1)

        # 7. Duplicar
        pyautogui.click(1583, 531)
        time.sleep(1)

        # 8. Editar Duplicado
        pyautogui.click(1524, 535)
        time.sleep(2) 

    somErro.som_sucesso()
    pyautogui.alert("✅ Concluído!")

if __name__ == "__main__":
    try:
        cadastrar_produtos()
    except KeyboardInterrupt:
        print("\n🛑 Programa encerrado pelo usuário.")
        try:
            somErro.som_error() # Garanta que esse nome de função existe em utils
        except:
            pass
        pyautogui.alert("Programa encerrado pelo usuário.")