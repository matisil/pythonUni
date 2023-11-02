#open just asks to the operating system, I need another thing: 

from urllib.request import urlopen

with urlopen('https://www.gutenberg.org/cache/epub/45334/pg45334.txt') as f:
    
    count_l = 0
    count_r = 0
    
    for line in f:
        if 'Lucia' in str(line):   #we need to change to str bc it is imported in bytes
            count_l=count_l +1
        
        if 'Renzo' in str(line):
            count_r=count_r+1

            
print('Lucia appears ' + str(count_l) + ' times.')
print('Renzo appears ' + str(count_r) + ' times.')        
        
# it wuould be better to have two sequences: one for the things you want to learn and one for the counter
