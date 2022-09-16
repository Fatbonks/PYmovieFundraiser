# this gets the ticket holders age #
def ticket_holder_age():
    print("To watch this movie you have to be older than 11")
    while True:
        try:
            ans = int(input("what is your age\n>"))

            if ans < 12:
                print("You are too young to watch this movie")

            elif ans >= 130:

                print("Your age is out of bounds are you sure that is your age?")
            else:
                print("Your age is :", ans)
                break

        except ValueError:
            print("please input a whole number")


ticket_holder_age()
