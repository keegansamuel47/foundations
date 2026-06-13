age = int(input("what is your age? "))
if age >=18:
    print("adult")
else:
    print("minor")

number = int(input("pick a number. "))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

score = int(input("what is your score? "))
if score >=90:
    print("A")
elif score >=80:
    print("B")
elif score >=70:
    print("C")
else:
    print("F")

#print big , don't exactly know why but  think if x is greater than 3 the elif condition needs to differ
x = 5
if x > 3:
    print("big")
elif x > 4:
    print("bigger")