def display_triangle(num, ch):
    for i in range(1, num+1):
        message = ""
        for n in range(i):
            message += ch
            print(message)
        
#main pro program
print("Program display triangle.")
num = int(input("Enter number line :"))
ch = input("Enter character :")
display_triangle(num, ch)