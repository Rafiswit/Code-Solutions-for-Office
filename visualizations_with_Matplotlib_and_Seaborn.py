import matplotlib.pyplot as plt
import seaborn as sns

# Create a line chart
plt.plot(df['date'], df['sales'])

# Create a scatter plot
sns.scatterplot(data=df, x='age', y='income', hue='gender')

# Create a bar chart
sns.barplot(data=df, x='category', y='value')

# Create a heatmap
sns.heatmap(data=df.corr(), cmap='coolwarm')
