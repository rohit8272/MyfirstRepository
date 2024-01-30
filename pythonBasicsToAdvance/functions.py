# def demo_routine(num):
#  print('I am a demo function')
#  if num % 2 == 0:
#     return True
#  else:
#     return False

# num = int(input('Enter a number:'))
# if demo_routine(num) is True:
#  print(num, 'is an even number')
# else:
#  print(num, 'is an odd number')



def checkEvenOdd(num):
    if num%2 == 0:
        return True
    else: 
        return False
    


num = int(input("enter num value :"))

check = checkEvenOdd(num)
if check is True:
    print(num , " is even number")
else:
    print(num ," is a odd number")

