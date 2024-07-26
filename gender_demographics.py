

import pandas as pd
import matplotlib.pyplot as plt


file_path = 'SalesForCourse_quizz_table.xlsx'
df = pd.read_excel(file_path)


df.rename(columns={
    'quantity': 'Quantity',
    'customer_age': 'Customer Age',
    'product_category': 'Product Category',
    'sub_category': 'Sub Category',
    'customer_gender': 'Customer Gender',
    'revenue': 'Revenue'
}, inplace=True)


quantity_by_product_subcategory = df.groupby(['Product Category', 'Sub Category'])['Quantity'].sum().reset_index()


product_categories = quantity_by_product_subcategory['Product Category'].unique()


for category in product_categories:
    category_data = quantity_by_product_subcategory[quantity_by_product_subcategory['Product Category'] == category]
    
    
    explode = [0.1] * len(category_data)  

    
    if category == product_categories[0]:  
        plt.figure(figsize=(14, 10))  
    else:
        plt.figure(figsize=(8, 6))
    
    plt.pie(
        category_data['Quantity'],
        labels=category_data['Sub Category'],
        autopct='%1.1f%%',
        startangle=140,
        explode=explode,
        colors=plt.cm.tab20.colors[:len(category_data)]  
    )
    plt.title(f'Sub Category Distribution within {category}')
    plt.axis('equal')  
    plt.show()
