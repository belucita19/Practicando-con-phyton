inversion = float(input("Introduce la inversión inicial: "))
interes = 0.04
balance1 = inversion * (1 + interes)
print("Balance tras el primer año:" + str(round(balance1, 2)))
balance2 = balance1 * (1 + interes)
print("Balance tras el segundo año:" + str(round(balance2, 2)))
balance3 = balance2 * (1 + interes)
print("Balance tras el tercer año:" + str(round(balance3, 2)))
balance4 = balance3 * (1 + interes)
print("Balance tras el cuarto año:" + str(round(balance4, 2)))
balance5 = balance4 * (1 + interes)
print("Balance tras el quinto año:" + str(round(balance5, 2)))

