import math
import argparse

DEBUG = False

# Parser
parser = argparse.ArgumentParser()
# Perimeter list for parser
parser.add_argument("--type", help="type of credit: 'diff' or 'annuity'")
parser.add_argument('--payment', help="monthly payment amount", type=float)
parser.add_argument('--principal', help="the amount of starting credit", type=float)
parser.add_argument('--periods', help="the number of months needed to repay the loan", type=float)
parser.add_argument('--interest', help="specified without a percent sign", type=float)
#parse the argument
args = parser.parse_args()


# Variable assigning and checking parameter
tipe, P, D, n, i = args.type, args.principal, args.payment, args.periods, args.interest
if i != None:
    i /= 1200


if DEBUG == True:
    print(f'Tipe: {tipe}')
    print(f'P: {P}')
    print(f'D: {D}')
    print(f'n: {n}')
    print(f'i: {i}')

# Finally starting to program
def diff_payment():
    payment_total = 0
    for m in range(int(n)):
        D = math.ceil((P / n) + i * (P - ((P * (m))/n)))
        payment_total += D
        print(f'Month {m + 1}: payment is {D}')

    print()
    print(f'Overpayment = {int(payment_total - P)}')
# DONE
def annuity_payment():
    A = math.ceil(((P * i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)))
    payment_total = A * n

    print(f'''Your annuity payment = {A}!
Overpayment = {int(payment_total - P)}''')
#DONE
def annuity_month():
    box = D / (D - i * P)
    n = math.ceil(math.log(box, 1 + i))
    times = divmod(n, 12)
    total_payment = D * n

    if n < 12:
        print(f'It will take {result} months to repay this loan')
    elif n == 12:
        print(f'It will take 1 year to repay this loan')
    elif times[1] == 0:
        print(f'It will take {times[0]} years to repay this loan')
    else:
        print(f'It will take {times[0]} years and {times[1]} months to repay this loan')

    print(f'Overpayment = {int(total_payment - P)}')
#DONE
def annuity_prin():
    box1 = i * math.pow(1 + i, n)
    box2 = math.pow(1 + i, n) - 1
    box = box1 / box2
    P = int(D / box)
    total_payment = D * n

    print(f'Your loan principal = {P}!')
    print(f'Overpayment = {int(total_payment - P)}')
#DONE
if tipe == 'diff' and P != None and n != None and i != None:
    diff_payment()
elif tipe == 'annuity' and P != None and i != None and n != None:
    annuity_payment()
elif tipe == 'annuity' and D != None and i != None and P != None:
    annuity_month()
elif tipe == 'annuity' and i != None and n != None and D != None:
    annuity_prin()
else:
    print('Incorrect parameters')
