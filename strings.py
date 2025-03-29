#double quotes to define strings
unit="Python's course"
course=unit[:]
print(course)
print(unit)
#multi line string
email='''
HI,JOHN
Karibu chai brewed the Kenyan way, kuna mandazi pia
bye >3'''
print(email)

#string manipulation
print(unit[0]) #1st value
print(unit[-1])# last value
print(unit[:-6]) #6 values from the end (nyuma)
print(unit[0:6]) # print 0 to 5th value(exclude 6th value)
name="  Jennifer tya jfto kipi"
print(name[1:-1])

#formatted strings
print(len(unit))
# string methods
print(unit.upper())
print(unit.title())
print(name.replace("J ","K"))
print(name.strip(" "))
print("chai" in email)