monIncome = int
annInvoicing = int
quaCars = int(input('Enter the number of cars: '))
rent = int(input('Enter the value of the car: '))

monIncome = quaCars + rent
annInvoicing = ((quaCars * 0.8) * rent) * 12
print('The monthly billing is: ', monIncome)
print("The annual revenue consedering the rental of 80 percent of the cars is: ", annInvoicing)