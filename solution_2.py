class Node:
	def __init__(self):
		self.children = {}  
		self.is_word = False  
		self.operator = None  
		self.price = None  

class Trie:
	def __init__(self):
		self.root = Node()

	def insert(self,prefix, operator, price):
		root = self.root
		for char in prefix:
			if char not in root.children: 
				root.children[char] =  Node()
			root =  root.children[char]
		root.price = price
		root.operator = operator
		root.is_word = True
	def search(self,number):
		current_price = float('inf')
		current_operator = None

		root = self.root
		for char in number:
			if char not in root.children:
				break
			root =  root.children[char]
			if root.is_word and root.price <  current_price :
				current_price =  root.price
				current_operator = root.operator
		return current_operator,current_price


def get_min_price(phone,operators):
	cheapest_operator = None
	cheapest_price = 0
	root = Trie()
	for  price_list in operators:
		for prefix, price in price_list.items():
			root.insert(str(prefix), operators.index(price_list), price)
	cheapest_operator , cheapest_price =  root.search(phone)
	return cheapest_operator,cheapest_price




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

phone = "4684620123456"
price_lists = [a,b]
rsl , min_price = get_min_price(phone,price_lists)
if rsl != None :
	print(f"It's cheapest to dial {phone} with operator {rsl} with price of {min_price}") 
else:
	print(f"it is not possible to dial {phone} with any operator") 