def loop_ticket(tickets, ticket_solded):
    while True:
        print("you have {} tickets left".format(tickets))
        if tickets == 0:
            print("you have sold {}. There is {} places available".format(ticket_solded, tickets))
            break
        ans = input("Name: ")
        if ans == "":
            print("this cannot be blank")

        elif ans == "2":
            print("you have sold {}. There is {} places available".format(ticket_solded, tickets))
            break

        else:
            tickets -= 1
            ticket_solded += 1


ticket_solded = 0
tickets = 5
loop_ticket(tickets, ticket_solded)
