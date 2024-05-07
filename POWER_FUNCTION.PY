
def power(base,exponent):#this is the function which is defined with two positional arguments
    if exponent == 0 :#if the exponent of any base is zero then the outcome will be always 
        return 1
    if exponent > 0:# this calculates the power of the function if the exponent is greater than zero 
        return base*power(base , exponent-1)# this step calls the function within it self till the exponent becomes zero till the exponents becomes zero and finally ends the functiom
    else:#this helps in calculating the power of base with negative exponents 
        return 1/(power(base, -exponent))#this recursion function sends the base and exponent to the part of calculation of base of positive exponent while keeping the answer in denomenator

a=2#base
b=999 #exponent
try:# during the recursion process there are chances that the recursion depth is exceeded which is the no of times the function can reoccur in itself which is equal to 998 in this code 
    r=power(a,b)#calling the function power to calculate the power of base(a) with exponent(b)
    print(r)
except RecursionError as e:#to solvethis we canuse try and except method so that the codedont get crashed 
    print("maximum recursion depth exceded")
finally: 
    print("thank you ")

