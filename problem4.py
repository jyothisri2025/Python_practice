sub1 = int(input("Enter 1st subject marks:"))
sub2 = int(input("Enter 2nd subject marks:"))
sub3 = int(input("Enter 3rd subject marks:"))
sub4 = int(input("Enter 4th subject marks:"))
sub5 = int(input("Enter 5th subject marks:"))

total = sub1 + sub2 + sub3 + sub4 + sub5
avg = total / 5
percentage = (total / 500)*100

print("Toatl marks are : ",total)
print("Avergae :",avg)
print("Percentage :",percentage)