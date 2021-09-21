print("Please enter your grades: ")
prelim = float(input("Prelims: "))
midterm = float(input("Midterms: "))
semis = float(input("Semifinals: "))
final = float(input("Finals: "))
avg = (prelim + midterm + semis + final)/4
print("Average: {}" .format(avg))

if avg>=99 and avg<=100:
    print("Your Average is {}" .format(avg) + "! Congratulations, you got 'A'!")
elif avg>=90 and avg<=98:
    print("Your Average is {}" .format(avg) + "! Good Job, you got 'B'!")
elif avg>=80 and avg<=89:
    print("Your Average is {}" .format(avg) + "! Nice work, you got 'C'!")
elif avg>=71 and avg<=79:
    print("Your Average is {}" .format(avg) + "! Averagely good, you got 'D'!")
elif avg>=61 and avg<=70:
    print("Your Average is {}" .format(avg) + "! Try Harder, you got 'E'!")
elif avg<60:
    print("Your Average is {}" .format(avg) + "! You failed, you got 'F'!")
else:
    print("INVALID")