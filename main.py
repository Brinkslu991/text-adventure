# Lucas Brinks
# 11/125/24
# Text Adventure
from time import sleep
import sys

lives = 3
score = 0

walmart_bag = ['key','duck','brush']

def lives_score():
    print('*******************************************')
    print(f'You have {lives} left.')
    print(f'Your score is {score}')
    print(f'The walmart bag contains {walmart_bag}')
    print('*******************************************')

def game_over():
    if lives <= 0:
        print(f'You have failed {name}')
        print('GAME OVER')
        lives_score()
        sys.exit()


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

choice1 = input('Press Q to run away or E to push her into the pot.: ')
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

choice2 = input('Press Q to pet the bunny, press P to punt that thing like a football, or press R to run from the small bunny.: ')
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

# Scene 3

print('As you make your way farther forest you feel something sralking you and watchiung you.')
print()
sleep(2)
print('You hear a low growl coming from the darkness.')
print()
sleep(1)
print('You start to run, weaving through the trees, and jumpig over roots. You see a cabin up ahead and it looks safe.')
print()
sleep(1)
print('You try the door but it\'s locked and the eyes in the darkness are getting closer.')
print()
print('You find a Walmart bag next to the door.')
print('Maybe something in your bag can help.')
print()
print(f'You look in your bag and find: {walmart_bag}')

# choice 3
choice3 = input('Press K to use the key, press D to use the duck to buy you some time, or press B to throw the brush at the monster in the darkness.: ')
choice3 = choice3.lower()
if choice3 == 'k':
    print('Somehow to your insane luck the key fits and you get into the house.')
    score = score + 1
    walmart_bag.remove('key')
elif choice3 == 'd':
    print('You throw the duck at the creature and square up with it. You start hitting the monster with a mortal combat like combo. You raise your arm victorious after your battle and kick down the door to the cabin and walk inside.')
    score = score + 5
    walmart_bag.remove('duck')
else:
    print('You throw the brush at the monster and it dies nothing. It leaps out of the darkness and it rips you apart for a gruesome death.')
    lives = lives -1
    walmart_bag.remove('brush')
    game_over()

lives_score()

# Scene 4

print('You step inside the cabin and it seems that someone lives here. It\'s well decorated and the place is clean.')
print()
sleep(1)
print('You look around the room and see a cake on the table and you are rather hungry. There is knife next to the cake you figure it wouldn\'t hurt to take a slice.')
print()
sleep(2)

# choice 4

choice4 = input('Press E to eat the cake now or press B to put it in your bag and save it for later.: ')
choice4 = choice4.lower()

if choice4 == 'e':
    print('You slice the cake to it turns out the is a pruessure bomb under the cake and you blow up.')
    lives = lives-1
    game_over()
else:
    print('You put the cake in you walmart bag and save it for later.')
    walmart_bag.append('cake')

lives_score()

# Scene 5

print('The door opens and a frail looking old man walks in. He is surprised to see you in his house.')
print()
sleep(1)
if 'cake' in walmart_bag:
    print('The man asks if you took the cake.')
    sleep(1)
    print('You stand your gound and nod.')
    sleep(1)
    print('The man is impressed by you confidence and lets you go.')
    score = score + 10
else:
    print('An old man enters the cabin seeing that his cake trap worked.')
    sleep(1)
    print('He cleans up the mess you made and throws your body out of his house.')

lives_score()

print(f'You wake from the nightmare that ahd trapped you and realize that all of this was a bad dream {name}.')
sleep(2)
print('Also you need to leave for work your going to late.')
sleep(1)
lives_score()
sleep(1)
print('THE END')
