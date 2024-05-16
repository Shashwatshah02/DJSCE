#Ammortized Method - Accounting Method
def accounting(n):
    size = 1
    total = 0
    dcost = 0
    icost = 0
    bank = 0
    print("Elements\tDoubling Copying Cost\tInsertion Cost\tTotal Cost\tAmortized Cost\t\tBank\t\tSize")
    for i in range(1, n + 1):
        icost = 1
        if i > size:
            size *= 2
            dcost = i - 1
        total = icost + dcost
        amortized_cost = 3
        if amortized_cost > total:
            bank += (amortized_cost - total)
        else:
            bank -= (total - amortized_cost)
        print(i, "\t\t", dcost, "\t\t\t", icost, "\t\t", total, "\t\t\t", amortized_cost, "\t\t", bank, "\t\t", size)
        icost = 0
        dcost = 0

n = int(input("Enter number of elements: "))
print("Accounting method")
accounting(n)
