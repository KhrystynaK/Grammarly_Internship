'''
Opens the file with the nouns and their attributes
searches only for the uncountable nouns,
then writes them into a new txt file
'''
my_file=open('CountOrUncount.txt')
f=open('Uncount.txt','a')
raw=my_file.read()

for i in raw.split():
    if i[-12:]=='-uncountable':
        f.write(i[:-12]+'\n')
            
f.close()

