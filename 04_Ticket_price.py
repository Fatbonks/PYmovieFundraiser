def ticket_price():
    name = ""
    age = 0
    ticket_p = 0.0
    while True:
        name = input("Name: ")
        if name == "2":
            print("Profit from Tickets: $10.50")
            break
        age = int(input("Age: "))
        if age == 16:
            ticket_p = 10.50
        print(name, ":", "$10.50")

ticket_price()
