# understanding input
# input("What is your name?!")

# Practical application

# print("Hello " + input("What is your name?!")) this will print a message saying hello to the input name ex: "Hello tito". 

# however in order to make this work the only thing that needs to be printed out is the "len()" of the input:
# input("What is your name?!") <-- turns out that was not needed! only the one bellow was! Thats why the program ran two questions before getting the len.
print(len(input("What is your name?!")))

