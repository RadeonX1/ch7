def sum_number(End):
    sum=0
    for i in range(1,End+1):
        sum += i
        print(f"sum of 1..{End}={sum}")

#Main program
print("Program sum 1 to 10 used function.")
num = int(input("enter number :"))
sum_number(num)
