print("Please enter your grades: ")
prelim = float(input("Prelims: "))
midterm = float(input("Midterms: "))
semis = float(input("Semifinals: "))
final = float(input("Finals: "))
avg = (prelim + midterm + semis + final)/4
print("Average: {}" .format(avg))

if (avg>=75):
    print ("PASSED")
else:
    print ("FAILED")