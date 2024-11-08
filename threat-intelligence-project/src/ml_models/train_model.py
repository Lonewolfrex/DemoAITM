import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model(features_file):
    df = pd.read_csv(features_file)
    X = df.drop('type', axis=1)  # Features
    y = df['type']               # Target variable

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    joblib.dump(model, '../data/models/trained_model.pkl')

if __name__ == "__main__":
    features_file_path = "../data/processed/features.csv"
    train_model(features_file_path)