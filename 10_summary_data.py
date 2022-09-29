import pandas as pd

Names = ['Rangi', 'Manaia', 'Talia', 'Arihi', 'Fetu']
Ticket = [7.5, 10.5, 10.5, 10.5, 6.5]
snacks = [12.75, 0.00, 2.00, 5.75, 17.25]
subtotal = [20.25, 10.50, 12.50, 16.25, 23.75]
surchare = [0.0, 0.0, 0.0, 0.0, 0.0]
toalt = [20.25, 10.50, 12.50, 16.25, 23.75]
Item = ['popcorn', 'M&M', 'Pita Chips', 'Water', 'OJ', 'Snack profit', 'Ticket profit', 'Total profit']
Amount = [3, 1, 2, 1, 5, 7.55, 20.50, 28.05]
dataframe = pd.DataFrame({
    'Names': Names, 'Tickets': Ticket, 'Snacks': snacks, 'Sub Total': subtotal, 'Surcharge': surchare, 'Total': toalt
})

data = pd.DataFrame({
    'Item': Item, 'Amount': Amount
})

print(dataframe)
print(data)
