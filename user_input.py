#input () to get user input
name=input("Enter your name: ")
print(type(name))
print(name)
age=int(input("How old are you? "))
print(age)
print(f"Hello {name} you are {age} years old!")
birth_year=int(input("Which year were you born? "))
age=2025-birth_year
print(age)