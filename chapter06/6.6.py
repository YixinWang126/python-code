favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

name_list = ['jen', 'a' , 'b', 'edward']
for i in name_list:
    if i in favorite_languages.keys():
        print(f'Thanks {i}')
    else:
        print(f'Invite {i} to have a survey')