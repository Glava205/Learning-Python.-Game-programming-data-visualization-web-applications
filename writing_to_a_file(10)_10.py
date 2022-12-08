filename='text.txt'

with open(filename) as f_obj:
	contents=f_obj.read()

words=contents.split()

counter=words.lower().count('the')

print(counter)
