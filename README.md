# Mutual Fund Data Scraper

This Python script fetches and stores mutual fund data from the [MFAPI](https://api.mfapi.in/) as CSV files. The script retrieves a list of mutual funds and then downloads their individual data, saving each to a CSV file in a specified folder.

## Features
- Fetches mutual fund data from the MFAPI.
- Creates a directory (if it doesn't exist) to store the CSV files.
- Saves each mutual fund's data as a separate CSV file, named by its scheme code.

## Requirements
- Python 3.x
- Packages: `requests`, `pandas`, `tqdm`

## Installation
1. Install Python 3.x if not already installed.
2. Install the required Python packages by running the following command:
   ```bash
   pip install requests pandas tqdm
   ```

## How to Use
1. Clone or download this script to your local machine.
2. Run the script with Python:
   ```bash
   python scrape_mf.py
   ```
3. The script will:
   - Fetch the list of all mutual funds from `https://api.mfapi.in/mf`.
   - Save each mutual fund's data as a CSV file in a folder named `mf_data`.

## Output
The CSV files will be saved in the `mf_data` folder in the current directory. Each file is named by the mutual fund's scheme code, e.g., `12345.csv`.

## Error Handling
- The script checks for errors when fetching data from the API. If an error occurs, it will print the error message and stop the execution.


