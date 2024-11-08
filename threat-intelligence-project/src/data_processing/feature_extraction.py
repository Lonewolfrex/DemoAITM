 
import pandas as pd

def extract_features(df):
    # Example feature extraction logic
    df['length'] = df['description'].apply(len)  # Add length of description as a feature
    return df[['type', 'length']]  # Return relevant features

if __name__ == "__main__":
    processed_data_path = "../data/processed/processed_threat_data.csv"
    df = pd.read_csv(processed_data_path)
    features_df = extract_features(df)
    features_df.to_csv("../data/processed/features.csv", index=False)