names = ['Gauss', 'Natsume Sousesi', 'Vaundy']
for name in names:
    print(f"{name}, I would be delighted if you could join me for dinner.")
print(f"{names[0]} can't be there")
names[0] = 'xQc'
for name in names:
    print(f"{name}, I would be delighted if you could join me for dinner.")

names.insert(0,'zmjjKK')
names.insert(2,'Yorushika')
names.append('Fujii Kaze')
for name in names:
    print(f"{name}, I would be delighted if you could join me for dinner.")

print(f'{len(names)} guests are invited')

print('I can only  invite 2 guests to have dinner.')
while len(names) > 2:
    popped_name = names.pop()
    print(f'{popped_name}, sorry I can\'t have dinner with you')
for name in names:
    print(f"{name}, I would be delighted if you could join me for dinner.")
del names[0]
del names[0]
print(names)