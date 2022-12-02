msg = "Enter your Age: "
msg2 = "\nEnter 'quit' when you want to stop asking ticket price.\n"
print(msg2)

while True:
   age = int(input(msg))
   if age != 'quit':
       if age < 3:
           print('you get free ticket')
       elif age < 13:
           print('Your ticket price is $10')
       else:
           print('Your ticket price is $15')
   else:
       break




