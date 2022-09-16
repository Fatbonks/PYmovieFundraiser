def want_snack():
    invalid = True
    snacks = ['popcorn', 'm&m', 'candy', 'EOF']
    snacks_ordered = []
    while True:
        ans = input('Want Snack?: ').lower()
        if ans == 'yes' or ans == 'y':
            while True:
                ans2 = input('Snack: ').lower()
                for i in snacks:
                    if i == ans2:
                        print('Snack Choice: {}'.format(ans2))
                        snacks_ordered.insert(0, ans2)
                        break
                    elif ans2 == '2':
                        print('Snack Ordered: ')
                        for s in snacks_ordered:
                            print(s)
                        return
                    elif i == 'EOF':
                        print('Snack Choice: invalid Choice')
                        break  # Breaking to prevent continuation if candies put after EOF
        elif ans == 'no' or ans == 'n':
            print('Snacks order: NONE')
            break
        else:
            print('please enter yes or no or y/n')


want_snack()
