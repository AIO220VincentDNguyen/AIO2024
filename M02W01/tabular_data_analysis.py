import pandas as pd
import numpy as np
df = pd.read_csv('/content/drive/MyDrive/advertising.csv')
data = df.to_numpy()

# question 15
max_value_15 = df['Sales'].max()
max_index_15 = df['Sales'].idxmax()

print(max_value_15, max_index_15)

# question 16
avg_tv_col = df['TV'].mean()
print(avg_tv_col)

# question 17
count_sale_col_20 = df['Sales'][df['Sales'] >= 20].count()
print(count_sale_col_20)

# question 18
avg_radio_sale_15 = df['Radio'][df['Sales'] >= 15].mean()
print(avg_radio_sale_15)

# question 19
total_sales_where_newspaper_above_avg = df[df['Newspaper'] > df['Newspaper'].mean()]['Sales'].sum()
print(total_sales_where_newspaper_above_avg)

# question 20
A = df['Sales'].mean() # Calculate the mean of the 'Sales' column
scores = ['Good' if x > A else 'Average' if x == A else 'Bad' for x in df['Sales']] # Create a new list 'scores' with 'Good', 'Average', 'Bad' based on the condition
print(scores[7:10])

# question 21
closest_to_mean = df.iloc[(df['Sales'] - mean_sales).abs().argsort()[:1]] # Find the value in 'Sales' closest to the mean
A = closest_to_mean['Sales'].values[0] # Get the Sales value closest to the mean
scores = ['Good' if x > A else 'Average' if x == A else 'Bad' for x in df['Sales']] # Create a new list 'scores' with 'Good', 'Average', 'Bad' based on the condition
print(scores[7:10])