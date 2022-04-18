fruits = [ 'banana','apple','strawberry','blueberries','watermelon' ]
fruits.sort()

for i in fruits:
    print(i, len(i))

fruits.append('red')
fruits.append('blue')
fruits.append('pink')
fruits.reverse()
print(fruits)