import os
import requests as rq
import pandas as pd
from tqdm import tqdm

# Fetch the list of all mutual funds
try:
    response = rq.get("https://api.mfapi.in/mf")
    response.raise_for_status()  # Check if the request was successful
    all_mf = response.json()

    if not isinstance(all_mf, list) or len(all_mf) == 0:
        raise ValueError("API response does not contain a valid list of mutual funds.")
    
except (rq.RequestException, ValueError) as e:
    print(f"Error fetching mutual fund data: {e}")
    exit(1)  # Exit the script if there's an error

# Define the folder name where you want to save the files
folder_name = "mf_data"

# Create the folder if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Loop through the list of mutual funds and save each to a CSV file in the folder
for mf_sample in tqdm(all_mf):
    mf_code = mf_sample["schemeCode"]
    mf_name = mf_sample["schemeName"]
    mf_data = rq.get(f"https://api.mfapi.in/mf/{mf_code}").json()
    
    # Save the data to the specified folder
    pd.DataFrame(mf_data["data"]).to_csv(f"./{folder_name}/{mf_code}.csv", index=False)
