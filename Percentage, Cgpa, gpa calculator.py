print("THIS PROGRAM CALCULATES THE PERCENTAGE, GPA AND GRADE OF THE STUDENT")
n=5
subject_one_total=1
subject_one=0
#TO TAKE INPUT OF THE TOTAL MARKS AND THE MARKS SCORED IN THE FIRST SUBJECT
while n>3:
    subject_one_total=int(input("Enter the total marks in first subject : "))
    subject_one=float(input("Enter the marks scored in the subject : "))
    print()    
      

#TO TAKE INPUT OF THE TOTAL MARKS AND THE MARKS SCORED IN THE SECOND SUBJECT

    subject_two_total=int(input("Enter the total marks in second subject : "))
    subject_two=float(input("Enter the marks scored in the second subject : "))
    print()

#TO TAKE INPUT OF THE TOTAL MARKS AND THE MARKS SCORED IN THE THIRD SUBJECT

    subject_three_total=int(input("Enter the total marks in third subject : "))
    subject_three=float(input("Enter the marks scored in the third subject : "))
    print()

#TO CALCULATE THE PERCENTAGE AND GPA OF THE FIRST SUBJECT

    percentage_one=(subject_one*100)/(subject_one_total)
    gpa_one=(percentage_one*5)/100
    print("The percentage in first subject is", percentage_one)
    print("The GPA of first subject is",gpa_one)
    print()

#TO CALCULATE THE PERCENTAGE AND GPA OF THE SECOND SUBJECT

    percentage_two=(subject_two*100)/(subject_two_total)
    gpa_two=(percentage_two*5)/100
    print("The percentage in second subject is", percentage_two)
    print("The GPA of second subject is",gpa_two)
    print()

#TO CALCULATE THE PERCENTAGE AND GPA OF THE THIRD SUBJECT

    percentage_three=(subject_three*100)/(subject_three_total)
    gpa_three=(percentage_three*5)/100
    print("The percentage in third subject is", percentage_three)
    print("The GPA of third subject is",gpa_three)
    print()

#TO CALCULATE THE OVERALL CGPA OF THE SUBJECTS

    CGPA=(gpa_one+gpa_two+gpa_three)/3
    print("----------------THE CGPA OF THE STUDENT IS ",CGPA,"----------------")
    print()

#CONDITIONS TO CALCULATE THE GRADE SCORED BY THE STUDENT


    if CGPA>=4:
        print("--------THE GRADE OF THE STUDENT IS  'A' .--------")
          
    elif (CGPA<4 and CGPA>=3):
        print("---------THE GRADE OF THE STUDENT IS 'B' .--------")
    elif (CGPA<3 and CGPA>=2):
        print("---------THE GRADE OF THE STUDENT IS 'C' .--------")
    elif (CGPA<2 and CGPA>=1):
        print("--------THE GRADE OF THE STUDENT IS 'D' .--------")
    elif (CGPA<1):
        print("--------THE GRADE OF THE STUDENT IS 'F' .--------")
    print()

    bb=str(input("Do you want to re-run the program (y/n): "))
    if bb == "y" :
    
        continue
    
    else:
        n=2
        
          
#PROGRAM ENDS          

 





























