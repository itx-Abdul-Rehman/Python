import random

score=0;
lifes=3
assests=['snake','water','gun']
 
 
def gameProcees(user,computer):
    global score,lifes
    if(assests[user]=='snake'and assests[computer]=='water'):
        score=score+5
        print(f'You Wins, as the snake drinks water')
    elif(assests[user]=='water'and assests[computer]=='snake'):
         lifes=lifes-1
         print(f'You lose, as the snake drinks water')
    elif(assests[user]=='water'and assests[computer]=='gun'):
         score=score+5
         print(f'You win, as the water douses gun')
    elif(assests[user]=='gun'and assests[computer]=='water'):
         lifes=lifes-1
         print(f'You lose, as the water douses gun')
    elif(assests[user]=='gun'and assests[computer]=='snake'):
         score=score+5
         print(f'You win, as the gun shoots snake')
    elif(assests[user]=='snake'and assests[computer]=='gun'):
         lifes=lifes-1
         print(f'You lose, as the gun shoots snake')
    else:
        print('Its, draw')


while(True):
    print('-----------------------Snake Water Gun---------------------------------') 
    if(lifes==0):
        print('Game Over')
        print(f'Your Score {score}')
        break
    
    print(f'1) Snake\t\t\t\tLives: {'❤️ '*lifes}\tScore: {score}')
    print('2) Water')
    print('3) Gun')
    
    
    user=int(input('Select one of them e.g(1,2,3):'))
    if user not in [1,2,3]:
         print("Invalid choice! Please pick 1, 2, or 3.")
         continue
    
    computer=random.randint(0,2)
    gameProcees((user-1),computer)
  
  
