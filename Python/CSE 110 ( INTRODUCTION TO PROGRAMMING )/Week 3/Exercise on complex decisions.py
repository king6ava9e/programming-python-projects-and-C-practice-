#prompts on a rate of 1-10
print("On a scale of 1 - 10, put is the appropriate value.")
credit_history = int(input("How good is your credit history? "))
down_payment = int(input("How large is your down payment? "))
income = int(input("How high is your income? "))
loan = int(input("How large is the loan? "))
should_loan = False
#Creating if statements
if loan >= 5:
    if credit_history and income >= 7:
        should_loan = True
    if credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            should_loan = True
        else:
            should_loan = False
    if credit_history <7 or income <7:
        should_loan =False
if loan < 5:
    if credit_history < 4:
        should_loan = False
    else:
        if income >=7 or down_payment >7:
            should_loan =True
        if income and down_payment >=4:
            should_loan = True
        else:
            should_loan = False
print()
if should_loan:
    print("The decision is good. you can loan")
else:
    print("The decision is bad, you cannot loan")
    
        
    
        