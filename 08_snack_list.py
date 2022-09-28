import pandas as pd

Names = ["Antrish", "Cody", "Robert", "Nova"]
Popcorn = [2, 0, 0, 1]
Water = [1, 2, 0, 0]
M = [3, 0, 0, 0]
Candy = [0, 3, 0, 1]
Tickets = ["$7.50", "$10.50", "$10.50", "$7.50"]
snack_price = ["$12.50", "$6.50", "$0", "$4.00"]
total_price = ["$20.00", "$17.50", "10.50", "$10.50"]
print(Names)
print(Water)
print(M)
print(Candy)
dataframe = pd.DataFrame(
    {
        'Names': Names, 'Tickets': Tickets,  'Popcorn': Popcorn, 'Water': Water, 'M&M': M, 'Candy': Candy,
        'Snack price': snack_price, 'Total': total_price
    })
print(dataframe)
