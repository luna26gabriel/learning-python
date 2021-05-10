store =[("Soda", 5.0), 
        ("Sanduich", 3.5), 
        ("Chesse", 16.0), 
        ("Ice Cream", 5.0)]

to_euros = lambda data: (data[0],data[1]*6.12)
to_dollars = lambda data: (data[0],data[1]*5.62)

store_euros = list(map(to_euros, store))
store_dollars = list(map(to_dollars, store))

for i in store_dollars:
    print(i)

