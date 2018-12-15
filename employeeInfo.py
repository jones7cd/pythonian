import random

chars='abcdefghijklmnopqrstuvwxyz1234567890'
idChars='1234567890'

password=''
password=random.choice(chars)
for c in range(10):
  password+=random.choice(chars)
idNumber=''
idNumber=random.choice(idChars)
for c in range(8):
  idNumber+=random.choice(idChars)


class Employee:
  def __init__(self, first, last):
    self.first = first
    self.last = last
    self.email = first + '.' + last + '@isatjmu.com'
    self.user = first + '.' + last
  def fullname(self):
    return '{} {}'.format(self.first, self.last)

e1 = Employee('Chris', 'Jones')
e2 = Employee('Austin', 'Fairchild')

print('Name:',Employee.fullname(e1))
print('Email:',e1.email)
print('Username:', e1.user.lower())
print('Password:', password)
print('Employee ID:', idNumber)


