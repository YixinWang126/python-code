from class_User import User
class Admin(User):
    def __init__(self, privileges, first_name, last_name, login_attempts=0):
        super().__init__(first_name, last_name, login_attempts)
        self.privileges = privileges
    def show_privileges(self):
        words = ''
        for i in self.privileges:
            words += f'{i}, '
        words = words.removesuffix(', ')
        print(f'Admin has {words}.')

a = Admin(['I', 'have', 'a', 'pen'], 'x', 'y')
a.show_privileges()