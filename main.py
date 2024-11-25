# Lucas Brinks
# 11/125/24
# Text Adventure
from time import sleep

lives = 3
score = 0

walmart_bag = ['key','duck','brush']

def lives_score():
    print('***********************')
    print(f'You have {lives} left.')
    print(f'Your score is {score}')
    print('***********************')

name = input('Please enter your name: ')
name = name.capitalize()
print(F'Welcome {name} to the adventure.')
print()
print()
lives_score()
print()
sleep(2)

# Scene 1
print('You awake to the sound of an Turbo Granny cooking in her pot.') 
print()
sleep(1)
print('She is singing an old song about cooking.')
print()
sleep(1) 
print('...I think she is about to cook you!')

# Choice 1

choice1 = input('Press q to run away or e to push her into the pot.: ')
choice1 = choice1.lower()
if choice1 == 'q':
    print('Turbo Granny catches you puts you in the pot.')
    lives = lives - 1
else:
    print('You dropkick Turbo Granny into the pot and burn the soup.')
    score = score + 5

lives_score()

# Scene 2
print('you move further into the forest. It is full of strange and frightning sounds. You can hear wolves howling and demons screaching. How much longer before one of them finds you?')
sleep(2)
print()

print('The demons are closing in.')
sleep(1)
print()
print('The demon runs at you and turns out to be a bunny.')
print()
print()
# choice 2

choice2 = input('Press q to pet the bunny, press p to punt that thing like a football, or press r to run from the small bunny.: ')
choice2 = choice2.lower()
if choice2 == 'q':
    print('You lean down to pet the bunny and it blows up in a fiery explosion.')
    lives = lives - 1
elif choice2 == 'p':
    print('You pick up the fluffy bunny and wind your leg back and punt that bunny into the sky and watch it explode like a fire work on the 4th of July.')
    score = score + 5
else:
    print('You try to run away from the bunny and run straight into a tree and then a pack of wolves find you and eat you.')
    lives = lives - 1

lives_score()
