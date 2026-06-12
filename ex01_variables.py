

name = "keegan"
age = 26
height_in_meters = 1.83
is_enjoying_this = True
print(name)
print(age)
print(height_in_meters)
print(is_enjoying_this)
print(type(name))
print(type(age))
print(type(height_in_meters))
print(type(is_enjoying_this))


x = 1
y = 2

b = x
#introduce a third variable to hold the value of x temporarily before the swap
x = y
y = b
print(x)
print(y)

money = 50
#i understand python execute code line by line , first of all check the value for the variable money , which is 50
money = money + 25
#then move to the next line and did the math instruction taking the value of money as 50, the add it to 25, as written in the code
money = money - 10
#then minus 10 from it
print(money)
#the outcome is 65
