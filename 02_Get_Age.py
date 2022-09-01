# this gets the ticket holders age #
def ticket_holder_age():
    print("To watch this movie you have to be older than 11")
    while True:
        try:
            ans = int(input("what is your age\n>"))

            if ans < 12 or ans > 120:
                print("your age is invalid you have either entered a age to young or your age is over 120")

            else:
                print("Your age is :", ans)

        except ValueError:
            print("please input a whole number")


ticket_holder_age()
