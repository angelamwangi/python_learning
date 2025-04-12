is_loyal_customer=True
age=19
fare=1240

if is_loyal_customer and age>=60:
    discount=0.5*fare
    print(f"You will pay Ksh{discount}")
else:
    print(f"You will pay Ksh{fare}")