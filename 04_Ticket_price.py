def ticket_price():
    name = ""
    age = 0
    ticket = 5
    ticket_sold = 0
    ticket_p = 0.0
    total_price = 0
    while not ticket == 0:
        print("there is", ticket, "places left")
        try:
            name = input("Name: ")
        except ValueError:
            print("Please input a name")
        if name == "2":
            print("Profit from Tickets: ${:.2f}".format(total_price))
            break
        try:
            age = int(input("Age: "))
        except ValueError:
            print("Please input a whole number")
        if age >= 12 <= 15:
            ticket_p = 7.50
            ticket_sold += 1
            ticket -= 1
            total_price += ticket_p
        elif age > 15 < 65:
            ticket_p = 10.50
            ticket_sold += 1
            ticket -= 1
            total_price += ticket_p
        elif age >= 65 <= 130:
            ticket_p = 7.50
            ticket_sold += 1
            ticket -= 1
            total_price += ticket_p
        elif age < 12:
            print("you are too young for this movie")
        elif age > 130:
            print("That age is too high are you sure thats your age?")
        print(name + ":$" + ticket_p)
    if name != "2":
        print("Profit from Tickets: ${:.2f}".format(total_price))

ticket_price()
