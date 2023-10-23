import secrets

class PasswordGenerator:
    def __init__(self, password_length, charset):
        self.password_length = int(password_length)
        self.charset = charset
        
    def generate_password(self):
        generated_digits = [""]
        password = ''

        while len(password) < self.password_length:
            new_password_digit = secrets.choice(self.charset)

            while new_password_digit != generated_digits[-1]:
                password += (''.join(new_password_digit))
                generated_digits.append(new_password_digit)

        return password