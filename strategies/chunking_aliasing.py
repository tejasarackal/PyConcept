from random import *

if __name__ == '__main__':
    print(random())
    print(50 + random() * 200) # 3 register
    print(uniform(50, 250)) # 2 registers (chunking)

    print(5000 + int(random() * 200) * 5) # random integer between 5000 & 6000 in steps of 5
    print(randrange(5000, 6000, 5))

    outcomes = ['win', 'lose', 'draw', 'tie', 'match abandoned']
    print(outcomes[int(random() * len(outcomes))]) # more registers
    print(outcomes[randrange(len(outcomes))]) # less registers
    print(choice(outcomes)) # least registers

    print([outcomes[int(random() * len(outcomes))] for _ in range(10)])
    print([choice(outcomes) for _ in range(10)])
    print(choices(outcomes, k=10))