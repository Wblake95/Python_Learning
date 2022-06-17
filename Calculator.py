'''
new stuff from geeksforgeeks.org
this is a 'Division(float) of number' whatever that means
and a 'modulo of both numbers'
I will be testing this today
'''
again = "go"
while again == "go":
    print("would you like to go or stop?")
    again = input()

    print("Choose first int:")
    x = int(input())
    print("Choose operator (+,-,*,/,//,%,//%):")
    print("/ = with decimal, // = without decimal, % = ramainder, //% = both // and % result")
    mode = input()
    print("Choose second int:")
    y = int(input())

    print("Your result:")
    if mode == "+":
        print(x+y)
    elif mode == "-":
        print(x-y)
    elif mode == "*":
        print(x*y)
    elif mode == "/":
        print(x/y)
    # 'Division(float) of number'
    # this just gets ride of the decimal point
    elif mode == "//":
        print(x//y)
    # modulo of both numbers
    # the gets the remainder
    elif mode == "%":
        print(x%y)
    # combine div2 and modulo
    elif mode == '//%' or '// %' or '%//' or '% //':
        print(x//y, "R",x%y)
    # I can't tell the difference between single quote and double quote
    # comma is important to seperate action and text
