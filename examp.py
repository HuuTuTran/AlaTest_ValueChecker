def get_min_price(phone,operators):
	min_price = float('inf')
	rsl = ''	
	for row in operators:
		current_prefix = ''
		#get the longest prefix that the phone start with
		for key in row:
			if  phone.startswith(str(key)) and len(str(key)) > len(current_prefix):
				current_prefix = str(key)
		#check if the price is lesser than the min price		
		if 	current_prefix and row[key] < min_price     :
			min_price = row[key]
			rsl = operators.index(row) 
	return rsl,min_price


# The complexity is o(k*m*n)



a = {
    1: 0.9,
    268: 5.1,
    46: 0.17,
    4620: 0.0,
    468: 0.15,
    4631: 0.15,
    4673: 0.9,
    46732: 1.1
}

b = {
    1: 0.82,
    44: 0.5,
    46: 0.2,
    467: 1.0,
    48: 1.2
}
operators = [a,b]
phone = '4673212345'
rsl , min_price = get_min_price(phone,operators)

if rsl != '' :
	print(f"It's cheapest to dial {phone} with operator {rsl} with price of {min_price}") 
else:
	print(f"it is not possible to dial {phone} with any operator") 



# a  = {
#     1: 0.9,
#     268: 5.1,
#     46: 0.17,
#     4620: 0.0,
#     468: 0.15,
#     4631: 0.15,
#     4673: 0.9,
#     46732: 1.1
# }

# b = {
#     1: 0.92,
#     44: 0.5,
#     46: 0.2,
#     467: 1.0,
#     48: 1.2
# }
