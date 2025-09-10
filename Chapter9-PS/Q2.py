# The game() function in a program lets a user play a game and returns the score as an integer.
# You need to read a file 'Hi-score.txt' which is either blank or contains the previous Hi-score
# Hi-score. You need to write a program to update the Hi-score whenever the game() function
# breaks the Hi-score


def game():
    return 20

with open("Hi-score.txt",'+w') as f:
    hi_Score=f.readline()
    new_Score=game()
    if(hi_Score!=''):
       if(int(hi_Score) < new_Score):
          f.write(new_Score)
    else:
        f.write(str(new_Score))