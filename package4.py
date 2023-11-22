from tabulate import tabulate

data = [
    ["Alice", 25, "Engineer"],
    ["Bob", 30, "Manager"],
    ["Charlie", 22, "Designer"],
]

headers = ["Name", "Age", "Occupation"]

table = tabulate(data, headers, tablefmt="grid")

print(table)


data2 = [
    ["Alice", 25, "Engineer"],
    ["Bob", 30, "Manager"],
    ["Charlie", 22, "Designer"],
]

headers2 = ["Name", "Age", "Occupation"]

table2 = tabulate(data2, headers2, tablefmt="grid", numalign="center", stralign="left", showindex=True)

print(table2)
