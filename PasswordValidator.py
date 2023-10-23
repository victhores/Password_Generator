import re
import common_passwords_DB

COMMON_PASSWORDS = common_passwords_DB.common_passwords

class PasswordValidator:
    def __init__(self, password):
        self.password = password
        self.define_password_strength()    

    def define_password_strength(self):
        password_strength = 0

        # Verifica o comprimento da senha
        if 8 <= len(self.password) < 12:
            password_strength += 1
        elif len(self.password) >= 12:
            password_strength += 2

        # Verifica se há caracteres repetidos na senha
        if len(set(self.password)) == len(self.password):
            password_strength += 1

        # Verifica a presença de caracteres em diferentes conjuntos
        if re.search(r'[A-Z]', self.password):
            password_strength += 1
        if re.search(r'[a-z]', self.password):
            password_strength += 1
        if re.search(r'\d', self.password):
            password_strength += 1 
        if re.search(r'\W', self.password):
            password_strength += 1

        # Verifica se a senha está na lista de senhas comuns
        if self.password not in COMMON_PASSWORDS:
            password_strength += 1
        else:
            password_strength = 0

        return password_strength >= 6

    def validate(self):
        self.define_password_strength()
        if self.define_password_strength():
            return True
        else:
            return False
              



