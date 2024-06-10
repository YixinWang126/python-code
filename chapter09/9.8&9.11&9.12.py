from class_User import User

class Privileges:
    def __init__(self):
        self.privileges = ['I', 'have', 'a', 'pen']
    def show_privileges(self):
        words = ''
        for i in self.privileges:
            words += f'{i}, '
        words = words.removesuffix(', ')
        print(f'Admin has {words}.')


class Admin(User):
    def __init__(self, privileges, first_name, last_name, login_attempts=0):
        super().__init__(first_name, last_name, login_attempts)
        self.privileges = privileges
        self.test = Privileges()

b = Admin(['what', 'is', 'Apple'], 'x', 'y')
b.test.show_privileges()


