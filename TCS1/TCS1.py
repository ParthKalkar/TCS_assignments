#Parth Kalkar, BS-19-02

# This is the implementation of first task of the TCS final
# In this task we check if the input is an element of the set Λ of lambda-terms defined by the grammar: Λ ::= V | (Λ)Λ | \V.Λ

# I am using the Stack data structure by using the in built list methods pop() and append()
# Also I need to create the method peek to get the first element of my stack

#Function to find the first element of the stack
def peek(stack):
    if stack == []:
        return None
    else:
        s = stack.copy()
        return s.pop(0)


# Initialsing the beta redex
beta = 0

# Function to check if the lambda expression is valid 
def checkLambda(str):
    
    # If the string is empty return false
    if str == "()":
        return False
    if str == "":
        return False
    # Declaring beta and initialising the boolean variables first, second and third
    # The booleans first, second and third correspond to the relevant cases to solve the problem
    global beta
    first = False
    second = False
    third = False

    # If the function correctName is true then set first as true
    if (correctName(str)): first = True

    # If the first character of the string is opening bracket then perform the following tasks
    if (str[0] == '('): 
        
        # Initialising count
        count = 1
        # This is the condition for finding beta
        if str[1] == '\\':
            
            # Beta is the beta redex
            beta = beta + 1
        for i in range (1,len(str)): # Iterating over the string
            if (str[i] == '('): count = count + 1  # If first character is openning bracket then increment count
            if (str[i] == ')'): count = count - 1  # If first character is closing bracket then decrement count
            
            # Following statements are for creating substrings
            if (count == 0):
                s1 = ""
                for j in range (1, i):
                    s1 += str[j]
                s2 = ""

                for j in range (i+1, len(str)): 
                    s2 += str[j] 

                if (len(s1) == 0 or len(s2) == 0):
                    second = False
                else:
                    if checkLambda(s1) and checkLambda(s2): second = True
                i = len(str)
                break
    
    # This if statement is for the third case
    if (ord(str[0]) == 92):
        # Initialisng the substrings
        s1 = ""
        s2 = ""
        for i in range (2, len(str)):
            if (str[i] == '.'):
                for j in range(1,i):
                    s1 += str[j]

                for j in range(i + 1,len(str)):
                    s2 += str[j]

                if (len(s1) == 0 or len(s2) == 0):
                    third = False
                else:
                    if (correctName(s1) and checkLambda(s2)):
                        third = True

                i = len(str) # Setting i equal to string length

    return first or second or third # Returning the boolean 

# Function to test the characters present in our expression
def correctName(str):
    result = True
    for i in range(len(str)): # Iterating over the string and checking if the each character present in our string is bounded 
        if (not ((ord(str[i]) >= 65 and ord(str[i]) <= 90) or (ord(str[i]) >= 97 and ord(str[i]) <= 122) or (ord(str[i]) >= 48 and ord(str[i]) <= 57))): 
              return False # If this statement holds then return false
    return True # Else we return true

# Function to check if our expression is balanced, this means checking if both the parenthesis are present
def checkBalance(str):
    para = [] # Here, para is my list of parenthesis 
    for i in range (len(str)):
        if (str[i] == '('): para.append('(') # If the first character is opening parenthesis then add that to the list 
        else: # Else if it is closing parenthesis then end the program by returning false
            if (str[i] == ')'):
                if (len(para) == 0): return False # This is to find if the list already contains some characters, if not then return false
                else:
                    if (peek(para) == '('): para.pop(); # If the first element of the list is an opening parenthesis then pop it
                    else: para.append(')') # Else add the closing parenthesis to the list

    if (len(para) == 0):  return True # If at last the list is empty then return true
    return False # Else return false

#Creating the input and output files 
input = open("input.txt", "r")
output = open("output.txt", "a")
open("output.txt", "w").close()

# Reading through the input file
string = input.readline()


# If checkBalance is not true then we print No and then close the file
if (not(checkBalance(string))) : 
   output.write("NO\n")
   output.close()

# If checkLamda is true then we print Yes, beta redex and then close the file
elif (checkLambda(string)):
   output.write("YES\n")
   output.write(str(beta) + "\n")
   output.close()

# Lastly, if nothing works then print No and close the file 
else : 
   output.write("NO\n")
   output.close()