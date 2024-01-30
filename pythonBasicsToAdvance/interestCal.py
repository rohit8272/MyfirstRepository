print('interest calculater')

amount = float(input('enter the amount:'))
roi = float(input('the interest rate:'))
yrs = int(input('years for interest:'))

total = amount * pow(1+(roi/100) , yrs)
interest = total - amount

print('\nInterest = %0.2f' %interest)

