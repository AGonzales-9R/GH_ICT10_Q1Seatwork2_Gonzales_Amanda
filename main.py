from pyscript import display

restuarant_name = "AMG Bakery" #string
owner_name = "Amanda Gonzales" #string
year_established = 2021 #integer
popular_item_price = 60 #integer
has_delivery = True #boolean
product_names = ['Banana Bread','Chocolate Chip Cookie','Brownie','Red Velvet Cupcake','Cinnamon Roll','Apple Pie'] #list
business_hours = ['10:00AM','10:00PM'] #list
common_allergens = ['Lactose','Nuts','Wheat'] #list
tax_rate = 0.08 #float
menu_prices = [50,80,100,120,150] #list
tagLine = "Sweetness is My Business!" #string

display(F'{restuarant_name}', target='brand_name')
display(F'"{tagLine}"', target='tagline')
display(F'By: {owner_name}', target='owner')
display(F'Since: {year_established}', target='year')


display(F'{product_names[0]}', target='card-title1')
display(F'₱{popular_item_price}', target='card-price1')
display(F'Allergens: {common_allergens[0]}, {common_allergens[1]}, {common_allergens[2]}', target='card-allergens1')

display(F'{product_names[1]}', target='card-title2')
display(F'₱{menu_prices[0]}', target='card-price2')
display(F'Allergens: {common_allergens[0]}, {common_allergens[2]}', target='card-allergens2')

display(F'{product_names[2]}', target='card-title3')
display(F'₱{menu_prices[1]}', target='card-price3')
display(F'Allergens: {common_allergens[0]}, {common_allergens[1]}, {common_allergens[2]}', target='card-allergens3')

display(F'{product_names[3]}', target='card-title4')
display(F'₱{menu_prices[2]}', target='card-price4')
display(F'Allergens: {common_allergens[0]}, {common_allergens[2]}', target='card-allergens4')

display(F'{product_names[4]}', target='card-title5')
display(F'₱{menu_prices[3]}', target='card-price5')
display(F'Allergens: {common_allergens[0]}, {common_allergens[2]}', target='card-allergens5')

display(F'{product_names[5]}', target='card-title6')
display(F'₱{menu_prices[4]}', target='card-price6')
display(F'Allergens: {common_allergens[0]}, {common_allergens[2]}', target='card-allergens6')

if has_delivery == True:
    display(F'We deliver through: Grab, Foodpanda, and Lalamove.', target='delivery')
else:
    display(F'We do not accept delivery.', target='delivery')

display(F'Business hours: {business_hours[0]}-{business_hours[1]}.', target='hours')    
display(F'The product prices above includes the tax rate of {tax_rate} (8%).', target='tax')