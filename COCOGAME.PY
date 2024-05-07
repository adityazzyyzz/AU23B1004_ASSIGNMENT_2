def p1(chocolates):# THIS IS THE FUNCTION WHICH IS DEFINED for p1
    if chocolates == 1:# this is a conditional statement which states that if the value of chocolates is equal to 1 then
        return 1 # the value will return 1 to the start game function 
    else:# this is the else part which will only work if the requirements of if condition does not get fulfilled
        result = p2(chocolates - 1)#here another function is called for the player 2 also here the no opf chocolates is reduced by 1
        return result

def p2(chocolates):# this is the function for player 2
    if chocolates == 2:# this conditional statement will run only if the no of chocolates remaining is 2
        return 2  #this will return 3 to the start_game function 
    elif chocolates == 1:# this conditional statemen will only run if the value of chocolates is =1
        return 2 # this will also return 2 to start_gamefunction
    elif chocolates % 2 == 0:#this checks if the number of choclates remaining is even 
        result = p1(chocolates - 2)# this here is calling a function p1 with argument the no of chocolate -1 
        return result
    else:# if the argument value does not match the above conditional statement the finally this code will be executed
        result = p1(chocolates - 1)# this here is calling a function p1 with the chocolate value -2
        return result

def start_game(chocolates):# this is the final function which begins the code 
    winner = p1(chocolates)# this is calling the function with the argument as chocolate value
    if winner == 1:
        print("Player 1 wins!")# if the returning value from function 1 is 1 then the player one wins
    else:#  if not then player 2 wins 
        print("Player 2 wins!")

chocolates=121
try:# in this blockof code the an error is raised to prevent the code to provide illogical output
    if chocolates<1:# if the value of chocolatesis less than 1 then this line of code will raise error since game cant begin with 0 chocolates 
        raise ValueError (chocolates)
    else:# if the value 
        start_game(chocolates)
except:
    print('The no of chocolates is not enough to start the game')
    print('the input chocolates =',chocolates,' is invalid')

  
