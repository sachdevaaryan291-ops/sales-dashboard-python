import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your local file
file_path = r"C:\Users\Amish\OneDrive\Desktop\Computed insight - Success of active sellers.csv"
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace(r'[^\w]', '', regex=True)

# Set style
sns.set(style="whitegrid")

# Plot 1: Top 10 Merchants by Total Units Sold
plt.figure(figsize=(10, 5))
top_units = df.sort_values(by="totalunitssold", ascending=False).head(10)
sns.barplot(data=top_units, x="merchantid", y="totalunitssold", palette="crest")
plt.title("Top 10 Merchants by Total Units Sold")
plt.xlabel("Merchant ID")
plt.ylabel("Total Units Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 2: Top 10 Merchants by Rating
plt.figure(figsize=(10, 5))
top_rating = df.sort_values(by="rating", ascending=False).head(10)
sns.barplot(data=top_rating, x="merchantid", y="rating", palette="viridis")
plt.title("Top 10 Merchants by Rating")
plt.xlabel("Merchant ID")
plt.ylabel("Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot 3: Distribution of Mean Product Prices
plt.figure(figsize=(8, 5))
sns.histplot(df["meanproductprices"], kde=True, bins=20, color="orange")
plt.title("Distribution of Mean Product Prices")
plt.xlabel("Mean Product Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Plot 4: Urgency Text Rate vs Total Urgency Count
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="totalurgencycount", y="urgencytextrate", hue="rating", palette="cool", s=80)
plt.title("Urgency Text Rate vs Total Urgency Count")
plt.xlabel("Total Urgency Count")
plt.ylabel("Urgency Text Rate")
plt.tight_layout()
plt.show()
