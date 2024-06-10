class User:
    def __init__(self, first_name, last_name, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
    def describe_user(self):
        print(f'User\'s name is {self.first_name.title()} {self.last_name.title()}')
    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
a= User('a', 'b')
a.describe_user()
a.greet_user()
a.increment_login_attempts()
a.increment_login_attempts()
a.increment_login_attempts()
print(a.login_attempts)
a.reset_login_attempts()
print(a.login_attempts)