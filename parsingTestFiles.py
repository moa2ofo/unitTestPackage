import os
import shutil

# Lista dei file da escludere dalla copia
EXCLUDED_FILES = {"unity.h", "unity.c", "cmock.c", "cmock.h", "unity_internals.h", "cmock_internals.h"}

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

        # Format branch
        branch = "└── " if is_last else "├── "
        #print(f"{indent}{branch}{item}")

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

# Specify the directory to start (change as needed)
folder_to_scan = "../../elop_048"  # Use "." for current directory or provide an absolute path
print(f"Folder Tree of: {os.path.abspath(folder_to_scan)}\n")
print_folder_tree(folder_to_scan)







