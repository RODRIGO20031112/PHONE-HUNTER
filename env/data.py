from tkinter import filedialog
import tkinter as tk
import pandas as pd

def obter_dados_do_csv():
    root = tk.Tk()
    root.withdraw()

    caminho_arquivo = filedialog.askopenfilename(title="Selecione um arquivo Selenium")

    if caminho_arquivo:
        try:
            df = pd.read_csv(caminho_arquivo)
            dados_lista = df.values.tolist()
            
            return dados_lista
        except FileNotFoundError:
            print("Nenhum arquivo selecionado.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")
    else:
        print("Nenhum arquivo selecionado.")
