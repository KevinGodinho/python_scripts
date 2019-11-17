import re

pattern = re.compile(r'[A-Za-z0-9$%#\@]{8,}\d')

password = input('Please enter password: ')

check_password = pattern.fullmatch(password)

if check_password:
  print('Thank you!')
else:
  print('Please type valid password.')
