def print_table(table):
    for r in table:
        print("\t".join(str(item) for item in r))

print_table([["X", "Y"], [0, 0], [10, 10], [200, 200]])
print("--------------------------------------------")
print_table([
    ["ID", "Name", "Surname"],
    ["001", "Guido", "Rossum"],
    ["002", "Donald", "Knuth"],
    ["003", "Gordon", "Moore"]
])
