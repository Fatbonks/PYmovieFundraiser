def snack():
    while True:
        ans = input('Want Snack').lower()
        if ans == 'yes' or ans == 'y':
            while True:
                ans2 = input('Snack: ').lower()
                if ans2 == 'salad':
                    print("Invalid Choice use a snack that is allowed")
                elif ans2 == '1.5 water':
                    print('Invalid Number please use a whole number')
                elif ans2 == '5 chips':
                    print('Snack number too high')
                elif ans2 == '2':
                    print('Snack ordered: 1 popcorn, 2 M&M, 4 Candy')
        elif ans == 'no' or ans == 'n':
            print('Snack ordered: NONE')
        else:
            print('please enter yes or no')

snack()
