# install an external module and use to it perform an operations

import pyjokes

print('Singal Joke..........')
joke=pyjokes.get_joke();
print(joke)

print('Multiple jokes......')
jokes=pyjokes.get_jokes();

for joke in jokes:
    print(joke)
  
