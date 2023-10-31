import pandas as pd
import numpy as np

# Read the Excel file into a DataFrame
df = pd.read_excel('Line Production September 2023.xlsx')

# Create a filtered DataFrame without the excluded columns
filtered_df = df.drop(columns=["Product", "deadline", "penalty cost"])

# Calculate the orderScore and add it to the filtered DataFrame
filtered_df['orderScore'] = df['deadline'] / df['penalty cost']

# Sort the DataFrame by "orderScore" in ascending order
filtered_df = filtered_df.sort_values(by='orderScore', ascending=True)

products = []
for i in range(1, len(df) + 1):
    products.append(i)

deadline = df["deadline"]
penaltyCost = df["penalty cost"]

print(filtered_df)



# Convert the filtered DataFrame to a NumPy matrix
processingTimes = filtered_df.to_numpy()
chosenline= np.zeros((len(products),7))

startTime = 0
currentTime = 0

for coordinate, value in np.ndenumerate(processingTimes):
    print("a")


Line1 = []
Line2 = []
Line3 = []
Line4 = []
Line5 = []
Line6 = []
Line7 = []



























    



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