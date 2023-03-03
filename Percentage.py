#GRADE CALCULATOR
#NOTE PG MIDTERM 30% AND FINAL 70%
#UG MIDTERM 40% AND FINAL 60%
# Get the first input from the user and convert it to an integer
input1 = int(input("Enter the first input: "))

# Get the second input from the user and convert it to an integer
input2 = int(input("Enter the second input: "))

# Calculate the percentages
percent1 = input1 * 0.3
percent2 = input2 * 0.7

# Calculate the total value of the inputs as percentages
total = percent1 + percent2

# Print the inputs, their corresponding percentages, and the total value
print("The first input is:", input1)
print("The first input as a percentage is:", percent1)
print("The second input is:", input2)
print("The second input as a percentage is:", percent2)
print("The total value of the inputs as percentages is:", total)

# Ask the user if they want to input new values
response = input("Do you want to input new values (Y/N)? ")

# If the user wants to input new values, repeat the process
while response == "Y":
    # Get the first input from the user and convert it to an integer
    input1 = int(input("Enter the first input: "))

    # Get the second input from the user and convert it to an integer
    input2 = int(input("Enter the second input: "))

    # Calculate the percentages
    percent1 = input1 * 0.3
    percent2 = input2 * 0.7

    # Calculate the total value of the inputs as percentages

    # Calculate the total value of the inputs as percentages64
    total = percent1 + percent2

    # Print the inputs, their corresponding percentages, and the total value
    print("The first input is:", input1)
    print("The first input as a percentage is:", percent1)
    print("The second input is:", input2)
    print("The second input as a percentage is:", percent2)
    print("The total value of the inputs as percentages is:", total)

