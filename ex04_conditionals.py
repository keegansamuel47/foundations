age = float(input("what is your age? "))
if age >= 18:
    print("adult")
else:
    print("minor")

number = float(input("pick a number. "))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")

score = float(input("what is your score? "))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")

x = 5
if x > 3:
    print("big")
elif x > 4:
    print("bigger")

# it will print bigger because both statement are true and python only process the first line statement.
x = 5
if x > 4:
    print("bigger")
elif x > 3:
    print("big")