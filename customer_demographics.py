import pandas as pd

file_path = 'SalesForCourse_quizz_table.xlsx'
df = pd.read_excel(file_path)


quantity_by_gender = df.groupby('Customer Gender')['Quantity'].sum().reset_index().sort_values(by='Quantity', ascending=False)
print("Quantity Sold by Customer Gender")
print(quantity_by_gender)

# Quantity Sold by Customer Age
quantity_by_age = df.groupby('Customer Age')['Quantity'].sum().reset_index().sort_values(by='Quantity', ascending=False)
print("Quantity Sold by Customer Age")
print(quantity_by_age)
