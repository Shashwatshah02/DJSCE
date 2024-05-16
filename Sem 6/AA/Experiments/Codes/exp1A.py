# Initialize an empty list to simulate the stack
stack = []
# Initialize the cost counter for operations
cost = 0

# Function to push an item onto the stack
def push(item):
    global cost
    stack.append(item)  # Append the item to the stack
    cost += 1           # Increment the cost counter for pushing
    printstack()        # Print the current stack

# Function to pop an item from the stack
def pop():
    global cost
    if stack:           # Check if the stack is not empty
        stack.pop()     # Remove the top item from the stackw
        cost += 1       # Increment the cost counter for popping
        printstack()    # Print the current stack

# Function to pop k items from the stack
def multipop(k):
    for _ in range(k):  # Iterate k times
        pop()           # Call the pop function to pop an item each time

# Function to print the current stack and the cost
def printstack():
    print(stack, end='')    # Print the stack
    print("\tCost: ", cost)  # Print the current cost

# Function for amortized analysis using the aggregate method
def aggregate_dynamic(n):
    size = 1    # Initialize the size variable for doubling
    icost = 0   # Initialize the insertion cost
    dcost = 0   # Initialize the doubling cost
    totalcost = 0  # Initialize the total cost
    total = 0   # Initialize the total variable

    print("Element\tDoubling Cost\tInsertion cost\tTotal cost")
    # Loop from 1 to n (inclusive)
    for i in range(1, n + 1):
        icost = 1   # Set the insertion cost to 1
        if i > size:  # Check if i is greater than the current size
            size *= 2  # Double the size
            dcost = i - 1  # Calculate the doubling cost
        totalcost = dcost + icost  # Calculate the total cost
        total += totalcost  # Accumulate the total cost
        # Print the current element, doubling cost, insertion cost, and total cost
        print(i, "\t\t", dcost, "\t\t", icost, "\t\t", totalcost, "")
        icost = 0   # Reset the insertion cost
        dcost = 0   # Reset the doubling cost

    return total / n  # Calculate and return the amortized cost per operation

# Get the number of elements from the user
n = int(input("Enter the number of elements: "))

print("Aggregate method")
# Perform the aggregate dynamic analysis and store the result
a = aggregate_dynamic(n)
print("Amortized cost =", a)  # Print the amortized cost per operation
