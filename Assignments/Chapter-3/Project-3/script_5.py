#Mortgage Payment Calculator
#Maxwell Phillips
#3 April 2017
#C Block Programming
#-------------------------------------------------------------------------------
#Algorithm:
#1)Get and store variables for loan amount, term, and range.
#2)Greeting
#3)Calculate discount
#4)Calculate loan amount using discount value
#5)Print it all out in a pretty table
#6)ask to run again
#-------------------------------------------------------------------------------
#Greeting
print("""
This is a program to calculate the monthly mortgage payment for a given loan
 amount, term (number of years) and range of interest rates from 3% to 18%.
""")
#Begin program loop
terminate = False
print("-"*80)
while (terminate == False):
    #Reset variables
    loan_amount = 0
    loan_term = 0
    #Get the loan amount
    while True:
        try:
            loan_amount = int(input("Please enter a amount for the loan: "))
            break
        except ValueError:
            print("Please enter a positive interger value for the amount of",
            "the loan.")
    #Get the loan term
    while True:
        try:
            loan_term = int(input("Please enter a length for the loan: "))
            break
        except ValueError:
            print("Please enter a positive interger value for the term of",
            "the loan.")
    #Calculate discounts and print
    n = loan_term * 12
    r = 3

    #---------------------------------------
    #Ask to use again
    if(input("\nUse Again (y/n)?: ") == "y"):
        terminate = False
        print("="*80)
    else:
        terminate = True
