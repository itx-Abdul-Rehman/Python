# write a program to print twinkle twinkle little star 
import pyttsx3

print('Twinkle, Twinkle, little, star,')
print('How I Wonder what you are!')
print('Up above the world so high,')
print('Like a diamond in the sky.\n')

print('When the blazing sun is gone,')
print('When he nothing shines upon,')
print('Then you show your little light,')
print('Twinkle, twinkle, all the night.\n')

print("Then the trav'ller in the dark,")
print('Thanks you for your tiny spark,')
print('He could not see which way to go,')
print('If you did not twinkle so.\n')

print('In the dark blue sky you keep,')
print('And often through my curtains peep,')
print('For you never shut your eye,')
print('Till the sun is in the sky.\n')

print('As your bright and tiny spark,\nLights the trav’ller in the dark,\nThough I know not what you are,\nTwinkle, twinkle, little star.')

voice=pyttsx3.init()

voice.say('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.
Then the trav’ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.
In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye,
Till the sun is in the sky.
As your bright and tiny spark,
Lights the trav’ller in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.''')

voice.runAndWait()
