print("THIS PROGRAM CALCULATES THE SUM OF EVEN AND ODD NUMBERS TILL A GIVEN RANGE")

sum_one=0   #PRE-ASSIGNING VALUES FOR FURTHER USE

sum_two=0   #PRE-ASSIGNING VALUES FOR FURTHER USE
i=0         #PRE-ASSIGNING VALUES FOR FURTHER USE
j=1         #PRE-ASSIGNING VALUES FOR FURTHER USE

number=int(input("Enter the last number of the range : "))

print()         #TO LEAVE SPACE AFTER THE INPUT

#LOOP TO CALCULATE THE SUM OF EVEN NUMBERS

while number>=i:
    sum_one+=i
    i+=2

    
    
print("The sum of even numbers till",number,"is", sum_one)

print()              #TO LEAVE SPACE AFTER THE INPUT

#LOOP TO CALCULATE THE SUM OF ODD NUMBERS

while number>=j:
    sum_two+=j
    j+=2
    

print("The sum of odd numbers till",number,"is", sum_two)

#END
    
    
