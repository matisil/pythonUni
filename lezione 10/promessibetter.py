

from urllib.request import urlopen

with urlopen('https://www.gutenberg.org/cache/epub/45334/pg45334.txt') as f:
    
    search: dict[str,int] = {'Lucia': 0, 'Renzo':0, 'Cristoforo':0, 'Azzecca':0, 'cioccolata':0}
    # i can just add things to the dictionary
    
    
    
    for line in f:
        for name in search:
            if name in str(line):
                search[name] = search[name] + 1
                
for name in search:
    print(name +' appears ' + str (search[name]) + ' times.')
         
#try by urself to use the ENUMERATE function