n = int(input("Enter the length of the sequence: ")) # Do not change this line
first_input = 1
second_input = 2
sum = 0
#The sequence for the algorythm is 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
#Algorithm adds up last 3 inputs and returns the sum of it
for i in range(1, n+1):
    while sum != 3:
        if sum == 0:
            print(first_input, end=", ")
            first_input += first_input
            sum += first_input
        elif sum == 1:
            print(second_input, end=", ")
            sum += second_input
        else:
            sum = sum + (first_input + second_input)
            print(sum, end=", ")