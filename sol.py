def diff(price, tot_items, tot_emp):  # To find the diff between elements
    # Variable Declaration

    minimum = 0
    prev = 999999
    high = 0
    low = 0

    print("Here the goodies that are selected for distribution are: \n")
    for i in range(tot_items - tot_emp + 1):
        minimum = min(prev, price[i + tot_emp - 1][1] - price[i][1])
        if minimum < prev:
            high = i + tot_emp - 1
            low = i
        prev = minimum

    return high, low, minimum


items = {}
# extracting input file
with open("input.txt") as f:
    for line in f:
        (key, val) = line.split(": ")
        items[key] = int(val)
sort_items = sorted(items.items(), key=lambda x: x[1])

# Total Goodies
tot_items = len(items)

# Total employees
tot_emp = int(input("Enter no. of employee: \n"))

high, low, minDiff = diff(sort_items, tot_items, tot_emp)

for i in range(low, high + 1):
    print(sort_items[i])

print('And the difference between the chosen goodie with highest price and the lowest price is : {}'.format(minDiff))

# writing to output.txt
textfile = open("output.txt", "w")
textfile.write("Enter no. of employee:")
textfile.write(str(tot_emp))
textfile.write("\n")
for i in range(low, high + 1):
    textfile.write(str(list(sort_items[i])))
    textfile.write("\n")
textfile.write('And the difference between the chosen goodie with highest price and the lowest price is : {}'.format(minDiff))
textfile.close()