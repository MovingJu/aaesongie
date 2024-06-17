import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('/home/galesky/Downloads/시도_인구동태건수_및_동태율_출생_사망_혼인_이혼__20240617191039.csv')

# Print the columns to debug
print("Columns in DataFrame:", df.columns)

# Rename columns if necessary (this step assumes the first column might have a different name)
df.rename(columns={df.columns[0]: 'Region'}, inplace=True)

# Set the 'Region' column as the index
df.set_index('Region', inplace=True)

# Print the DataFrame to ensure it's correctly formatted
print(df)

# Plot the data
plt.figure(figsize=(12, 8))
for region in df.index:
    plt.plot(df.columns, df.loc[region], marker='o', label=region)

plt.title('Total Fertility Rate by Region (2010-2011)')
plt.xlabel('Year')
plt.ylabel('Total Fertility Rate')
plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()

# Save the plot as an image
plt.savefig('/mnt/data/fertility_rate_trend.png')

# Show the plot
plt.show()
