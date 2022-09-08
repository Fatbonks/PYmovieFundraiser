def ticket_price():
    name = ""
    age = 0
    ticket = 5
    ticket_sold = 0
    ticket_p = 0.0
    total_price = 0
    while not ticket == 0:
        print("there is", ticket, "places left")
        name = input("Name: ")
        if name == "2":
            print("Profit from Tickets: ${:.2f}".format(total_price))
            break
        age = int(input("Age: "))
        if 10 < age < 65:
            ticket_p = 10.50
            ticket_sold += 1
            ticket -= 1
            total_price += ticket_p
        if age < 10:
            print("you are too young for this movie")
        if age > 65:
            print("the age you have entered is too high")
    if name != "2":
        print("Profit from Tickets: ${:.2f}".format(total_price))

ticket_price()
