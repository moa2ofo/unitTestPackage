# Project: C File Extraction and Organization Tool

## Overview
This Python script automates the process of:
- Searching for specific C source files and functions within a directory and its subdirectories.
- Extracting function definitions, return types, and bodies from the located files.
- Creating a structured test environment for each extracted function.
- Copying `.c` and `.h` files while excluding specific Unity and CMock-related files.
- Modifying test source files to insert extracted function implementations.

## Features
- **Recursive File Search**: Automatically scans directories for the specified C files.
- **Function Extraction**: Finds function definitions, including their return types and bodies.
- **Automated Directory and File Creation**: Creates structured test folders (`TEST_<function_name>`) with `src/` and `test/` subdirectories.
- **Selective File Copying**: Copies only `.c` and `.h` files, excluding specified test framework files (`unity.h`, `cmock.h`, etc.).
- **Code Insertion into Test Files**: Replaces a specific marker (`/* Do not enter any characters below this string */`) in the test source files with the extracted function body.
- **Folder Structure Visualization**: Prints the directory tree while identifying `TEST_` folders and their relevant files.

## Installation
1. Ensure you have Python 3 installed.
2. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/c-file-extraction-tool.git
   cd c-file-extraction-tool
   ```
3. Install required dependencies (if any):
   ```sh
   pip install -r requirements.txt  # If additional dependencies exist
   ```

## Usage
To execute the script, run:
```sh
python script.py
```

### Parameters:
The script processes a predefined set of modules:
```python
moduli = [
    {"nome_modulo": "VoltMon.c", "nome_funzione": "VoltMon_Run", "percorso": PATH},
    {"nome_modulo": "SpeedMon.c", "nome_funzione": "SpeedMon_Run", "percorso": PATH},
    {"nome_modulo": "CurrentMon.c", "nome_funzione": "CurrentMon_Derating", "percorso": PATH},
    {"nome_modulo": "LinStub.c", "nome_funzione": "ApplLinDiagEcuReset", "percorso": PATH},
    {"nome_modulo": "BridgeCtrl.c", "nome_funzione": "OffStateHandler", "percorso": PATH}
]
```
To modify this, update the `moduli` list in the script.

## Functionality Breakdown
### 1. **Finding and Extracting Functions**
- Searches for a specified file within the directory tree.
- Extracts the function header, return type, and function body.
- Saves the extracted function details into a structured string.

### 2. **Creating Test Directories**
- Generates a test directory `TEST_<function_name>` for each function.
- Inside the directory, creates `src/` and `test/` subdirectories.
- If `src/` is empty, creates `<function_name>.c` and `<function_name>.h`.
- If `test/` is empty, creates `test_<function_name>.c`.

### 3. **Copying Files Selectively**
- Only copies `.c` and `.h` files.
- Skips `unity.h`, `unity.c`, `cmock.h`, `cmock.c`, `unity_internals.h`, `cmock_internals.h`.

### 4. **Modifying Test Source Files**
- Searches for `/* Do not enter any characters below this string */` in the test source file.
- Replaces everything after the marker with the extracted function body.

### 5. **Printing Folder Structure**
- Recursively scans the root folder and prints its tree.
- Identifies `TEST_` folders and prints full paths of matching files.

## Example Execution
```
✅ Cartella 'TEST_VoltMon_Run' creata con successo!
   ├── src/
   └── test/
✅ Creati src/VoltMon_Run.c e src/VoltMon_Run.h
✅ Creato test/test_VoltMon_Run.c
✅ Il file 'src/VoltMon_Run.c' è stato aggiornato con la funzione estratta.
📂 Scansionando '../../elop_048' e copiando file .c e .h → '../../elop_048/tests/runnableAllTest'
🔍 Found matching file: VoltMon_Run.h in /elop_048/platform/basic_sw_platform/monitoring/test
```

## Contributing
If you wish to contribute:
1. Fork this repository.
2. Create a feature branch: `git checkout -b feature-new-functionality`.
3. Commit your changes: `git commit -m "Added new feature"`.
4. Push to your branch: `git push origin feature-new-functionality`.
5. Open a pull request.

## License
This project is licensed under the MIT License. See `LICENSE` for details.

## Contact
For any inquiries or issues, please open an issue on GitHub or contact the author.

---
🚀 Happy Coding! 🚀


