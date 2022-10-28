def get_age():
    while True:
        try:
            ans = int(input("What is your age: "))
            age.insert(len(names), ans)
            break
        except ValueError:
            print("please input a number")


def get_name():
    ans = input("What is your name: ")
    names.insert(len(names), ans)


def want_snack():
    valid_snack = False
    valid_amount = False
    amount = 0
    while True:
        ans = input('Want Snack?: ').lower()
        if ans == 'yes' or ans == 'y':
            while True:
                valid_snack = False
                valid_amount = False
                ans2 = input("Snack: ").lower()

                if ans2 == "xxx":
                    break

                snack = ans2[1:].strip()
                if ans2[0].isdigit():
                    amount = int(ans2[0])
                    valid_amount = True

                elif ans2[0] == " ":
                    valid_amount = True
                    amount = 1

                for i in range(len(valid_snacks)):
                    if snack == valid_snacks[i]:
                        valid_snack = True

                if valid_snack and valid_amount:
                    snacks_ordered.insert(len(snacks_ordered), ans2[1:].strip())
                    snacks_ordered_amount.insert(len(snacks_ordered_amount), amount)

                if not valid_amount:
                    print("you have not inputted a valid number ")
                    continue

                if not valid_snack:
                    print("what you have inputted is not a valid snack")
                    continue
        elif ans == 'no' or ans == 'n':
            if len(snacks_ordered) > 0:
                pass
            else:
                print('Snacks order: NONE')
            break

        else:
            print('please enter yes or no or y/n')


valid_snacks = ['popcorn', 'm&m', 'candy']
snacks_ordered = []
snacks_ordered_amount = []
snacks = []
snack_amount = []
names = []
age = []

max_tickets = 150
tickets_sold = 0

while True:
    get_name()
    get_age()
    want_snack()

    print(names)
    print(age)
    print(snacks_ordered)
    print(snacks_ordered_amount)
