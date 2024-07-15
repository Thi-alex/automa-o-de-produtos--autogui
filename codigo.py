import pyautogui
import time

pyautogui.PAUSE = 0.5

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Login
pyautogui.click(x=1026, y=485)
pyautogui.write("automacaopython@gmail.com")
pyautogui.press("tab") 
pyautogui.write("12345")
pyautogui.press("enter") 
time.sleep(3)

#importar pandas
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

#cadastrar produto
for linha in tabela.index:
    pyautogui.click(x=651, y=331)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") 
    pyautogui.scroll (5000)
