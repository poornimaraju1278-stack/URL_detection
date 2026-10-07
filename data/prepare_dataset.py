import pandas as pd
import sys

# Allow Python to find feature_extraction.py inside src
sys.path.insert(0, "src")

from feature_extraction import extract_features, FEATURE_COLUMNS


# Input and output files
INPUT_FILE = "data/PhiUSIIL_Phishing_URL_Dataset.csv"
OUTPUT_FILE = "data/processed_features.csv"


print("Loading dataset...")

df = pd.read_csv(INPUT_FILE)

print(f"Dataset loaded: {len(df)} rows")


# Extract the 11 required URL features
print("Extracting URL features...")

features = df["URL"].apply(extract_features)

feature_df = pd.DataFrame(features.tolist())


# Keep the required feature order
feature_df = feature_df[FEATURE_COLUMNS]


# Add the original label
feature_df["label"] = df["label"].astype(int)


# Save processed dataset
feature_df.to_csv(OUTPUT_FILE, index=False)


print("Feature extraction completed!")
print(f"Processed dataset saved to: {OUTPUT_FILE}")

print("\nProcessed dataset shape:")
print(feature_df.shape)

print("\nFeature columns:")
print(feature_df.columns.tolist())

print("\nLabel counts:")
print(feature_df["label"].value_counts())