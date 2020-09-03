n = int(input("Enter the length of the sequence: ")) # Do not change this line
#The sequence for the algorythm is 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
#Idea: i + 2 power of i
#Algorithm adds up last 3 inputs and returns the sum of it
#Make a list with first 3 inputs which are already determined
#Print out the first 3 on the screen and then use a storage variable to keep the first 3 inputs
listi = [1,2,3]
for i in range(0, n):
    if i < 3: #Check through the list and print out first 3 numbers
        if i != n-1: #If lenght of sequence is not over then keep on adding ','
            print(listi[i], end=", ")
        else: print(listi[i]) #Print out storage without ','
    else: #Print out the rest until lenght of the sequence is finished
        storage = sum(listi)
        listi = listi[1:] + [storage] #Adds last number in list and adds it to storage variable
        if i != n-1: #If lenght of sequence is not over then keep on adding ','
            print(storage, end=", ")
        else: print(storage) #Print out storage without ','