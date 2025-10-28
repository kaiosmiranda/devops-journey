# log_parser_project

This project contains `log_parser.py`, a simple python utility desenvolved to demonstrate processing of file logs, counting metrics and exporting results to JSON format.

# functions

The `log_parser.py` performs the following tasks:
1.  **Efficient reading:** Read the file `sample.log` line by line (ensuring low memory usage).
2.  **Counting metrics:**  Calculate the total number of rows, the number of  **"ERROR"** ocurrences and the number of **"WARN"** ocurrences.
3. **Exporting JSON:** Generates a strutured report in the `report.json` file with all counts.

log_parser_project/
├── log_parser.py
├── sample.log  <-- Você deve criar/preencher este arquivo!
└── README.md

## Config and execution

To ensure the "reproducibility" of script, it is essential to follow the steps below to create and activate a virtual environment.

## 1. Required folder structure

The script expects the log file to be in the same folder:

log_parser_project/
├── log_parser.py
├── sample.log  <-- You need create and fill out this file!
└── README.md

## 2. Config of virtual enviroment (`venv`)

Run the following commands in the terminal, **from your project's source folder**

| Action | Command |
| :--- | :--- |
| **Create Enviroment** | `python3 -m venv .venv` |
| **Activate Enviroment** | `source .venv/bin/activate` |

*(If your prompt changes to `(.venv)`, the enviroment will be activated successfully)*

## 3. Script execution

After filling out the file `sample.log` and activate the virtual enviroment, execute the script:

```bash
#  Navigate to the project folder
cd log_parser_project

# Execute the script
python log_parser.py
```

## 4. Expected output

1. The terminal displayed the line count, errors and warnings.
2. A new file called `report.json` will be created in same folder with the data format struture (with `ident=4`)
