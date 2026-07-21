print("====== CAJERO AUTOMÁTICO ======")

saldo = 500.00

print("Saldo disponible: $", saldo)

retiro = float(input("Ingrese la cantidad que desea retirar: $"))

if retiro <= 0:
    print("Debe ingresar una cantidad mayor que cero.")
elif retiro > saldo:
    print("Fondos insuficientes.")
else:
    saldo -= retiro
    print("Retiro realizado con éxito.")
    print("Saldo restante: $", saldo)