def potential(n):
    size = 1                    # Initialize the size of the data structure
    total = 0                   # Initialize the total cost
    dcost = 0                   # Initialize the doubling cost
    icost = 0                   # Initialize the insertion cost
    bank = 0                    # Initialize the bank value
    phi = 0                     # Initialize the potential function value
    ci = 0                      # Initialize the change in potential
    phi_prev = 0                # Initialize the previous potential value

    print("Elements\tDoubling Copying Cost\tInsertion Cost\tTotal Cost\t\tBank\t\tSize\t\tPhi\t\tCi")
    for i in range(1, n + 1):   # Loop from 1 to n (inclusive)
        icost = 1               # Set the insertion cost to 1 for each iteration
        if i > size:            # Check if the current element exceeds the current size
            size *= 2           # Double the size
            dcost = i - 1       # Calculate the doubling cost
        total = icost + dcost   # Calculate the total cost as the sum of insertion and doubling costs
        phi = 2 * i - size      # Calculate the potential function value
        ci = total + phi - phi_prev  # Calculate the change in potential
        bank += (3 - total)     # Update the bank based on the difference between 3 and total cost
        # Print the current iteration's details including costs, bank value, size, potential, and change in potential
        print(i, "\t\t", dcost, "\t\t", icost, "\t", total, "\t\t\t", bank, "\t\t", size, "\t\t", phi, "\t\t", ci)
        icost = 0               # Reset the insertion cost for the next iteration
        dcost = 0               # Reset the doubling cost for the next iteration
        phi_prev = phi          # Update the previous potential value for the next iteration

potential(10)   # Call the potential function with n=10 to perform amortized analysis
