weight=input("weight?: ")
unit=input(" Pounds or Kilos? Please answer with a single P or K:  ")
if unit.upper()=="P":
    converted=int(weight)*0.45
    print(f"you are  {round(converted)} kilos")
else:
    converted=int(weight)/0.45
    print(f"you are {round(converted)} pounds")
