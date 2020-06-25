# the list "walks" is already defined
# your code here
total = sum(w['distance'] for w in walks)
avg = total // len(walks)
print(f'{avg}')
