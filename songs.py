# credit to https://onlinesequencer.net/3235812#t613
# 4/4
# main_low 1-8 four measures each
main_low = ['d5:1', 'd5:1', 'd6:1','r:1',
              'a5:2','r:1','g#5:1',
              'r:1','g5:1','r:1','f5:2',
              'd5:1','f5:1','g5:1']
main_low+= ['c5:1', 'c5:1', 'd6:1','r:1',
              'a5:2','r:1','g#5:1',
              'r:1','g5:1','r:1','f5:2',
              'd5:1','f5:1','g5:1']
main_low+= ['b4:1', 'b4:1', 'd6:1','r:1',
              'a5:2','r:1','g#5:1',
              'r:1','g5:1','r:1','f5:2',
              'd5:1','f5:1','g5:1']
main_low+= ['a#4:1', 'a#4:1', 'd6:1','r:1',
              'a5:2','r:1','g#5:1',
              'r:1','g5:1','r:1','f5:2',
              'd5:1','f5:1','g5:1']

# main_high 9-16 four measures each
main_high = ['d6:1', 'd6:1', 'd7:1','r:1',
              'a6:2','r:1','g#6:1',
              'r:1','g6:1','r:1','f6:2',
              'd6:1','f6:1','g6:1']
main_high+= ['c6:1', 'c6:1', 'd7:1','r:1',
              'a6:2','r:1','g#6:1',
              'r:1','g6:1','r:1','f6:2',
              'd6:1','f6:1','g6:1']
main_high+= ['b5:1', 'b5:1', 'd7:1','r:1',
              'a6:2','r:1','g#6:1',
              'r:1','g6:1','r:1','f6:2',
              'd6:1','f6:1','g6:1']
main_high+= ['a#5:1', 'a#5:1', 'd7:1','r:1',
              'a6:2','r:1','g#6:1',
              'r:1','g6:1','r:1','f6:2',
              'd6:1','f6:1','g6:1']

# second_low 17-20 four measures each
second_low = ['d#6:1','f6:1','f6:1','f6:2',
              'f6:2','f6:2',
              'd6:2',
              'd6:5']
second_low+= ['f6:2','f6:1','f6:2',
              'g6:2','g#6:2',
              'g6:1','f6:1','d6:1',
              'f6:1','g6:3']
second_low+= ['f6:2','f6:1','f6:2',
              'g6:2','g#6:2',
              'a6:2','c7:2',
              'a6:3']
second_low+= ['d7:2','d7:2',
              'd7:1','a6:1','d7:1',
              'c7:4',
              'g7:5']

# second_high 21-24 four measures each
second_high = ['a6:2','a6:1','a6:2',
               'a6:2','a6:2',
               'g6:2',
               'g6:5']
second_high+= ['a6:2','a6:1','a6:2',
               'a6:2','g6:2',
               'a6:2','d7:2',
               'a6:1','g6:2']
second_high+= ['d7:2','a6:2',
               'g6:2','f6:2',
               'c7:2','g6:2',
               'f6:2','e6:2']
second_high+= ['a#5:2','c6:1',
               'd6:2','f6:2',
               'c7:5',
               'f5:1','d5:1','f5:1','g5:1']

# transition 25-28 33-36 four measures each
transition = ['r:4',
              'r:4',
              'f6:1','d6:1','f6:1','g6:1',
              'g#6:1','g6:1','f6:1','d6:1']
transition+= ['g#6:1','f6:1','f6:2',
              'g6:4',
              'r:5',
              'g#6:2','a6:1']
transition+= ['c7:2','a6:1','g#6:1',
              'g6:1','f6:1','d6:1','e6:1',
              'f6:2','g6:2',
              'a6:2','c7:2']
transition+= ['c#7:2','g#6:2',
              'g#6:1','g6:1','f6:1',
              'g6:5',
              'r:4']

# buildup 29-32 37-40 four measures each
bdup = ['f5:2','g5:2',
        'a5:2','f6:2',
        'e6:4',
        'd6:4']
bdup+= ['e6:4',
        'f6:4',
        'g6:4',
        'e6:4']
bdup+= ['a6:8',
        'a6:1','g#6:1','g6:1','f#6:1',
        'f6:1','e6:1','d#6:1','d6:1']
bdup+= ['c#6:8',
        'd#6:8']

# deep 41-48 eight measures each
deep = ['a#4:11','r:1',
        'f5:4']
deep+= ['e5:8',
        'd5:8']
deep+= ['f5:15','r:1']
deep+= ['r:16']
deep+= ['a#4:11','r:1',
        'f5:4']
deep+= ['e5:8',
        'd5:8']
deep+= ['d5:8',
        'd5:1','c#5:1','b4:1',
        'a#4:1','g#4:1','g4:1',
        'f4:1','e4:1']
deep+= ['d4:8',
        'r:8']

# main_no_drop 49-54 one measure each
mnd = ['d4:1', 'd4:1', 'd5:1','r:1',
       'a4:2','r:1','g#4:1',
       'r:1','g4:1','r:1','f4:2',
       'd4:1','f4:1','g4:1']

# drop 55-56 one measure each
drop = ['d4:1','d4:1','f5:2',
        'e5:3','c5:2',
        'e5:2','d5:2',
        'g4:1','a4:1','c5:1']

# bass_pieces 57-70 two measures each
# piece 1
bp1 = ['a#2:2','d4:2',
       'a#2:2','d4:1','a#2:2',
       'a#1:1','d4:2',
       'a#2:2','d4:2']
bp1+= ['c3:2','e4:2',
       'c3:2','e4:1','c3:2',
       'c3:1','e4:2',
       'c3:2','e4:2']
# piece 2
bp2 = ['d3:2','f4:2',
       'd3:2','f4:1','c#3:2',
       'c#3:1','e4:2',
       'c#3:2','e4:2']
bp2+= ['c3:2','e4:2',
       'c3:2','e4:1','b2:2',
       'b2:1','d4:2',
       'b2:2','d4:2']
# piece 3 (could be made one measure but is two for consistency)
bp3 = ['d3:2','f4:2',
       'd3:2','f4:1','d3:2',
       'd3:1','f4:2',
       'd3:2','f4:2']
bp3+= ['d3:2','f4:2',
       'd3:2','f4:1','d3:2',
       'd3:1','f4:2',
       'd3:2','f4:2']

# finisher 73-78 six measures each (could be shortened but this program has enough arrays already)
finisher = ['a#4:1', 'a#4:1', 'd6:1','r:1',
            'a5:2','r:1','g#5:1',
            'r:1','g5:1','r:1','f5:2',
            'd5:1','f5:1','g5:1']
finisher+= ['c5:1', 'c5:1', 'd6:1','r:1',
            'a5:2','r:1','g#5:1',
            'r:1','g5:1','r:1','f5:2',
            'd5:1','f5:1','g5:1']
finisher+= ['d5:1', 'd5:1', 'd6:1','r:1',
            'a5:2','r:1','g#5:1',
            'r:1','g5:1','r:1','f5:2',
            'd5:1','f5:1','g5:1']
finisher+= ['d5:1', 'd5:1', 'd6:1','r:1',
            'a5:2','r:1','g#5:1',
            'r:1','g5:1','r:1','f5:2',
            'd5:1','f5:1','g5:1']
finisher+= ['a#4:1', 'a#4:1', 'd6:1','r:1',
            'a5:2','r:1','g#5:1',
            'r:1','g5:1','r:1','f5:2',
            'd5:1','f5:1','g5:1']
finisher+= ['c5:1', 'c5:1', 'd6:1','r:1',
            'a5:2','r:1','g#5:1',
            'r:1','g5:1','r:1','f5:2',
            'd5:1','f5:1','g5:1']

# assembling the song
megalovania = []
megalovania+= main_low+main_low # 1-8
megalovania+= main_high+main_high #m9-16
megalovania+= second_low # 17-20
megalovania+= second_high # 21-24
megalovania+= transition # 25-28
megalovania+= bdup # 29-32
megalovania+= transition # 33-36
megalovania+= bdup # 37-40
megalovania+= deep # 41-48
megalovania+= mnd+mnd+mnd+mnd+mnd+mnd # 49-54
megalovania+= drop+drop #55-56
megalovania+= bp1+bp2+bp1+bp3+bp1+bp2+bp1 # 57-70
megalovania+= mnd+mnd # 71-72
megalovania+= finisher

# I could automate this in the future
# credit to https://onlinesequencer.net/3221969#t251
# 3/4
# okay I'm not gonna be as heavy with the labels
# this song is short enough to not be a problem
# and I need to finish this
a = ['f#6:2','f6:2','d#6:2',
     'c#6:2','d#6:2','a#5:2']
a+= ['c6:2','r:2','g#5:2',
     'r:2']
b = ['d#6:2','f6:2','f#6:4',
     'g#6:4','c#7:4','a#6:12']
c = ['d#5:2','f5:2','f#5:4',
     'f5:4','c#5:4','d#5:12']

# 17
x = ['g#6:2','f#6:2','e6:2',
     'd#6:2','c#6:2','e6:2']
# 18
x+= ['d#6:4','a#5:4','a#5:2','d#6:2']
# 19
x+= ['g#6:2','f#6:2','e6:2',
     'd#6:2','c#6:2','e6:2']
# 20
x+= ['d#6:8','d#5:2','g#5:2']
# 21
x+= ['c#6:2','c6:2','a#5:2',
     'g#5:2','a#5:2','c6:2']
# 22
x+= ['a#5:4','d#5:4','d#5:2','f5:2']

# 23
y = ['f#5:4','b5:4','d#6:4']
# 24
y+= ['d6:12']

# 31
z = ['f#5:4','f5:4','c#5:4']
# 32
z+= ['d#5:12']

determination = []
determination+= a+b+a+c
determination+= a+b+a+c
determination+= x+y+x+z