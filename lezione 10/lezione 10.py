f= open('foo.txt','wt')
'''you shall give a name, it could be a path but if you use a path the program will depend
on the path structure so it may not work on anotther machine
using the foo. you tell him, use the same folder of the running program and you resolve the situation
-->not sure about the foo. , check

adding " ,'w' " means: please open the file in a writing mode. if you want to start at the end of what's already there you need:
'w+'
or 'a' for append which is even better
you can sum these commands
.txt is a convention

'''
f.write('Hello world!\n')

f.close()
