import pyautogui

# Loop infinito
while True:
    # Primeiro clique
    pyautogui.moveTo(1834, 594, duration=0.1)
    pyautogui.click()
    pyautogui.sleep(0.3)
    
    # Segundo clique
    pyautogui.moveTo(1564, 579, duration=0.1)
    pyautogui.click()
    
    # Espera 2 segundos antes de recomeçar
    pyautogui.sleep(2)