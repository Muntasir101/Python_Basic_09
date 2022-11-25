cars_list = ['bmw', 'honda', 'nissan', 'toyota']
number_list = [12, 11, 23, 4, 56]
mix_list = [0, 1, 2, 'bmw', 'honda', 12.3]

# Methods
length = len(mix_list)
print(length)

cars_list.append("suzuki")
print(cars_list)

cars_list.insert(0, 'tata')
print(cars_list)

index = cars_list.index("nissan")
print(index)

my_favorite_car = cars_list.pop()
print(cars_list)
print(my_favorite_car)

cars_list.remove('bmw')
print(cars_list)

slice = cars_list[:2]
print(slice)

slice2 = cars_list[1:3]
print(slice2)

number_list.sort()
print(number_list)

cars_list.sort()
print(cars_list)
