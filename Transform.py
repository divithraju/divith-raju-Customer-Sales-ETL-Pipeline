import pandas as pd
import os

def transform_data():
    # Step 1: Load the extracted data
    data_path = '/home/divithraju/Downloads/salesdata/combined_sales.csv'
    df = pd.read_csv(data_path)

    # Step 2: Handle missing values
    df['Sales Amount'] = df['Sales Amount'].fillna(0)
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df = df.dropna(subset=['Order Date'])  # Remove rows where Order Date could not be parsed

    # Step 3: Standardize data formats
    df['Sales Amount'] = df['Sales Amount'].astype(float)
    df['Customer Name'] = df['Customer Name'].str.title()
    df['Region'] = df['Region'].str.upper()

    # Step 4: Feature Engineering - Adding new calculated columns
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    df['Week'] = df['Order Date'].dt.isocalendar().week

    # Step 5: Aggregation - Sales by Region, Product Category, and Month
    region_sales = df.groupby(['Region', 'Product Category', 'Month'])['Sales Amount'].sum().reset_index()

    # Save the transformed data
    output_path = '/home/divithraju/Downloads/salesdata/transformed_region_sales.csv'
    region_sales.to_csv(output_path, index=False)

    print(f"Data transformation completed and saved at: {output_path}")

if __name__ == "__main__":
    transform_data()
