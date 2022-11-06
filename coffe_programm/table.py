from prettytable import PrettyTable

table = PrettyTable()

table.add_column('Pokemon Name',['Pikatchu', 'Squirtle','charmander'])
table.add_column('Type',["electtic", 'water', 'fire'])
table.align = 'l'
print(table)