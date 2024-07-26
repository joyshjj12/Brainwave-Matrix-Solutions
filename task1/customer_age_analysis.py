import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'SalesForCourse_quizz_table.xlsx'
df = pd.read_excel(file_path)


df.rename(columns={'quantity': 'Quantity', 'customer_age': 'Customer Age', 'product_category': 'Product Category'}, inplace=True)


age_groups = {
    '10-20': (10, 20),
    '20-30': (20, 30),
    '30-50': (30, 50),
    '50-60': (50, 60),
    '60-70': (60, 70),
    '70-80': (70, 80)
}


age_group_data = {}
for label, (lower_bound, upper_bound) in age_groups.items():
    filtered_df = df[(df['Customer Age'] >= lower_bound) & (df['Customer Age'] < upper_bound)]
    aggregated_data = filtered_df.groupby('Product Category')['Quantity'].sum().reset_index()
    aggregated_data['Age_Group'] = label
    age_group_data[label] = aggregated_data


combined_df = pd.concat(age_group_data.values())

for label in age_groups.keys():
    print(f"\nQuantity Bought by Product Category for Age Group {label}:")
    print(age_group_data[label])

plt.figure(figsize=(14, 10))
sns.barplot(data=combined_df, x='Product Category', y='Quantity', hue='Age_Group', palette='viridis')
plt.title('Total Quantity Bought by Product Category Across Different Age Groups')
plt.xlabel('Product Category')
plt.ylabel('Total Quantity Bought')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.legend(title='Age Group')
plt.show()
