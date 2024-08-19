import pandas as pd
import os

def extract_data():
    # Path to the sales data directory
    data_dir = '/home/divithraju/Downloads/salesdata/'
    
    # List all CSV files in the directory
    all_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.csv')]
    
    # Read and combine all CSV files into a single DataFrame
    df_list = [pd.read_csv(file) for file in all_files]
    combined_df = pd.concat(df_list, ignore_index=True)
    
    # Save the combined data to a new CSV file
    output_path = '/home/divithraju/Downloads/salesdata/combined_sales.csv'
    combined_df.to_csv(output_path, index=False)
    
    print(f"Data extraction completed. Combined data saved at: {output_path}")

if __name__ == "__main__":
    extract_data()
