'''
def make_shirt(content, size='M'):
    print(f'This shirt is {size}-size and has {content}')

make_shirt('Sakura', 'XXL')
'''

def make_shirt(content='I love Python', size='L'):
    print(f'This shirt is {size}-size and has {content}')

make_shirt()
make_shirt(size='M')
make_shirt('Love', 'S')