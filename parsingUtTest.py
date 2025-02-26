# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:37:13 2025

@author: moa2ofo
"""

import os
import re
import sys
import shutil


# Lista dei file da escludere dalla copia
EXCLUDED_FILES = {"unity.h", "unity.c", "cmock.c", "cmock.h", "unity_internals.h", "cmock_internals.h"}
# ==============================
# CONFIGURATION & MODULE LIST
# ==============================
moduli = [
    {"nome_modulo": "LinStub.c", "nome_funzione": "ApplLinDiagReadDataByAddress", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "ApplLinDiagSessionControl", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "RdbiCalibrationVerificationNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "WdbiEcuHwPartNumberId_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "WdbiEcuPartNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "ApplLinDiagEcuReset", "percorso": "../../elop_048/product/lin_drv/LinStub_test"}, 
    {"nome_modulo": "LinStub.c", "nome_funzione": "ApplLinDiagReadDataById", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "ApplLinDiagWriteDataById", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},    
    {"nome_modulo": "LinStub.c", "nome_funzione": "WdbiEcuManufactoringDate_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "WdbiEcuSerialNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "WdbiVhitSerialNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "WdbiEcuPartNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "WdbiEcuHwPartNumberId_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "WdbiSystemSupplierEcuHardwareNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "WdbiSystemSupplierEcuHardwareVersionNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "WdbiSupplierSerialNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "RdbiCalibrationVerificationNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "RdbiCurrentDiagApp_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "RdbiEcuPartNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "RdbiActiveDiagnosticSession_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "RdbiEcuManufactoringDate_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "RdbiSupplierSerialNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "RdbiSupplierSerialNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "RdbiSystemSupplierEcuHardwareNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "RdbiSystemSupplierEcuHardwareVersionNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "RdbiSystemSupplierEcuSoftwareNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "RdbiVmSystemNameOrEngineType_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "RdbiSwNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "RdbiSerialNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "RdbiEcuHwPartNumberId_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "RdbiVhitActualStatusDiag_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    {"nome_modulo": "LinStub.c", "nome_funzione": "ApplLinDiagRoutineControl", "percorso": "../../elop_048/product/lin_drv/LinStub_test"},
    


{"nome_modulo": "LinStub.c", "nome_funzione": "WdbiSupplierSerialNumber_", "percorso": "../../elop_048/product/lin_drv/LinStub_test"}, 
]

def copy_c_h_files(source_folder, destination_folder):
    """
    Cerca le cartelle 'test' e 'src' nella cartella sorgente e copia solo i file .c e .h
    (escludendo specifici file) nella cartella di destinazione, organizzandoli in 'src' e 'test'.

    :param source_folder: Cartella sorgente in cui cercare 'test' e 'src'
    :param destination_folder: Cartella di destinazione in cui copiare i file
    """
    # Percorsi di destinazione
    dest_test = os.path.join(destination_folder, "test")
    dest_src = os.path.join(destination_folder, "src")
    

    # Creare le cartelle di destinazione se non esistono
    os.makedirs(dest_test, exist_ok=True)
    os.makedirs(dest_src, exist_ok=True)

    # Scandire la cartella sorgente
    for root, dirs, files in os.walk(source_folder):
        for dir_name in dirs:
            if dir_name in ["test", "src"]:
                src_path = os.path.join(root, dir_name)
                dest_path = dest_test if dir_name == "test" else dest_src

                print(f"📂 Scansionando '{src_path}' e copiando file .c e .h → '{dest_path}'")
                copy_c_h_files_from_folder(src_path, dest_path)

def copy_c_h_files_from_folder(src_folder, dest_folder):
    """
    Copia solo i file .c e .h (escludendo alcuni file specifici) da una cartella sorgente a una cartella di destinazione.

    :param src_folder: Cartella sorgente
    :param dest_folder: Cartella di destinazione
    """
    for item in os.listdir(src_folder):
        src_path = os.path.join(src_folder, item)
        dest_path = os.path.join(dest_folder, item)

        # Controlla se è un file .c o .h e non è tra quelli esclusi
        if os.path.isfile(src_path) and item.endswith((".c", ".h")) and item not in EXCLUDED_FILES:
            print(f"    📄 Copiando {item} → {dest_folder}")
            shutil.copy2(src_path, dest_path)



def print_folder_tree(start_path, indent=""):
    """
    Recursively prints the folder tree structure of a given directory.
    Additionally, detects and prints the full path of any folder starting with "TEST_",
    extracts its name, and searches for files inside that folder and its subfolders that start with the extracted name.

    :param start_path: Root directory to start the tree print
    :param indent: Indentation for subdirectories
    """
    try:
        items = sorted(os.listdir(start_path))  # Sort items for consistent order
    except PermissionError:
        print(f"{indent}[ACCESS DENIED] {start_path}")
        return

    for i, item in enumerate(items):
        item_path = os.path.join(start_path, item)
        is_last = (i == len(items) - 1)


        # Check if the folder name starts with "TEST_"
        if os.path.isdir(item_path) and item.startswith("TEST_"):
            folder_name = item[5:]  # Extract the part after "TEST_"
            print(f"  📂 Found TEST folder: {os.path.abspath(item_path)} (Searching for '{folder_name}_' files...)")

            # Search for files inside this folder and all subfolders
            search_files_in_folder_recursive(item_path, folder_name)

        # Recursively print subdirectories
        if os.path.isdir(item_path):
            new_indent = indent + ("    " if is_last else "│   ")
            print_folder_tree(item_path, new_indent)

def search_files_in_folder_recursive(folder_path, search_prefix):
    """
    Searches recursively inside a given folder and its subfolders for files that start with a specific prefix.

    :param folder_path: Path of the folder to search in
    :param search_prefix: Prefix to match filenames against
    
    """
    copy_c_h_files(folder_path,"../../elop_048/tests/runnableAllTest")
    try:
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.startswith(search_prefix+".h"):
                    print(f"    🔍 Found matching file: {file} in {root}")
    except PermissionError:
        print(f"    [ACCESS DENIED] Cannot read {folder_path}")



# ==============================
# FUNCTION EXTRACTION
# ==============================
def find_and_extract_function(file_name, function_name):
    """
    Searches for a file in a directory and its subdirectories, extracts a function,
    its body, and its return type.
    """
    directory = "../../elop_048"
    file_path = None

    for root, _, files in os.walk(directory):
        if file_name in files:
            file_path = os.path.join(root, file_name)
            break

    if not file_path:
        return f"❌ Error: File '{file_name}' not found in directory '{directory}'."

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        function_pattern = re.compile(rf"(\w+\s+\*?{function_name}\s*\([^)]*\))\s*\{{", re.MULTILINE)
        match = function_pattern.search(content)

        if not match:
            return f"⚠️ Function '{function_name}' not found in '{file_name}'."

        start_index = match.start()
        function_header = match.group(1)
        return_type = function_header.split(function_name)[0].strip()

        open_braces = 0
        function_body = ""

        for i in range(start_index, len(content)):
            char = content[i]
            function_body += char

            if char == "{":
                open_braces += 1
            elif char == "}":
                open_braces -= 1
                if open_braces == 0:
                    break

        return f"\n\n{function_body}"

    except Exception as e:
        return f"❌ Error reading file: {e}"

# ==============================
# PROJECT STRUCTURE SETUP
# ==============================
def setup_project_structure(base_folder, name):
    """
    Creates a 'TEST_<name>' directory with 'src' and 'test' subdirectories.
    """
    test_folder_path = os.path.join(base_folder, f"TEST_{name}")
    src_folder = os.path.join(test_folder_path, "src")
    test_folder = os.path.join(test_folder_path, "test")
    
    os.makedirs(src_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)
    
    c_file_path = os.path.join(src_folder, f"{name}.c")
    h_file_path = os.path.join(src_folder, f"{name}.h")
    test_c_file_path = os.path.join(test_folder, f"test_{name}.c")

    if not os.listdir(src_folder):
        with open(c_file_path, "w", encoding="utf-8") as c_file:
            c_file.write(f'#include "{name}.h"\n\n/* FUNCTION TO TEST */')
        with open(h_file_path, "w", encoding="utf-8") as h_file:
            h_file.write(f"#ifndef {name.upper()}_H\n#define {name.upper()}_H\n\n#endif\n")
        print(f"✅ Created {c_file_path} and {h_file_path}")
    
    if not os.listdir(test_folder):
        with open(test_c_file_path, "w", encoding="utf-8") as test_file:
            test_file.write(f'#include "{name}.h"\n\n// Test function\n\n')
        print(f"✅ Created {test_c_file_path}")

# ==============================
# MODIFY FILE AFTER MARKER
# ==============================
def modify_file_after_marker(file_path, new_content):
    """
    Replaces content in the file after a specific marker.
    """
    marker = "/* FUNCTION TO TEST */"
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        marker_index = content.find(marker)
        if marker_index == -1:
            print("⚠️ Marker not found in file.")
            return
        
        modified_content = content[:marker_index + len(marker)] + "\n" + new_content + "\n"
        
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(modified_content)
        print(f"✅ File '{file_path}' successfully updated.")
    except FileNotFoundError:
        print(f"❌ Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"❌ Error modifying file: {e}")
# ==============================
# DELETE PREVIOUS SRC AND TEST FOLDERS
# ==============================
def delete_previous_content():
    """
        delete the previous files inner the folder
    """
    destination_folder="../../elop_048/tests/runnableAllTest"
    # Percorsi di destinazione
    dest_test = os.path.join(destination_folder, "test")
    dest_src = os.path.join(destination_folder, "src")

    # Se le cartelle di destinazione esistono, eliminarle
    for dest in [dest_test, dest_src]:
        if os.path.exists(dest):
            shutil.rmtree(dest) 
            
def extract_static_functions(c_code):
    # Cerca le funzioni static, assumendo che la graffa aperta "{" sia sulla stessa riga
    pattern = re.compile(r'^\s*static\s+([\w\s\*\[\]]+?)\s+(\w+)\s*\(([^)]*)\)\s*\{', re.MULTILINE)
    functions = []
    for match in pattern.finditer(c_code):
        ret_type = match.group(1).strip()
        func_name = match.group(2).strip()
        params = match.group(3).strip()
        functions.append((ret_type, func_name, params))
    return functions

def parse_function_definitions(file_path):
    function_pattern = re.compile(
        r'(?P<ret_type>\w[\w\s\*]+?)\s+'  # Tipo di ritorno
        r'(?P<func_name>\w+)\s*'  # Nome funzione
        r'\((?P<params>[^)]*)\)\s*;'  # Parametri tra parentesi
    )
    
    functions = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            if i >= 190:
                break
            match = function_pattern.match(line.strip())
            if match:
                ret_type = match.group('ret_type').strip()
                func_name = match.group('func_name').strip()
                params = match.group('params').strip()
                functions.append((ret_type, func_name, params))
    
    return functions


def aggiorna_file(file_path):
    with open("../../elop_048/product/lin_drv/app/LinStub.c", 'r', encoding='utf-8') as f:
        c_code = f.read()
    static_functions = extract_static_functions(c_code)
   # with open("../../elop_048/platform/basic_sw_platform/lin_drv/core/inc/LinDiag.h", 'r', encoding='utf-8') as f:
    #    LinDiag = f.read()
    LinDiagDefFunctions = parse_function_definitions("../../elop_048/platform/basic_sw_platform/lin_drv/core/inc/LinDiag.h")
    marker = "/*NOT USER DEFINED*/"
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            contenuto = f.read()
    except Exception as e:
        print(f"Errore nell'apertura del file: {e}")
        sys.exit(1)

    pos = contenuto.find(marker)
    if pos == -1:
        print("Il marker non è stato trovato nel file.")
        sys.exit(1)
    
    # Conserva il contenuto fino alla fine del marker
    nuovo_contenuto = contenuto[:pos + len(marker)]
    
    # Aggiunge una nuova riga e poi la lista (ogni elemento in una nuova riga)
    for ret_type, func_name, params in static_functions:
        nuovo_contenuto += "\n" + f"{ret_type} {func_name}({params});\n"
    for ret_type, func_name, params in LinDiagDefFunctions:
        nuovo_contenuto += "\n" + f"{ret_type} {func_name}({params});\n"
        
        

    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(nuovo_contenuto)
    except Exception as e:
        print(f"Errore nella scrittura del file: {e}")
        sys.exit(1)
    
    print("File aggiornato con successo.")

def fileManager( output_file):
    with open("../../elop_048/product/lin_drv/app/LinStub.c", 'r', encoding='utf-8') as f:
        c_code = f.read()
    static_functions = extract_static_functions(c_code)

    with open(output_file, 'w', encoding='utf-8') as f:
        for ret_type, func_name, params in static_functions:
            f.write(f"{ret_type} {func_name}({params});\n")
# ==============================
# MAIN EXECUTION
# ==============================
if __name__ == "__main__":
    delete_previous_content()
    aggiorna_file("../../elop_048/product/lin_drv/LinStub_test/TEST_ApplLinDiagReadDataById/src/LinStub.h") 
    for modulo in moduli:
        module_name = modulo['nome_modulo']
        function_name = modulo['nome_funzione']
        base_directory = modulo['percorso']
        
        extracted_body = find_and_extract_function(module_name, function_name)
        if extracted_body:
            setup_project_structure(base_directory, function_name)
            modify_file_after_marker(os.path.join(base_directory, f"TEST_{function_name}", "src", f"{function_name}.c"), extracted_body)
            print(f"\n🔹 Extracted function body:\n{[function_name]}")
            
    # Specify the directory to start (change as needed)
    folder_to_scan = "../../elop_048"  # Use "." for current directory or provide an absolute path
    print(f"Folder Tree of: {os.path.abspath(folder_to_scan)}\n")
    print_folder_tree(folder_to_scan) 
   
