friends = [("Rachel", 19),
           ("Monica", 23),
           ("Phoebe", 17),
           ("Joey", 16),
           ("Chandler", 21),
           ("Ross", 24)]

age = lambda data:data[1] >= 21

drinking_buddies= list(filter(age, friends))

for i in drinking_buddies:
    print(i)

