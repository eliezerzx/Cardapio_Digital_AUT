from utils import somErro
import pyautogui
import os
import time

def cadastrar_bairros():
    try:
        with open('data/bairros.txt', 'r', encoding='utf-8') as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print("Erro: arquivo data/bairros.txt não encontrado!")
        return

    print("Você tem 5 segundos para preparar o navegador...")
    time.sleep(5)

    for linha in linhas:
        if not linha.strip(): 
            continue

        try:
            # Agora separamos apenas por '|' assim como nos produtos
            partes = linha.split('|')

            if len(partes) < 2:
                print(f"Linha ignorada (formato incorreto): {linha}")
                continue

            # Limpa os dados: remove o R$ (se houver) e espaços extras
            nome_bairro = partes[0].strip()
            preco = partes[1].replace('R$', '').strip()

            print(f" Cadastrando: {nome_bairro} | R$ {preco}")

            # --- Automação ---
            # Digita o Bairro (Certifique-se de que o campo já está focado)
            pyautogui.write(nome_bairro, interval=0.05) 
            time.sleep(0.5)

            pyautogui.press('tab')
            time.sleep(0.5)

            # Digita o Preço
            pyautogui.write(preco, interval=0.05)
            time.sleep(0.5)

            pyautogui.press('enter')
            
            # Espera o salvamento do site
            time.sleep(3) 

            # Sequência de cliques para resetar/próximo (coordenadas que você definiu)
            pyautogui.click(603, 262)
            time.sleep(1)

            pyautogui.click(1460, 334)
            time.sleep(1)

            pyautogui.click(1084, 393)
            time.sleep(1.5)

        except Exception as e:
            print(f"❌ Erro ao processar linha: {e}")

    pyautogui.alert("✅ Todos os bairros foram processados!")
    somErro.som_sucesso()

if __name__ == "__main__":
    try:
        cadastrar_bairros()
    except KeyboardInterrupt:
        print("\n🛑 Programa encerrado pelo usuário.")
        try:
            somErro.som_error()
        except:
            pass
        pyautogui.alert("❌ Programa encerrado pelo usuário.")