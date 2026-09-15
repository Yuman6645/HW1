import pandas as pd
filepath = "Film_Permits_20260914.csv"
df = pd.read_csv(filepath)

# Print the first 2 rows
print(df.head(2))

# Print the first row
print(df.iloc[0])

# Print rows 10–19
print(df.iloc[10:20])

# Print column names
print(df.columns)

# Print the first 10 values of one column
print(df["Borough"].head(10))

# Print the first 10 rows of three columns
print(df[["Borough", "Category", "SubCategoryName"]].head(10))

# Question 1: How many permit records are listed in Manhattan?
manhattan_count = (df["Borough"] == "Manhattan").sum()
print(manhattan_count)

# Question 2: How many Television vs Film permit records are there?
category_counts = df.loc[df["Category"].isin(["Television", "Film"]), "Category"].value_counts(dropna=False)
print(category_counts)

# Question 3: How many Television permit records are listed in Manhattan?
television_manhattan_count = ((df["Category"] == "Television") & (df["Borough"] == "Manhattan")).sum()
print(television_manhattan_count)
