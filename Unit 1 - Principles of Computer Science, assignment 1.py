# Write your code here

menu = """
Welcome to program 'Main.py' written by student TimurYun (BMC202132729)

Please select problem:
1. Print out the sentence on one line using print
2. Add parenthesis to the expression
4. Bruce variable
5. Compute final amount
6. Division by zero
8. Clock task
"""
print(menu)
problem = input('Please enter number of problem that you want to complete: ')

if problem == '1':
    # Task 1
    # All work and no play makes Jack a dull boy

    print('Problem 1')

    w0 = 'All'
    w1 = 'work'
    w2 = 'and'
    w3 = 'no'
    w4 = 'play'
    w5 = 'makes'
    w6 = 'Jack'
    w7 = 'a'
    w8 = 'dull'
    w9 = 'boy'
    
    print("{} {} {} {} {} {} {} {} {} {}.".format(w0, w1, w2, w3, w4, w5, w6, w7, w8, w9))

  
elif problem == '2':
    print('Problem 2')
    expression = '6 * 1 - 2'

    newexpression = expression.replace('1', '(1').replace('2', '2)')
    newexpressionint = eval(newexpression)
    #It will prints the result of new expression
    print(str(newexpression) + ' = ' + str(newexpressionint))

elif problem == '4':
    print('Problem 4')
    bruce = 6
    print('Bruce = ' + str(bruce + 4))

elif problem == '5':
    print('Problem 5')
    P = 10000
    print('P = ' + str(P))
    n = 12
    print('n = ' + str(n))
    r = 0.08
    print('r = ' + str(r))
    t = input('Please enter amount of years that the money will be compounded for: ')
    t = float(t)
    result = P * (1 + r / n) ** (n * t)
    print("You will recieve  ${:,} after {} years.".format(round(result, 2), t ))
elif problem == '6':
    print('Problem 6')
    print("You can't divide by zero. It's why at last example we got an error.")

elif problem == '8':
  print('Problem 8')
  def twenty_four_hour_format(hour, format):
    #Takes hour in 12-hour format and takes format in 'am, pm'. Returns hour as integer from 0 to 23 that represents 24-hour format
    if hour == 12 and format == 'am':
      return 0
    elif hour == 12 and format == 'pm':
      return 12
    elif format == 'am':
      return hour
    elif format == 'pm':
      return hour + 12
  
      
  def twelve_hour_format(hour_24):
    if hour_24 == 0:
      return "midnight"
    elif hour_24 == 12:
      return "noon"
    elif hour_24 < 12:
      return str(hour_24) + " am"
    elif hour_24 > 12:
      return str(hour_24 - 12) + " pm"
  ct = input('What time is it? \nPlease enter the time rounded to the nearest hour: ')
  format = input('Is it am or pm? : ')
  wt = input('How many hours you have to wait? : ')
  
  #Convert current time to 24-hour format
  ct_in_24_hour_format = twenty_four_hour_format(ct, format)
  #Finding what the time will be on the clock when the alarm goes off
  wait_ends = (int(ct_in_24_hour_format) + int(wt)) % 24
  #Format the output and printing out
  output = twelve_hour_format(wait_ends)
  print('Alarm goes off by {}.'.format(output))
