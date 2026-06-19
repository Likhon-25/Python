# count = 1

# while count <= 10 : 
    # print(count)
#     count += 1

 # print("The End")


# -----------------------------------------------

count = 1
add = 0 

while count <= 10:
    add = add + count
    # print(add)
    count += 1

# print(f"Total sum : {add} ")
# print("The End")

# -----------------------------------------------


num = 1        
mult = 1        

while num <= 5: 
    mult = mult * num 
    # print(mult)
    num += 1

# print(f"Multiplication Total : {mult}")
# print("The End")

# --------------------------------------------------

i = 1

while i < 6:
    # print(i)

    if i == 3:
        break
    i += 1

# -------------------

i = 0
while i < 6:
    i += 1

    if i == 3:
        continue
    # print(i)


# ----------------------------------------------------
# lIST & Tauple in python

# .............List ---  ""mutable""..........................

# fruits = ["Apple", "Mango", "Bannana"]
# print(fruits)
# print(fruits[1])

# fruits[1] = "Guava"
# print(fruits)
# print(fruits[1])


#.................. Tauple --- ""immutable"""........................

# fruits = ("Apple", "Mango", "Bannana")
# print(fruits)
# print(fruits[1])

# fruits[1] = "Guava"
# print(fruits)
# print(fruits[1])

# ------------------------------------------

# fruits = ["apple", "Mnago", "charry", "guava", "Watermilon"]
# print(fruits[2:5])

# print(fruits + ["Dragon", "Lichi"])
# print(fruits * 3)
# print(fruits)



#  ...........  List Methods ...................

fruits = [ "Mango", "Banana"]
fruits.append("Cherry")
# print(fruits)

#  ---------------------------

fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
# print(fruits)

# ------------------------------

fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
# print(fruits)

# ---------------------------

fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
# print(fruits)

# -----------------------------------
cars = [ 'Volvo','Ford', 'BMW']
cars.sort()
# print(cars)

# ------------------------------
fruits = ['apple', 'banana', 'cherry', 'orange']
showIndex = fruits.index('cherry')
# print(showIndex)

# ................... 2nd List (Matrix) ...........................
my_matrix = [
    [1,3,6,7],
    [-2,4,5,-7],
    [9.6,3,0],
    [44,-9, -4, 3],
    [1,3,4,2,6]
]

# print(my_matrix[3][0])



# ............................... Dictionary in Python ..................... 
students = {
    "name" : "Likhon Mondol",
    "Institute" : "Rangpur",
    "Department" : "Computer Scince & Technology",
    "Skill" : "Full Stack Engineer",
    "Age" : "20",
    "is_Valid" : True
}

# print(type(students))
# print(students["name"])
# print(type(students["Age"]))
# print(type(students["is_Valid"]))

#  ........ Operations in Dictionary ..................... 
dics_items = students.items()
# print(dics_items)
# print(students.values())
# print(students.keys())
# print(type(list(dics_items)[0]))

# --------------

students.update({
    "Institute" : "RIIT",
    "Hobby" : "Jannahat"
})

# print(students)


#  ..................  For Loop .................... 
fruits = ["Apple", "Orange", "Pinaple", "Jackfruits", "Guava"]

# for fruit in fruits:
#     print(fruit)

# -------------  Range in For Loop ------------------
# for i in range(3,13,2):
# for i in range(3,10):
for i in range(3):
    print(i)
