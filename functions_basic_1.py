'''

@ author:
Gianni M. Javier
    
Assignment: Functions Basic I

Objectives:
Avoid common mistakes of using functions
Really understand how to use T-diagram to correctly predict and debug codes

For each of the following code snippets, first predict the output (what you will see printed to the terminal). 
Once you've made a prediction, run the code snippet to see if you are correct!

'''

#1
def number_of_food_groups():
    return 5 # return ends the function and returns 5 to the function call
print(number_of_food_groups())
# Prediction: 5
# Output: 5


# #2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# # Prediction:   Error "number of days in a week silicon or triangle sides() is undefined"
# # Output:   NameError: name 'number_of_days_in_a_week_silicon_or_triangle_sides' is not defined


#3
def number_of_books_on_hold():
    return 5 # return breaks out of the function and returns 5 to the function call
    return 10
print(number_of_books_on_hold())
# Prediction: 5
# Output: 5


#4
def number_of_fingers():
    return 5 # return breaks out of the function and returns 5 to the function call
    print(10)
print(number_of_fingers())
# Prediction: 5
# Output: 5


#5
def number_of_great_lakes():
    print(5) # function will print 5 when it is called
x = number_of_great_lakes() # Value of x will be none because the function is not returning anything to the function call
print(x)
# Prediction: 5
# Output: 5
#         none


# #6
# def add(b,c):
#     print(b+c) # Function will execute when called and print out sum of arguments
# print(add(1,2) + add(2,3))# print will error because function does not return any values but returns none
# # Prediction: 3
# #             5
# #             Error
# # Output: 3
# #         5
# #         TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'


#7
def concatenate(b,c):
    return str(b)+str(c) # Function is executed upon function call and converts arguments into strings, concatenates and returns new String
print(concatenate(2,5))
# Prediction: '25'
# Output: 25


#8
def number_of_oceans_or_fingers_or_continents(): # function is executed upon call
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10 # functions breaks at else statement and retursn 10
    return 7
print(number_of_oceans_or_fingers_or_continents()) #function is called and receives return value of 10 which is then printed to the console
# Prediction: 10
# Output: 100
#         10


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Prediction: 7
#             14
#             21
# Output: 7
#         14
#         21


#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# Prediction: 8
# Output: 8


#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# Prediction: 500
#             500
#             300
#             300
# Output: 500
#         500
#         300
#         500


#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b # Though the function is returning the value saved in the variable b, 
# it is noot being saved or redifined outside of the function, so the original value is not changed
print(b)
foobar()
print(b)
# Prediction: 500
#             500
#             300
#             500
# Output: 500
#         500
#         300
#         500


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# Prediction: 500
#             500
#             300
#             300
# Output: 500
#         500
#         300
#         300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# Prediction: 1
#             3
#             2
# Output: 1
#         3
#         2


#15
def foo():
    print(1)
    x = bar() # function call becomes whatever function returns, after executing,
    # in this case it is 5, so bar() becomes a variable which holds the value 5
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo() # function call becomes whatever function returns, after executing,
    # in this case it is 10, so foo() becomes a variable which holds the value 10 and that value is assigned to y
print(y)
# Prediction: 1
#             3
#             5
#             10
# Output:  1
#         3
#         5
#         10