# Example 1
from traceback import print_tb
from unittest import skipIf

students = {
"Alice": [85, 78, 92],
"Bob": [79, 74, 81],
"Charlie": [91, 82, 85],
"David": [76, 85, 83],
"Eve": [88, 79, 92]
}

#task1
total = 0
n = 0
p= 0
students_a = {}
for i in students.keys():
    total = 0
    n = 0
    for v in students[i]:
        total += v
        n +=1
        p = round(total/n,2)
    students_a[i] = p

    print(f"{i} average is: {p}")
print(students_a)
maxi = max(students_a, key = students_a.get)
mini = min(students_a, key = students_a.get)
print(f"Highest score is : {maxi}")
print(f"Lowest score is:{mini}")
students["Frank"] = [80,90,85]
print(students)

#Excersise 2

import numpy as np
inventory = {
"apple": (50, 0.5),
"banana": (100, 0.2),
"orange": (75, 0.3),
"pear": (20, 0.4)
}
#1
for i,k in inventory.items():
    print('{0:<9}{1:<9}'.format(f"{i}",f"{k}"))
#2
total = 0
for i,k in inventory.items():
    a,b = k
    product = a*b
    print(product)
    total += product
print(total)
#3
inventory["mango"] = (30, 0.6)
print(inventory)
#4
inventory["banana"] = (120, 0.2)
print(inventory)
del inventory["pear"]
print(inventory)
#Exercise 3
employees = [
("John Doe", "Accounting", "john.doe@example.com"),
("Jane Smith", "Marketing", "jane.smith@example.com"),
("Emily Davis", "HR", "emily.davis@example.com"),
("Michael Brown", "IT", "michael.brown@example.com")
]
for i in employees:
    a,b,_ = i
    print(f"Name:{a:} - Deparment:{b}")

print(employees)
L_S = []
for i in employees:
    _,_,a = i
    L_S.append(a)
L_S2 = sorted(L_S, key= lambda x : x.split(".")[1])
print(L_S2)

#3
employees.append(("David Wilson","Sales","david.wilson@example.com"))
print(employees)
#4
for i in employees:
    a,b,_ = i
    if a in "Jane Smith":
        print(b)
#Excersie 4
library = {
"978-3-16-148410-0": {"title": "The Catcher in the Rye","author": "J.D. Salinger", "year": 1951},
"978-0-14-028329-7": {"title": "1984", "author": "George Orwell", "year": 1949},
"978-0-7432-7356-5": {"title": "To Kill a Mockingbird","author": "Harper Lee", "year": 1960},
"978-0-452-28423-4": {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932}}

#1
for i in library.values():
    for k,l in i.items():
        print(f"{k}:{l}",end="/ ")
    print()
#2
for i,k in library.items():
    if i in "978-0-14-028329-7":
        for m,n in k.items():
            print(f"{m}:{n}",end="/ ")
print()
#3
library["978-1-4028-9462-6"] = {"title":"The Great Gatsby",
"author": "F. Scott Fitzgerald", "year": 1925}
#4
library["978-0-7432-7356-5"]["year"] = 1961
print(library)
#5
del library["978-0-452-28423-4"]
print(library)
#Exercise 5
cities = {
"New York": 8419000,
"Los Angeles": 3980000,
"Chicago": 2716000,
"Houston": 2328000,
"Phoenix": 1690000
}

for i,k in cities.items():
    print(f"{i}: {k} population")

maxi = max(cities, key=cities.get)
mini = min(cities,key=cities.get)
print(maxi)
print(mini)
cities["Phoenix"]=1700000
print(cities)
cities["San Francisco"]= 884000
print(cities)
#Excercise 6
movies = {

"Inception": {"year": 2010, "rating": 8.8, "genre": "Sci-Fi"},
"The Godfather": {"year": 1972, "rating": 9.2, "genre":"Crime"},
"The Dark Knight": {"year": 2008, "rating": 9.0, "genre":"Action"},
"Pulp Fiction": {"year": 1994, "rating": 8.9, "genre": "Crime"},
"Forrest Gump": {"year": 1994, "rating": 8.8, "genre": "Drama"}
}
#1
for i,k in movies.items():
    print(f"{i} -", end=" ")
    for l,s in k.items():
        print(f"{l}:{s}",end="/ ")
    print()
#2
get = []
#3
movies["The Matrix"]= {"year":1999,"rating":8.8,"genre":"Sci-Fi"}
#
movies["Inception"]["rating"] = 9.0
print(movies)
del movies["Pulp Fiction"]
print(movies)

#Exercise 7
countries = {
"USA": "Washington, D.C.",
"Canada": "Ottawa",
"France": "Paris",
"Germany": "Berlin",
"Japan": "Tokyo"
}
#1
for i,k in countries.items():
    print(f"{i}: {k} ")
#2
for i,k in countries.items():
    if i in "Germany":
        print(k)
#3
countries["Australia"] = "Canberra"
print(countries)
#4
countries["USA"]="New Washington"
print(countries)
del countries["France"]
print(countries)
#Exercise 8
cart = [
{"item": "apple", "quantity": 3, "price_per_unit": 0.5},
{"item": "banana", "quantity": 6, "price_per_unit": 0.2},
{"item": "orange", "quantity": 4, "price_per_unit": 0.3},
{"item": "pear", "quantity": 2, "price_per_unit": 0.4}
]
#1
for i in cart:
    for k,l in i.items():
        print(f"{k}: {l}",end="/")
    print()
#2
total=0
for i in cart:
    product = i["quantity"] * i["price_per_unit"]
    total += product
print(total)
#3
cart.append({"item":"grape","quantity": 2,"price_per_unit": 0.6})
#4
for i in cart:
    if i["item"] == "banana":
        i["quantity"] = 10
print(cart)
#
for i in cart:
    if i["item"] == "pear":
        cart.remove(i)
print(cart)
#Exercise 9
weather = {
"Monday": {"temperature": 20, "humidity": 60},
"Tuesday": {"temperature": 22, "humidity": 55},
"Wednesday": {"temperature": 19, "humidity": 65},
"Thursday": {"temperature": 23, "humidity": 50},
"Friday": {"temperature": 21, "humidity": 70}
}
#1
for i,k in weather.items():
    print(i,end="-")
    for l,m in k.items():
        print(f"{l}:{m}", end="/")
    print()
#2
highest = max(weather, key=lambda v: weather[v]["temperature"])
print (highest)

lowest = min(weather, key=lambda v: weather[v]["temperature"])
print(lowest)
weather["Wednesday"]["temperature"]= 25
print(weather)
weather["Saturday"]= {"temperature":24,"humidity": 70}
print(weather)
