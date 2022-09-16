# this gets the ticket holders name #
def ticket_holder_name():
    # This code loops until you use break
    while True:
        # age hold what ever the user inputs
        name = input("what is your name")
        # checks if what the user inputted was blank
        if name == "":
            print('Please input a name')
        # checks if what the user inputted was a number
        elif name.isdigit():
            print("please input a valid name")
        # if both the other if statements are false then this is will run
        else:
            print('Name:' + name)
            break

ticket_holder_name()
