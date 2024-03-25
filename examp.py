def get_min_price(phone,operators):
	current_prefix = ''
	min_price = 0
	rsl = ''	
	for row in operators:
		for key in row:
			if not current_prefix:
				current_prefix = str(key)
				min_price = row[key]
			if  phone.startswith(str(key))  :

				if (len(str(key)) > len(current_prefix) and int(current_prefix) in row ) or ((len(str(key)) == len(current_prefix) or int(current_prefix) not in row)  and   row[key] <= min_price):
					#change value if the element in the same dict and length > current length
					#or not same dict but lesser or same dict and same length and lesser 
					min_price = row[key]
					current_prefix = str(key)
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

if rsl :
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
