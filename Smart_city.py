Smart_city = input("Enter the city name: ")
S_r = int(input("Enter the number of smart roads availabe in "+Smart_city+": "))
M_h = int(input("Enter the number of multinational hospitals availabe in "+Smart_city+": "))
A_inc = int(input("Enter the average annual income per head: "))
P = int(input("Enter the population of "+Smart_city+": "))
L_r = int(input("Enter the literacy rate of "+Smart_city+" in percentage: "))
I_u = int(input("Enter the number of internet users in "+Smart_city+"in percentage: "))
C_r = int(input("Enetr the crime rate of "+Smart_city+" in percentage: "))
if S_r>=400 and M_h>=600 and A_inc>=400000 and P>=8000000 and L_r>=70 and I_u>=70 and C_r<=20:
    print("Yes...ur city passed all th criteria for smart city.")
    print(Smart_city+" is a smart city..")
else :
    print("no your city can't be a Smart city")
    n = input("Do you want the reason....?(yes/no):")
    if n == "yes":
        if P<8000000:
          print(Smart_city+" must have the population more than 8 million to be a smart city.")
        if A_inc<400000:
          print(Smart_city+"'s annual income rate is required 4,00,000 to be a smart city.")
        if S_r<400:
          print(Smart_city+" must have smart roads greater than 400 to be a smart city.")
        if L_r<70:
          print(Smart_city+"'s literacy rate is less than 70% to be a smart city.")
        if I_u<70:
          print(Smart_city+"'s must have internet users more than 70% to be a smart city.")
        if C_r>20:
          print(Smart_city+"'s crime rate should be less than 20% to be a smart city.")
        if S_r<400:
          print(Smart_city+" must have smart roads greater than 400 to be a smart city.")
    else :
        print("Better Luck next time..")