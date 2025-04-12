weight=float(input("How much do you weigh? "))
unit_of_measurement=input("Enter unit of measurement (L) for lbs or (K) for kgs: ").upper()

if unit_of_measurement =="L":
    weight*=0.45359237
    print(f"You weigh {weight} kgs.")
elif unit_of_measurement =="K":
    weight/=0.45359237
    print(f"You weigh {weight} lbs.")
else:
    print("Invalid Input")