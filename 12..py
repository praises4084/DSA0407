import pandas as pd

# Sample sales data (replace this with your actual DataFrame)
data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product A', 'Product B', 'Product D'],
    'Quantity Sold': [20, 15, 25, 18, 22, 30]
}

sales_data = pd.DataFrame(data)

# Group by Product and sum the quantities sold for each product
product_sales = sales_data.groupby('Product')['Quantity Sold'].sum().reset_index()

# Sort the products based on total quantities sold and get top 5
top_5_products = product_sales.nlargest(5, 'Quantity Sold')

print("Top 5 products sold the most in the past month:")
print(top_5_products)
