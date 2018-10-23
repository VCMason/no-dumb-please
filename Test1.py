#This is a python script

print 'This program will make a new file and output some text'

print 'This is for exp1'
print 'This is for exp2'
print 'This is for exp3'
print 'This is for exp3.2'
print 'This is for master challenge'

OUT = open('outputfile.txt', 'w')
OUT.write('Hello bioinformaticians!')
OUT.close()