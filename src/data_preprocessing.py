import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder

RAW_DATA_PATH = 'data/raw/life_expectancy_data.csv'
PROCESSED_DATA_PATH = 'data/processed/life_expectancy_cleaned.csv'

def load_and_clean_data():
    df = pd.read_csv(RAW_DATA_PATH)
    df = df.dropna(thresh=len(df.columns) - 3)
    if 'Status' in df.columns:
        le = LabelEncoder()
        df['Status'] = le.fit_transform(df['Status'])  
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        df[col] = df[col].fillna(df[col].median())
    df = df.dropna()

    df = df.drop(columns=['Country'], errors='ignore')

    os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)
    print(f"Processed data saved to {PROCESSED_DATA_PATH}")

if __name__ == '__main__':
    load_and_clean_data()
