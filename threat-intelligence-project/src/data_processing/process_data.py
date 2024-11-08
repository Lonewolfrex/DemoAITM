 
import pandas as pd

def process_raw_data(file_path):
    df = pd.read_csv(file_path)
    # Clean and process data as needed
    df.dropna(inplace=True)  # Example: remove missing values
    return df

if __name__ == "__main__":
    raw_data_path = "../data/raw/threat_data_source_2.csv"
    processed_data = process_raw_data(raw_data_path)
    processed_data.to_csv("../data/processed/processed_threat_data.csv", index=False)