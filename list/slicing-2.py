price_list_u: list[float] = [45.5 , 12.0 , 78.9 , 23.4 , 56.7]

price_list_o: list[float] = sorted(price_list_u)

print(price_list_o)

print(min(price_list_u))
print(max(price_list_o))

print( 23.1 in price_list_o)

counter = 0

print(sum( 1 for p in price_list_o if p > 50.0))