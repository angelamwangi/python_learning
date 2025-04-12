#while loops
'''i=1
while i<=5:
    print("Sky"*i)
    i+=1
print("toddles")'''
###########GUESSING GAME####################
number=43
tries=3
answer_found=False

while answer_found==False and tries>0:
    guess = int( input( "Enter guess: " ) )
    if guess==number:
        print(f"You win, correct number is {number}")
        answer_found=True
    else:
        tries-=1
        print(f"Wrong.You have {tries} remaining.")
else:
    print("woiye,sorry")