'''A MEANS PASS WITH EXCELLENT
   B MEANS PASS WITH GOOD
   C MEANS PASS WITH ALRIGHT
   D MEANS PASS WITH NICE
   F MEANS FAIL '''

m1= int(input("enter the marks (m1):"))
m2= int(input("enter the marks (m2):"))
m3= int(input("enter the marks (m3):"))
m4= int(input("enter the marks (m4):"))
m5= int(input("enter the marks (m5):"))

percentage= (m1+m2+m3+m4+m5)/5
print(percentage)

if(percentage<33):
    print(f"you fail with {percentage} and grade is F")
elif(percentage>=90):
    print(f"you pass with {percentage} and grade is A")
elif(percentage>=80):
    print(f"you pass {percentage} and grade is B")
elif(percentage>=70):
    print(f"you pass with {percentage} and grade is C")
elif(percentage>=60):
    print(f"you pass with {percentage} and grade is D")

