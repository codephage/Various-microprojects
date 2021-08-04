# To buy a house you need to pay a initial payment, this code will calculate it based on your credit history
# It is a very basic program.
# if the buyer has good credit, they need to put down 5% initial payment
# Otherwise, the buyer need to put down a 20%  initial payment.

PriceofHouse=3000000 # this is the price of the house to buy

answer=input("Has the Client good credit score ? Please type 'yes' or 'no': ") #here you ask in console the client credit reputation

if answer=="yes":
    client_has_good_credit=True
else:
    client_has_good_credit=False


# here it calculates de initial down payment
if client_has_good_credit:
    initial_down_payment=0.05*PriceofHouse
else:
    initial_down_payment=0.2*PriceofHouse

print(f"The price of the house is {PriceofHouse}")
print(f"Your Initial down payment is: {initial_down_payment}")

