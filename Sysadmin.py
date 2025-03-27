import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox
import os
import datetime
import shutil
import subprocess

# Funció per llistar fitxers i directoris 
def llistar_fitxers():
    directori = filedialog.askdirectory()
    if directori:
        llista_fitxers.delete('1.0', tk.END)
        try:
            with os.scandir(directori) as entrades:
                for entrada in entrades:
                    nom = entrada.name
                    tipus = "Directori" if entrada.is_dir() else "Fitxer"
                    mida = entrada.stat().st_size
                    data = datetime.datetime.fromtimestamp(
                        entrada.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
                    linia = f"{nom} ({tipus}) - {mida} bytes - Modificat: {data}\n"
                    llista_fitxers.insert(tk.END, linia)
        except Exception as e:
            messagebox.showerror("Error", f"No s'ha pogut llistar el directori: {e}")

# Funció per eliminar fitxers antics
def eliminar_fitxers_antics():
    if not 'directori_eliminar' in globals() or not directori_eliminar:
        messagebox.showerror("Error", "Primer seleccioneu un directori")
        return
    
    try:
        dies = int(entrada_dies.get())
    except ValueError:
        messagebox.showerror("Error", "Introduïu un nombre vàlid de dies")
        return
    
    data_limit = datetime.datetime.now() - datetime.timedelta(days=dies)
    eliminats = 0
    
    try:
        with os.scandir(directori_eliminar) as entrades:
            for entrada in entrades:
                if entrada.is_file():
                    data_modificacio = datetime.datetime.fromtimestamp(entrada.stat().st_mtime)
                    if data_modificacio < data_limit:
                        os.remove(entrada.path)
                        eliminats += 1
        messagebox.showinfo("Èxit", f"S'han eliminat {eliminats} fitxers")
    except Exception as e:
        messagebox.showerror("Error", f"Error en eliminar fitxers: {e}")

# Funció per seleccionar directori per eliminar fitxers
def seleccionar_directori_eliminar():
    global directori_eliminar
    directori_eliminar = filedialog.askdirectory()
    if directori_eliminar:
        etiqueta_eliminar.config(text=f"Directori seleccionat: {directori_eliminar}")

# Funció per obtenir informació del sistema
def obtenir_info_sistema():
    try:
        # Informació del sistema operatiu
        sistema_operatiu = os.name
        info = f"Sistema operatiu: {sistema_operatiu}\n"
        
        # Informació de l'espai al disc
        disc = shutil.disk_usage('/')
        info += f"Espai al disc:\n"
        info += f"  Total: {disc.total // (2**30)} GB\n"
        info += f"  Utilitzat: {disc.used // (2**30)} GB\n"
        info += f"  Lliure: {disc.free // (2**30)} GB\n"
        
        text_info.delete('1.0', tk.END)
        text_info.insert(tk.END, info)
    except Exception as e:
        messagebox.showerror("Error", f"No s'ha pogut obtenir la informació: {e}")

# Funció per executar comandes
def executar_comanda():
    comanda = entrada_comanda.get()
    if not comanda:
        return
    
    try:
        resultat = subprocess.run(comanda, shell=True, 
                                capture_output=True, 
                                text=True, 
                                timeout=30)
        sortida = f"$ {comanda}\n\n"
        sortida += f"Sortida:\n{resultat.stdout}\n"
        if resultat.stderr:
            sortida += f"Errors:\n{resultat.stderr}\n"
        
        text_sortida.delete('1.0', tk.END)
        text_sortida.insert(tk.END, sortida)
    except subprocess.TimeoutExpired:
        messagebox.showerror("Error", "La comanda ha excedit el temps d'espera")
    except Exception as e:
        messagebox.showerror("Error", f"Error en executar la comanda: {e}")

# Funció per crear còpies de seguretat
def crear_backup():
    if not 'directori_backup' in globals() or not directori_backup:
        messagebox.showerror("Error", "Primer seleccioneu un directori")
        return
    
    fitxer_desti = filedialog.asksaveasfilename(
        defaultextension=".zip",
        filetypes=[("Fitxer ZIP", "*.zip")]
    )
    if not fitxer_desti:
        return
    
    try:
        shutil.make_archive(fitxer_desti.replace('.zip', ''), 'zip', directori_backup)
        messagebox.showinfo("Èxit", f"Còpia de seguretat creada a:\n{fitxer_desti}")
    except Exception as e:
        messagebox.showerror("Error", f"Error en crear la còpia: {e}")

# Funció per seleccionar directori per còpia de seguretat
def seleccionar_directori_backup():
    global directori_backup
    directori_backup = filedialog.askdirectory()
    if directori_backup:
        etiqueta_backup.config(text=f"Directori seleccionat: {directori_backup}")

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