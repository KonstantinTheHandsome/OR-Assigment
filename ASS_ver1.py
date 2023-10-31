import pandas as pd
import numpy as np

df = pd.read_excel('Line Production September 2023.xlsx')

products = []
for i in range(1, len(df) + 1):
    products.append(i)

deadline = df["deadline"]
penaltyCost = df["penalty cost"]



# dictionary maybe
# Create a filtered DataFrame without the excluded columns
filtered_df = df.drop(columns=(["Product", "deadline", "penalty cost"]))
# Convert the filtered DataFrame to a NumPy matrix
processingTimes = filtered_df.to_numpy()













data = {
    'Product': [0],
    'Line': [0],
    'Process Time': [0],
    'End': [0],
    'Deadline': [0],
    'Tardiness': [0],
    'Total Penalty Cost': [0]
}

df1 = pd.DataFrame(data)

df1.to_excel('Solution.xlsx')