# Copy C and H Files

This repository contains a Python script that copies `.c` and `.h` files from the `test` and `src` subdirectories within a source folder to a destination folder. If the destination folders already exist, they will be deleted before being recreated to ensure a clean copy operation.

## Code Structure

### Main Functions

1. **`copy_c_h_files(source_folder, destination_folder)`**  
   - Deletes the destination folders if they exist.
   - Recreates the destination folders.
   - Scans the source folder to find `test` and `src` subdirectories.
   - Calls `copy_c_h_files_from_folder` to copy the files.

2. **`copy_c_h_files_from_folder(src_path, dest_path)`**  
   - Scans the specified source folder.
   - Copies only files with `.c` and `.h` extensions to the destination folder.

### Execution Flow Diagram

```
copy_c_h_files(source_folder, destination_folder)
│
├──> Delete destination folders (if they exist)
│
├──> Create new destination folders
│
├──> Scan the source folder
│   │
│   ├──> If "test" folder is found, call copy_c_h_files_from_folder(test, dest_test)
│   ├──> If "src" folder is found, call copy_c_h_files_from_folder(src, dest_src)
│
└──> copy_c_h_files_from_folder(src_path, dest_path)
    │
    ├──> Scan src_path
    ├──> Copy .c and .h files to dest_path
    └──> End
```

## Usage

To run the script, use the following command:

```sh
python script.py <source_folder> <destination_folder>
```

Where:
- `<source_folder>` is the source directory containing `test` and `src` subdirectories.
- `<destination_folder>` is the directory where the files will be copied.

### Example

If you have the following directory structure:
```
/source_folder
│── src
│   ├── main.c
│   ├── utils.c
│   ├── utils.h
│
│── test
│   ├── test_main.c
│   ├── test_utils.c
```
After running the script, the destination folder will contain:
```
/destination_folder
│── src
│   ├── main.c
│   ├── utils.c
│   ├── utils.h
│
│── test
│   ├── test_main.c
│   ├── test_utils.c
```

## Requirements

- Python 3.x
- `os` and `shutil` modules (built-in in Python)

## Author

Created by [Andrea Monti] 🚀

