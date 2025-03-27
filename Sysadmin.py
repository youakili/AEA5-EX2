import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
import os
import datetime
import shutil
import subprocess

# Funció per llistar fitxers i directoris 
def llistar_fitxers():
    pass

# Funció per eliminar fitxers antics
def eliminar_fitxers_antics():
    pass

# Funció per seleccionar directori per eliminar fitxers
def seleccionar_directori_eliminar():
    pass

# Funció per obtenir informació del sistema
def obtenir_info_sistema():
    pass

# Funció per executar comandes
def executar_comanda():
    pass

# Funció per crear còpies de seguretat
def crear_backup():
   pass

# Funció per seleccionar directori per còpia de seguretat
def seleccionar_directori_backup():
    pass

# Configuració de la finestra principal
finestra = tk.Tk()
finestra.title("Administrador del Sistema")

# Crear un panell de pestanyes
notebook = ttk.Notebook(finestra)
notebook.pack(fill='both', expand=True, padx=10, pady=10)

# Pestanya 1: Llistar fitxers
pestanya_fitxers = ttk.Frame(notebook)
notebook.add(pestanya_fitxers, text="Llistar Fitxers")

ttk.Button(pestanya_fitxers, text="Seleccionar Directori", 
         command=llistar_fitxers).pack(pady=5)

llista_fitxers = scrolledtext.ScrolledText(pestanya_fitxers, width=80, height=20)
llista_fitxers.pack(fill='both', expand=True)

# Pestanya 2: Eliminar fitxers
pestanya_eliminar = ttk.Frame(notebook)
notebook.add(pestanya_eliminar, text="Eliminar Fitxers")

ttk.Button(pestanya_eliminar, text="Seleccionar Directori", 
         command=seleccionar_directori_eliminar).pack(pady=5)

etiqueta_eliminar = ttk.Label(pestanya_eliminar, text="Directori seleccionat: Cap")
etiqueta_eliminar.pack(pady=5)

frame_entrada = ttk.Frame(pestanya_eliminar)
frame_entrada.pack(pady=5)

ttk.Label(frame_entrada, text="Eliminar fitxers més antics de (dies):").pack(side='left')
entrada_dies = ttk.Entry(frame_entrada, width=5)
entrada_dies.pack(side='left', padx=5)

ttk.Button(pestanya_eliminar, text="Eliminar Fitxers", 
         command=eliminar_fitxers_antics).pack(pady=5)

# Pestanya 3: Informació del sistema
pestanya_info = ttk.Frame(notebook)
notebook.add(pestanya_info, text="Informació del Sistema")

text_info = scrolledtext.ScrolledText(pestanya_info, width=80, height=10)
text_info.pack(fill='both', expand=True)

ttk.Button(pestanya_info, text="Actualitzar Informació", 
         command=obtenir_info_sistema).pack(pady=5)

# Pestanya 4: Executar comandes
pestanya_comandes = ttk.Frame(notebook)
notebook.add(pestanya_comandes, text="Executar Comandes")

entrada_comanda = ttk.Entry(pestanya_comandes, width=60)
entrada_comanda.pack(pady=5)

ttk.Button(pestanya_comandes, text="Executar Comanda", 
         command=executar_comanda).pack(pady=5)

text_sortida = scrolledtext.ScrolledText(pestanya_comandes, width=80, height=15)
text_sortida.pack(fill='both', expand=True)

# Pestanya 5: Còpies de seguretat
pestanya_backup = ttk.Frame(notebook)
notebook.add(pestanya_backup, text="Còpies de Seguretat")

ttk.Button(pestanya_backup, text="Seleccionar Directori per Còpia", 
         command=seleccionar_directori_backup).pack(pady=5)

etiqueta_backup = ttk.Label(pestanya_backup, text="Directori seleccionat: Cap")
etiqueta_backup.pack(pady=5)

ttk.Button(pestanya_backup, text="Crear Còpia de Seguretat", 
         command=crear_backup).pack(pady=5)

# Executar la finestra
finestra.mainloop()