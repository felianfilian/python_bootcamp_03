from prettytable import PrettyTable

def start():
    table = PrettyTable()
    table.add_column("Pokemon Name", ["Pikachu", "Bisasam", "Glurak"])
    table.add_column("Pokemon Type", ["electric", "flower", "fire"])
    table.align = "l"
    print(table)
