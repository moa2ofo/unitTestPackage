# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:37:13 2025

@author: moa2ofo
"""

import re
import os


# Lista per memorizzare gli oggetti
moduli = []
PATH = "../../elop_048/platform/basic_sw_platform/monitoring/test"
MARKER = "/* Do not enter any characters below this string */"
# Aggiunta di oggetti alla lista
moduli.append({"nome_modulo": "VoltMon.c", "nome_funzione": "VoltMon_Run", "percorso":PATH })
moduli.append({"nome_modulo": "SpeedMon.c", "nome_funzione": "SpeedMon_Run", "percorso":PATH })
moduli.append({"nome_modulo": "CurrentMon.c", "nome_funzione": "CurrentMon_Derating", "percorso":PATH })
moduli.append({"nome_modulo": "LinStub.c", "nome_funzione": "ApplLinDiagEcuReset", "percorso":PATH })
moduli.append({"nome_modulo": "LinStub.c", "nome_funzione": "ApplLinDiagEcuReset", "percorso":PATH })
moduli.append({"nome_modulo": "BridgeCtrl.c", "nome_funzione": "OffStateHandler", "percorso":PATH })



def find_and_extract_function( file_name, function_name):
    """
    Cerca un file all'interno di una cartella e delle sue sottocartelle, estrae una funzione,
    il suo corpo e il tipo di ritorno.

    :param directory: Cartella in cui cercare il file
    :param file_name: Nome del file da trovare
    :param function_name: Nome della funzione da estrarre
    :return: Stringa contenente il tipo, la definizione e il corpo della funzione
    """
    directory = "../../elop_048"
    file_path = None

    # Cerca il file nella cartella e nelle sottocartelle
    for root, _, files in os.walk(directory):
        if file_name in files:
            file_path = os.path.join(root, file_name)
            break

    if not file_path:
        return f"❌ Errore: Il file '{file_name}' non è stato trovato nella cartella '{directory}'."

    try:
        # Legge il file
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Trova l'intestazione della funzione (tipo di ritorno + nome funzione + parametri)
        function_pattern = re.compile(rf"(\w+\s+\*?{function_name}\s*\([^)]*\))\s*\{{", re.MULTILINE)
        match = function_pattern.search(content)

        if not match:
            return f"⚠️ Funzione '{function_name}' non trovata in '{file_name}'."

        # Estrarre l'intera funzione
        start_index = match.start()
        function_header = match.group(1)  # Include il tipo di ritorno

        # Determina il tipo di ritorno
        return_type = function_header.split(function_name)[0].strip()

        # Gestire parentesi nidificate per estrarre il corpo della funzione
        open_braces = 0
        function_body = ""

        for i in range(start_index, len(content)):
            char = content[i]
            function_body += char

            if char == "{":
                open_braces += 1
            elif char == "}":
                open_braces -= 1
                if open_braces == 0:  # Fine della funzione
                    break

        # Formatta il risultato come stringa
        extracted_function = f"\n\n{function_body}"
        return extracted_function

    except Exception as e:
        return f"❌ Errore durante la lettura del file: {e}"




def create_test_folder(base_path, name):
    """
    Crea una cartella di nome 'TEST_nome' con due sottocartelle 'src' e 'test' 
    solo se non esiste già.
    
    :param base_path: Percorso in cui creare la cartella
    :param name: Nome da usare per creare la cartella 'TEST_nome'
    """
    # Costruisce il percorso della cartella TEST_nome
    test_folder_path = os.path.join(base_path, f"TEST_{name}")
    
    # Percorsi delle sottocartelle
    src_folder_path = os.path.join(test_folder_path, "src")
    test_folder_sub = os.path.join(test_folder_path, "test")

    # Verifica se la cartella TEST_nome esiste già
    if os.path.exists(test_folder_path):
        print(f"⚠️ La cartella '{test_folder_path}' esiste già. Nessuna azione necessaria.")
    else:
        try:
            # Creazione delle cartelle
            os.makedirs(src_folder_path)
            os.makedirs(test_folder_sub)
            print(f"✅ Cartella '{test_folder_path}' creata con successo!")
            print(f"   ├── src/")
            print(f"   └── test/")
        except Exception as e:
            print(f"❌ Errore nella creazione delle cartelle: {e}")



def setup_project_structure(base_folder, name):
    """
    Crea una cartella 'TEST_nome' e le sottocartelle 'src' e 'test'.
    Se 'src' è vuota, crea i file '<nome>.c' e '<nome>.h'.
    Se 'test' è vuota, crea il file 'test_<nome>.c'.

    :param base_folder: Percorso in cui creare la cartella TEST_nome
    :param name: Nome base per i file da creare
    """
    # Creazione del percorso principale TEST_nome
    test_folder_path = os.path.join(base_folder, f"TEST_{name}")

    # Definizione dei percorsi per src e test
    src_folder = os.path.join(test_folder_path, "src")
    test_folder = os.path.join(test_folder_path, "test")

    # Creazione della cartella principale TEST_nome se non esiste
    if not os.path.exists(test_folder_path):
        os.makedirs(test_folder_path)
        print(f"📁 Creata la cartella: {test_folder_path}")

    # Creazione delle sottocartelle src e test se non esistono
    os.makedirs(src_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # Percorsi dei file da creare in src
    c_file_path = os.path.join(src_folder, f"{name}.c")
    h_file_path = os.path.join(src_folder, f"{name}.h")

    # Percorso del file da creare in test
    test_c_file_path = os.path.join(test_folder, f"test_{name}.c")

    # Creazione dei file in src se la cartella è vuota
    if not os.listdir(src_folder):
        with open(c_file_path, "w", encoding="utf-8") as c_file:
            c_file.write(f'#include "{name}.h"\n\n/*Do not enter any characters below this string*/ \n /* FUNCTION TO TEST */')
        with open(h_file_path, "w", encoding="utf-8") as h_file:
            h_file.write(f"#ifndef {name.upper()}_H\n#define {name.upper()}_H\n\n// Dichiarazioni delle funzioni\n\n#endif\n")
        print(f"✅ Creati {c_file_path} e {h_file_path}")

    # Creazione del file in test se la cartella è vuota
    if not os.listdir(test_folder):
        with open(test_c_file_path, "w", encoding="utf-8") as test_file:
            test_file.write(f'#include "{name}.h"\n\n// Test della funzione\n\n')
        print(f"✅ Creato {test_c_file_path}")


def modify_file_after_marker(file_path, new_content):
    """
    Apre un file, rimuove tutto il contenuto dopo la stringa '/* INSERTE THE FUNCTION HERE */'
    e inserisce una nuova stringa dopo di essa.

    :param file_path: Percorso del file da modificare
    :param new_content: Testo da inserire dopo la stringa di riferimento
    """
    try:
        # Legge il contenuto del file
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Trova la posizione della stringa target
        marker = "/* Do not enter any characters below this string */"
        marker_index = content.find(marker)

        if marker_index == -1:
            print("⚠️ La stringa di riferimento non è stata trovata nel file.")
            return

        # Mantiene solo la parte del file fino alla stringa target e aggiunge il nuovo contenuto
        modified_content = content[:marker_index + len(marker)] + "\n" + new_content + "\n"

        # Scrive il file aggiornato
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(modified_content)

        print(f"✅ Il file '{file_path}' è stato aggiornato con successo.")

    except FileNotFoundError:
        print(f"❌ Errore: Il file '{file_path}' non esiste.")
    except Exception as e:
        print(f"❌ Errore durante la modifica del file: {e}")

   


# ESEMPIO DI UTILIZZO



# Stampa della struttura
for modulo in moduli:
    module_name = modulo['nome_modulo'] 
    function_name =  modulo['nome_funzione'] 
    base_directory = modulo['percorso'] 
    extracted_body =find_and_extract_function(module_name,function_name)


    setup_project_structure(base_directory, function_name)

    modify_file_after_marker(base_directory+"/TEST_"+function_name+"/src/"+function_name+".c",extracted_body)
    if extracted_body:
        print("\n🔹 Corpo della funzione trovata:\n")
        print(extracted_body)
        
        
        










