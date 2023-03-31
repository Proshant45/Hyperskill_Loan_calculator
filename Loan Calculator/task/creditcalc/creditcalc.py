import math
import argparse
# loan_principal = int(input("Enter the loan principal:" ))


parser=argparse.ArgumentParser("")
parser.add_argument("--type",choices=["annuity","diff"])
parser.add_argument("--principal",type=int)
parser.add_argument("--payment", type=int)
parser.add_argument("--periods",type=int)
parser.add_argument("--interest",type=float)


args = parser.parse_args()


typec=args.type
loan_principal = args.principal
monthly_payment = args.payment
loan_interest=args.interest
periods=args.periods
if loan_principal == None:
    print("Incorrect parameters.")
else:
    pass



if typec =="annuity":

    if loan_interest == None:
        print("Incorrect parameters.")
    else:
        nominal_interest = (1 / 12 * (loan_interest)) / 100
        if monthly_payment !=None and loan_principal !=None:
            number_of_payments = math.log((monthly_payment / (monthly_payment - (nominal_interest * loan_principal))),
                                      (1 + nominal_interest))

            year = (round(number_of_payments)) / 12
            fyear = math.floor(year)
            month = math.ceil(number_of_payments % 12)

            if year == 0:
                print("It will take ", month, "months to repay this loan!")
            if month == 0 or month == 12:
                print("It will take ", fyear, "years to repay this loan!")
            else:
                print("It will take", fyear, "years and", month, "months to repay this loan!")
            print("Overpayment =",math.ceil(((math.ceil(number_of_payments))*monthly_payment)-loan_principal))
        else:
             pass
             if monthly_payment!=None:

                somthing = (nominal_interest * (1 + nominal_interest) ** periods) / (((1 + nominal_interest) ** periods) - 1)
                loan_principal = monthly_payment/somthing
                print("Your loan principal =",math.floor(loan_principal),"!")
                print("Overpayment = ",(monthly_payment*periods)-math.floor(loan_principal))
             else:
                 annuity = loan_principal * ((nominal_interest * (1 + nominal_interest) ** periods) / (((1 + nominal_interest) ** periods) - 1))
                 annuity=math.ceil(annuity)
                 print("Your annuity payment =",annuity,"!")
                 print("Overpayment =",((periods*annuity)-loan_principal))

if typec =="diff":
    if loan_interest == None:
        print("Incorrect parameters.")
    else:
        nominal_interest = (1 / 12 * (loan_interest)) / 100
        D = 0
        sumD=0
        for i in range(periods):

            D = (loan_principal/periods) + nominal_interest * (loan_principal - (loan_principal*(i+1-1)/periods))
            print("Month" ,(i+1),":","payment is ",math.ceil(D))
            sumD +=math.ceil(D)
        print("")
        print("Overpayment =",(sumD-loan_principal))








