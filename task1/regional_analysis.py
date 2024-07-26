import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'SalesForCourse_quizz_table.xlsx'
df = pd.read_excel(file_path)
df.rename(columns={'quantity': 'Quantity', 'country': 'Country', 'state': 'State'}, inplace=True)


quantity_by_region = df.groupby(['Country', 'State'])['Quantity'].sum().reset_index()


filtered_quantity_by_region = quantity_by_region[quantity_by_region['Quantity'] >= 2300]


plt.figure(figsize=(14, 8))
sns.barplot(data=filtered_quantity_by_region, x='State', y='Quantity', hue='Country', palette='tab10')
plt.title('Quantity Sold by Region (Filtered)')
plt.xlabel('State')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=45)
plt.legend(title='Country')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
