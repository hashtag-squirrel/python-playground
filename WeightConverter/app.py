weight = int(input("Weight: "))
unit = input("(L)bs or (K)g? ").lower()

if unit == "l":
    weight *= 0.45
    print(f'You are {weight} kilos')
elif unit == "k":
    weight = weight // 0.45
    print(f'You are {weight} pounds')
else:
    print("Incorrect unit")