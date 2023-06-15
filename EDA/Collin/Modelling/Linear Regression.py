# Import libraries

from sklearn.linear_model import LinearRegression
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

# Identify absolute file path
directory = os.path.dirname(os.path.abspath(__file__))

# Identify relative file path
merged = os.path.join(directory, "Datasets/Merged.csv")

# Load data
merged = pd.read_csv(merged)

# Create a key to translate income values to income brackets
incomekey = {None: "No data", 1: "€21,100 to €30,300", 2: "€30,300 to €42,800", 3: "€42,800 to €59,800", 4: "€59,800 +"}

# Linear regression
merged = merged.dropna(subset = ["Income Index"])
merged = merged.drop_duplicates(subset = ["Income Index", "Average Green Score"])

regression_model = LinearRegression()

X = merged["Income Index"].values.reshape(-1, 1)
y = merged["Average Green Score"].values.reshape(-1, 1)

regression_model.fit(X, y)
predicted_scores = regression_model.predict(X)

# Display "Average Income" by neighborhood in a chloropleth map plot

# Configure the outlier threshold
threshold = merged["Average Green Score"].quantile(0.6)
filtered = merged[merged["Average Green Score"] < threshold]

# Calculate the correlation between "Income Index" and "Average Green Score"
correlation = filtered["Income Index"].corr(filtered["Average Green Score"])

fig, ax = plt.subplots(figsize = (8, 6))

sns.scatterplot(
    data = filtered,
    x = "Income Index",
    y = "Average Green Score",
    ax = ax)

plt.plot(
    X,
    predicted_scores,
    color = "r",
    linewidth = 2,
    label = "Regression Line")

# Remove axis labels
ax.set_xlabel("")
ax.set_ylabel("")

# Convert x-axis income values to income brackets
ax.xaxis.set_major_locator(ticker.MaxNLocator(integer = True))
ax.set_xticklabels([incomekey.get(int(x), x) for x in ax.get_xticks()])

# Convert y-axis values to percentages
ax.yaxis.set_major_formatter(ticker.PercentFormatter(decimals = 0))

# Display the plot with correlation
ax.set_title(f"Correlation: {correlation:.2f}")
plt.show()