
import pandas as pd

df = pd.read_csv("data/pokemon_data.csv", delimiter="\t")
df_xlsx = pd.read_excel("data/pokemon_data.xlsx")

print(df.head(3)) # Display the first 3 rows of the DataFrame

print(df.columns) # Display the column names

print(df["Name"][0:5]) # Display the first 5 names in the "Name" column
print(df.name)
print(df[["Name", "Type 1", "HP"]][0:5]) # Display the first 5 rows of the "Name", "Type 1", and "HP" columns
print(df.iloc[0:5]) # Display the first 5 rows of the DataFrame using iloc
print(df.iloc[2, 1]) # Display the value at row index 2 and column index 1

for index, row in df.iterrows(): # Iterate through each row
    print(index, row["Name"])  # Print the index and the "Name" of each row

df.loc[df["Type 1"] == "Fire", "Type 1"] = "Flamer"  # Change "Fire" to "Flamer" in the "Type 1" column
print(df.describe())  # Display summary statistics of the DataFrame

df.sort_values(["Type 1", "HP"], ascending= [1,0])  # Sort the DataFrame by "Type 1" and "HP" in ascending order for "Type 1" and descending for "HP"

df["Total"] = df["HP"] + df["Attack"] + df["Defense"] + df["Sp. Atk"] + df["Sp. Def"] + df["Speed"]  # Create a new column "Total" as the sum of specified columns

df.drop(columns=["Total"])  # Drop the "Total" column from the DataFrame
df["Total"] = df.iloc[:, 4:10].sum(axis=1)  # Create "Total" column as the sum of columns from index 4 to 9

cols = list(df.columns.values)  # Get the list of column names
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]  # Reorder columns to move "Total" to the second position
df[["Total", "HP", "Defense"]]


df.to_csv("data/pokemon_data_modified.csv", index=False)  # Save the modified DataFrame to a new CSV file without the index
df.to_excel("data/pokemon_data_modified.xlsx")  # Save the modified DataFrame to a new Excel file
df.to_csv("data/pokemon_data_modified.txt", sep="\t", index=False)  # Save the modified DataFrame to a tab-separated text file without the index

new_df = df.loc[(df["Type 1"] == "Grass") & (df["Type 2"] == "Poison") & ["HP"] > 70]  # Filter rows where "Type 1" is "Grass" and "Type 2" is "Poison"
print(new_df)

new_df.to_csv("filtered.csv")

new_df = new_df.reset_index(drop=True, inplace= True)  # Reset the index of the filtered DataFrame

import re
df.loc[df["Name"].str.contains("Mega")]  # Filter rows where "Name" contains "Mega"
df.loc[df["Type 1"].str.contains("fire|grass", flags=re.I, regex=True)]  # Filter rows where "Name" contains "fire" or "grass", case-insensitive
df.loc[df["Name"].str.contains("^pi[a-z]*", flags=re.I, regex=True)]  # Filter rows where "Name" starts with "pi" followed by any lowercase letters

df.loc[df["Total"] > 500, ["Generation", "Legendary"]] = ["Test 1", "Test 2"] 


df = pd.read_csv("data/pokemon_data_modified.csv") 

df.groupby(["Type 1"]).mean().sort_values("HP", ascending=False)  # Group by "Type 1" and calculate the mean of each group, sorted by "HP"
df["count"] = 1  # Add a new column "count" with value 1
df.groupby(["Type 1", "Type 2"]).count()["count"]


new_df = pd.DataFrame(columns=df.columns)  # Create an empty DataFrame with the same columns as df
for df in pd.read_csv("data/pokemon_data_modified.csv", chunksize=5):  # Read the CSV file in chunks of 5 rows
    results = df.groupby(["Type 1"]).count()  # Group by "Type 1" and count the occurrences
    new_df = pd.concat([new_df, results])  # Concatenate the results to the new DataFrame
