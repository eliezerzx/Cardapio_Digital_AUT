from utils import somErro
import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 0.5 

def cadastrar_complementos():
    try:
        with open('data/complementos.txt', 'r', encoding='utf-8') as arquivo:
            linhas = [l.strip() for l in arquivo.readlines() if l.strip()]
    except FileNotFoundError:
        print("Arquivo não encontrado!")
        return

    print("Iniciando... Clique no PRIMEIRO campo 'Nome' e aguarde.")
    time.sleep(5)

    total_linhas = len(linhas)

    for i, linha in enumerate(linhas):
        partes = linha.split('|')
        if len(partes) < 3: continue
        nome, descricao, valor = partes[0].strip(), partes[1].strip(), partes[2].strip()

        # --- PREENCHIMENTO ---
        # 1. Nome
        pyperclip.copy(nome)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('tab')

        # 2. Descrição
        pyperclip.copy(descricao)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('tab')

        # 3. Valor
        pyperclip.copy(valor)
        pyautogui.hotkey('ctrl', 'v')
        
        # --- NAVEGAÇÃO ---
        if i < total_linhas - 1:
            # Clica no botão "Adicionar item"
            pyautogui.click(489, 818) 
            time.sleep(1)

            pyautogui.click(741, 814) # Ajuste essas coordenas para clicar dentro do NOVO campo Nome
            
            # Se a página estiver crescendo muito, use o scroll para "puxar" o botão de volta
            pyautogui.scroll(-250) 
        else:
            # Finalizar
            pyautogui.hotkey('ctrl', 'end') # Garante que vai para o fim da página
            time.sleep(0.5)
            pyautogui.click(573, 901) # Coordenada do Enviar

    somErro.som_sucesso()
    pyautogui.alert("✅ Concluído!")

if __name__ == "__main__":
    try:
        cadastrar_complementos()
    except KeyboardInterrupt:
        print("\n🛑 Programa encerrado pelo usuário.")
        try:
            somErro.som_error()
        except:
            pass
        pyautogui.alert("❌ Programa encerrado pelo usuário.")