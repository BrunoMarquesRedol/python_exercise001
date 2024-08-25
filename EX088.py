
import random
for x in range(int(input('Number of games: '))):
    print(f'Game {x+1}: {random.sample(range(1, 60), 6)}')