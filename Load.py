import pandas as pd
import mysql.connector

def load_data():
    # Load the transformed data
    transformed_data_path = '/home/divithraju/Downloads/salesdata/transformed_region_sales.csv'
    df = pd.read_csv(transformed_data_path)
    
    # Establish connection to MySQL
    conn = mysql.connector.connect(
        host='localhost',
        user='divithraju',
        password='Divi#567',
        database='sales_db'
    )
    cursor = conn.cursor()

    # Create table if it does not exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS region_sales (
        region VARCHAR(255),
        product_category VARCHAR(255),
        month INT,
        total_sales FLOAT
    )
    """)

    # Insert data into the table
    for _, row in df.iterrows():
        cursor.execute("""
        INSERT INTO region_sales (region, product_category, month, total_sales) 
        VALUES (%s, %s, %s, %s)
        """, (row['Region'], row['Product Category'], row['Month'], row['Sales Amount']))

    conn.commit()
    cursor.close()
    conn.close()
    print("Data loading completed successfully.")

if __name__ == "__main__":
    load_data()
