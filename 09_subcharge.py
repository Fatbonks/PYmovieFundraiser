surcharge = 0.00
sub = 0.0
while True:
    Name = input("Name: ")
    ans = input("cash or credit").lower()
    subtotal = int(input("Subtotal: "))

    if ans == "credit":
        surcharge = 0.05
        sub = surcharge * subtotal
    else:
        surcharge = 0.00
    total = sub + subtotal
    print("Name: {} | Subtotal: ${} | Surcharge: {} | Total: ${}".format(Name, subtotal, surcharge, total))


