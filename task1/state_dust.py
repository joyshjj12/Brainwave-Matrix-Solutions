# valid_french_states = [
#     'Île-de-France', 'Provence-Alpes-Côte d\'Azur', 'Auvergne-Rhône-Alpes', 
#     'Occitanie', 'Hauts-de-France', 'Bretagne', 'Normandie', 
#     'Centre-Val de Loire', 'Bourgogne-Franche-Comté', 'Grand Est', 
#     'Pays de la Loire', 'Corsica', 'Essonne', 'Yveline', 'Seine Saint Denis', 
#     'Seine (Paris)', 'Pas de Calais', 'Moselle', 'Hauts de Seine', 'Nord', 
#     'Seine et Marne', 'Loiret', 'Charente-Maritime', 'Loir et Cher', 
#     'Val d\'Oise', 'Val de Marne', 'Garonne (Haute)', 'Somme'
# ]


# import pandas as pd

# # Load the data
# file_path = 'SalesForCourse_quizz_table.xlsx'
# df = pd.read_excel(file_path)

# # Rename columns for consistency
# df.rename(columns={
#     'quantity': 'Quantity',
#     'customer_age': 'Customer Age',
#     'product_category': 'Product Category',
#     'sub_category': 'Sub Category',
#     'customer_gender': 'Customer Gender',
#     'revenue': 'Revenue',
#     'state': 'State'  # Ensure this matches the column name in your dataset
# }, inplace=True)

# # Remove rows where 'State' is not in valid_french_states or is NaN
# df = df[df['State'].isin(valid_french_states)]

# # Check for any remaining NaN values and handle them if necessary
# df = df.dropna(subset=['State'])

# # Verify the cleaned dataset
# unique_states = df['State'].unique()
# print("Filtered unique states:")
# print(unique_states)


# import matplotlib.pyplot as plt

# # Group data by State and Product Category
# state_product_distribution = df.groupby(['State', 'Product Category'])['Quantity'].sum().reset_index()

# # Get unique states
# states = state_product_distribution['State'].unique()

# # Plot a pie chart for each state individually
# for state in states:
#     state_data = state_product_distribution[state_product_distribution['State'] == state]
    
#     plt.figure(figsize=(8, 6))
#     plt.pie(
#         state_data['Quantity'],
#         labels=state_data['Product Category'],
#         autopct='%1.1f%%',
#         startangle=140,
#         colors=plt.cm.tab20.colors[:len(state_data)]  # Use a colormap with enough distinct colors
#     )
#     plt.title(f'Product Category Distribution in {state}')
#     plt.axis('equal')  # Equal aspect ratio ensures the pie chart is drawn as a circle.
#     plt.show()



import matplotlib.pyplot as plt
import pandas as pd

# Define valid French states
valid_french_states = [
    'Île-de-France', 'Provence-Alpes-Côte d\'Azur', 'Auvergne-Rhône-Alpes', 
    'Occitanie', 'Hauts-de-France', 'Bretagne', 'Normandie', 
    'Centre-Val de Loire', 'Bourgogne-Franche-Comté', 'Grand Est', 
    'Pays de la Loire', 'Corsica', 'Essonne', 'Yveline', 'Seine Saint Denis', 
    'Seine (Paris)', 'Pas de Calais', 'Moselle', 'Hauts de Seine', 'Nord', 
    'Seine et Marne', 'Loiret', 'Charente-Maritime', 'Loir et Cher', 
    'Val d\'Oise', 'Val de Marne', 'Garonne (Haute)', 'Somme'
]

# Power BI provides a DataFrame named 'dataset'
file_path = 'SalesForCourse_quizz_table.xlsx'
df = pd.read_excel(file_path)



df.rename(columns={
    'quantity': 'Quantity',
    'customer_age': 'Customer Age',
    'product_category': 'Product Category',
    'sub_category': 'Sub Category',
    'customer_gender': 'Customer Gender',
    'revenue': 'Revenue',
    'state': 'State'  
}, inplace=True)


df = df[df['State'].isin(valid_french_states)]


df = df.dropna(subset=['State'])


accessories_data = df[df['Product Category'] == 'Accessories']


state_accessories_distribution = accessories_data.groupby('State')['Quantity'].sum().reset_index()


plt.figure(figsize=(10, 8))
plt.pie(
    state_accessories_distribution['Quantity'],
    labels=state_accessories_distribution['State'],
    autopct='%1.1f%%',
    startangle=140,
    colors=plt.cm.tab20.colors[:len(state_accessories_distribution)] 
)
plt.title('Distribution of Accessories Sales Across States')
plt.axis('equal')  
plt.show()
