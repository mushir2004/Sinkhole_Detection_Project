import pandas as pd
import os

# Update 'Session_1' and '1.csv' if your extracted PVS files have different names!
file_path = os.path.join("Data", "Raw_Data", "PVS 1", "dataset_labels.csv") 

print(f"Attempting to read file at: {file_path}\n")

try:
    # Load the CSV file
    df = pd.read_csv(file_path)
    
    print("✅ SUCCESS! The file was loaded.\n")
    print("-" * 40)
    print("FIRST 5 ROWS:")
    print("-" * 40)
    print(df.head())
    
    print("\n" + "-" * 40)
    print("COLUMN NAMES (Features):")
    print("-" * 40)
    
    # Print out all column names so we know exactly what to filter next
    for col in df.columns:
        print(f"- {col}")
        
except FileNotFoundError:
    print("❌ ERROR: Could not find the file.")
    print("Please check that your folder names exactly match the file_path variable.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")