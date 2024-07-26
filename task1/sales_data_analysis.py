import pandas as pd
import matplotlib.pyplot as plt


file_path = 'SalesForCourse_quizz_table.xlsx'
df = pd.read_excel(file_path, sheet_name='Salestable')


print(df.head())

# Convert the 'date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Sales Over Time Analysis
sales_over_time = df.groupby('Date')['Revenue'].sum().reset_index()

plt.figure(figsize=(10, 6))
plt.plot(sales_over_time['Date'], sales_over_time['Revenue'], marker='o')
plt.title('Total Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Total Revenue')
plt.grid(True)
plt.show()

# Top Selling Products by Quantity
top_products_quantity = df.groupby(['Product Category', 'Sub Category'])['Quantity'].sum().reset_index().sort_values(by='Quantity', ascending=False)
print("Top Selling Products by Quantity")
print(top_products_quantity)

# Top Selling Products by Revenue
top_products_revenue = df.groupby(['Product Category', 'Sub Category'])['Revenue'].sum().reset_index().sort_values(by='Revenue', ascending=False)
print("\nTop Selling Products by Revenue")
print(top_products_revenue)

# Sales Performance by Product Category
category_performance = df.groupby('Product Category')['Revenue'].sum().reset_index().sort_values(by='Revenue', ascending=False)
print("Sales Performance by Product Category")
print(category_performance)

# Sales Performance by Region (Country/State)
regional_sales = df.groupby(['Country', 'State'])['Revenue'].sum().reset_index().sort_values(by='Revenue', ascending=False)
print("Sales Performance by Region")
print(regional_sales)

# Average Sales per Transaction
average_sales_per_transaction = df['Revenue'].mean()
print(f"Average Sales per Transaction: ${average_sales_per_transaction:.2f}")

# Customer Demographics Analysis
gender_sales = df.groupby('Customer Gender')['Revenue'].sum().reset_index().sort_values(by='Revenue', ascending=False)
print("Sales by Customer Gender")
print(gender_sales)

age_sales = df.groupby('Customer Age')['Revenue'].sum().reset_index().sort_values(by='Revenue', ascending=False)
print("Sales by Customer Age")
print(age_sales)
