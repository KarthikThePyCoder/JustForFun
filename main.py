import random
import time

integer = random.randint(1, 1000000000)
print('This is an RNG from 1 to 1 BILLION! Or 10^9. I am not that calm.')
time.sleep(3)
if integer <= 100:
    print(f'Starting small with {integer}. 🤌')
elif integer <= 10000 and integer > 100:
    print(f'Hey, we get bigger now at {integer}! 😄')
elif integer <= 300000 and integer > 10000:
    print(f'Wow, {integer}? Even my bank account cannot reach this level of success!💸')
elif integer <= 1000000 and integer > 300000:
    print(f'{integer}? Now THAT is big!🐘')
else:
    print(f'The number {integer} is incredibly massive, that I will need scientific notation.🧮')