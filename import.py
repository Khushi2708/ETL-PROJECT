import pandas as pd

import dateutil
import six


# Example of creating final_df
final_df = pd.read_csv('SampleSuperstore.csv')  # Replace with your actual data source or transformation


# Step 1: Extract Data from CSV files
SampleSuperstore_df = pd.read_csv('SampleSuperstore.csv')  # Load FIRST data

# Display the extracted data to verify
print(SampleSuperstore_df.head()) 

# Step 2: Transform Data

# 1. Clean the sales data by removing duplicates
SampleSuperstore_df_clean = SampleSuperstore_df.drop_duplicates()


from sqlalchemy import create_engine

# Step 3: Load Transformed Data into a Database

# Create a SQLite database connection
engine = create_engine('sqlite:///etl_project.db', echo=True)

# Load the final transformed data into the database
final_df.to_sql('SampleSuperstore_data', con=engine, if_exists='replace', index=False) # type: ignore

print("Data successfully loaded into the database!")

# Step 4: Verify Data Loaded in the Database

# Query the database to check the loaded data
query = "SELECT * FROM SampleSuperstore_data"
loaded_data = pd.read_sql(query, con=engine)

# Display the loaded data
print(loaded_data.head())


