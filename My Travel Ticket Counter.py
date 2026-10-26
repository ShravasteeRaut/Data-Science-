
travel_name = "Pune to Mumbai"
price = 500.00
quantity = 3
is_available = True

print("Travel Route:", travel_name)
print("Ticket Price: Rs.", price)
print("Number of Tickets:", quantity)
print("Available?", is_available)

print(type(travel_name))
print(type(price))
print(type(quantity))
print(type(is_available))

total = price * quantity
print("Total ticket cost: Rs.", total)
print("Discounted price: Rs.", price - 50)
print("Double tickets:", quantity * 2)

print("Is ticket price under Rs. 600?", price < 600)
print("More than 2 tickets?", quantity > 2)
print("Is ticket price exactly Rs. 500?", price == 500.00)

travel_company = "Quick" + " " + "Travels"
print("Travel Company:", travel_company)
print("Letters in travel name:", len(travel_name))
print("First letter:", travel_name[0])

price_a = 500.00
price_b = 800.00
print("Before:", price_a, "and", price_b)

temp = price_a
price_a = price_b
price_b = temp
print("After:", price_a, "and", price_b) 
