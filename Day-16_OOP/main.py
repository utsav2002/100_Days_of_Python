from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Pokemon Type", ["Electric", "Water", "Fire"])

table.align["Pokemon Name"] = "l"
table.align["Pokemon Type"] = "l"

print(table)
