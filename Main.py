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
    while True:
        ans = input('Want Snack?: ').lower()
        if ans == 'yes' or ans == 'y':
          
        elif ans == 'no' or ans == 'n':
            print('Snacks order: NONE')
            break

        else:
            print('please enter yes or no or y/n')


valid_snacks = ['popcorn', 'm&m', 'candy', 'EOF']
snacks_ordered = []
names = []
age = []
max_tickets = 150
tickets_sold = 0
while True:
    print()
    try:
        amount_of_people = int(input("How many people will be buying a ticket?: "))
    except ValueError:
        print("")
    for i in range(amount_of_people):
        get_name()
        get_age()

    print(names)
    print(age)
