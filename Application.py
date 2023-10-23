import CharsetSelector as CS
import clipboard
import PasswordGenerator as PG
import PasswordValidator as PV
import tkinter as tk
from tkinter import messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # Paleta de cores - tons de azul
        self.AZUL_ESCURO = "#3B7197"
        self.AZUL_MEDIO = "#4A8DB7"
        self.AZUL_CLARO = "#74BDE0"
        self.AZUL_BEBE = "#A1E1FA"
        
        # Tela principal 
        self.title("Gerador de Senhas")
        self.geometry("300x460")
        self.columnconfigure(
            index=[0, 1], 
            weight=1
        )
        self.configure(bg=self.AZUL_ESCURO)
        
        self.create_widgets()
        
    def validate_numeric_input(self, char):
        # Restringe os valores de entrada para apenas númerais
        if char.isdigit() or char == "" or char == "\x08" or char == "\t":
            return True
        return False

    def create_widgets(self): # Função de criação de todo o layout principal da aplicação
        # Variáaveis para armazenar estado das checkboxes
        self.var_uppercase = tk.BooleanVar()
        self.var_lowercase = tk.BooleanVar()
        self.var_digits = tk.BooleanVar()
        self.var_punctuation = tk.BooleanVar()
        self.var_whitespaces = tk.BooleanVar()


        self.checkbox_vars = {
            "uppercase": self.var_uppercase.get(), 
            "lowercase": self.var_lowercase.get(), 
            "digits": self.var_digits.get(), 
            "punctuation": self.var_punctuation.get(), 
            "whitespaces": self.var_whitespaces.get()
        }
        
        self.screen_title = tk.Label(
            text="GERADOR DE SENHAS", 
            font=("Arial", 14, "bold"),
            bg=self.AZUL_ESCURO, 
            fg=self.AZUL_BEBE
        )
        self.screen_title.grid(
            row=0, 
            column=0, 
            columnspan=2, 
            sticky="NSEW", 
            pady=(10, 10)
        )

        self.subtitle = tk.Label(
            text="Selecione os caracteres da senha:", 
            font=("Arial", 11), 
            bg=self.AZUL_ESCURO, 
            fg=self.AZUL_BEBE
        )
        self.subtitle.grid(
            row=1, 
            column=0, 
            columnspan=2,
            sticky="w", 
            padx=(10, 0), 
            pady=(10, 10)
        )

        self.parameters_frame = tk.Frame(self)
        self.parameters_frame.grid(
            row=2, 
            column=0, 
            sticky="w", 
            padx=(10, 10)
        )

        self.check_uppercase = tk.Checkbutton(
            self.parameters_frame, 
            text="Incluir letras maiúsculas", 
            variable=self.var_uppercase
        )
        self.check_uppercase.grid(
            row=0, 
            column=0, 
            sticky="w", 
            padx=(10, 10), 
            pady=(10, 0)
        )

        self.check_lowercase = tk.Checkbutton(
            self.parameters_frame, 
            text="Incluir letras minúsculas", 
            variable=self.var_lowercase
        )
        self.check_lowercase.grid(
            row=1, 
            column=0, 
            sticky="w", 
            padx=(10, 10)
        )

        self.check_digits = tk.Checkbutton(
            self.parameters_frame, 
            text="Incluir números", 
            variable=self.var_digits
        )
        self.check_digits.grid(
            row=2, 
            column=0, 
            sticky="w", 
            padx=(10, 10)
        )

        self.check_punctuation = tk.Checkbutton(
            self.parameters_frame, 
            text="Incluir pontuações", 
            variable=self.var_punctuation
        )
        self.check_punctuation.grid(
            row=3, 
            column=0, 
            sticky="w", 
            padx=(10, 10)
        )

        self.check_whitespaces = tk.Checkbutton(
            self.parameters_frame, 
            text="Incluir espaços", 
            variable=self.var_whitespaces
        )
        self.check_whitespaces.grid(
            row=4, 
            column=0, 
            sticky="w", 
            padx=(10, 10)
        )

        self.generate_password_button = tk.Button(
            self.parameters_frame, 
            text="\n\n\nGerar\nSenha\nAleatória\n\n\n", 
            width=10, 
            font=("Arial", 10, "bold"),
            bg=self.AZUL_ESCURO, 
            fg="#F0F0F0", 
            height=10, 
            command=self.generate_random_password_button
        )
        self.generate_password_button.grid(
            row=0, 
            column=1, 
            rowspan=7, 
            sticky="e", 
            padx=(10, 10)
        )

        self.length_label = tk.Label(
            self.parameters_frame, 
            text="Nº de dígitos:"
        )
        self.length_label.grid(
            row=5, 
            column=0, 
            sticky="w", 
            padx=(10, 0), 
            pady=(5, 0)
        )

        vcmd = (self.register(self.validate_numeric_input), '%P')
        self.password_length_entry = tk.Entry(
            self.parameters_frame, 
            width=24, bg="#E0E0E0", 
            validate="key", 
            validatecommand=vcmd
        )
        self.password_length_entry.grid(
            row=6, 
            column=0, 
            padx=(10, 10), 
            pady=(0, 10)
        )

        self.password_frame = tk.Frame(self)
        self.password_frame.grid(
            row=3, 
            column=0, 
            columnspan=2, 
            sticky="we", 
            padx=(10, 10), 
            pady=(10, 0)
        )

        self.password_title = tk.Label(
            self.password_frame, 
            text="Senha"
        )
        self.password_title.grid(
            row=0, 
            column=0, 
            sticky="w", 
            padx=(10, 0), 
            pady=(10, 0)
        )

        self.password_entry = tk.Entry(
            self.password_frame, 
            width=20, 
            bg="#E0E0E0"
        )
        self.password_entry.grid(
            row=1, 
            column=0, 
            padx=(10, 10), 
            pady=(0, 10)
        )

        self.strength_title = tk.Label(
            self.password_frame, 
            text="Força da senha"
        )
        self.strength_title.grid(
            row=0, 
            column=1, 
            sticky="w", 
            padx=(10, 0), 
            pady=(10, 0)
        )

        self.password_strength_label = tk.Label(
            self.password_frame, 
            text="", 
            bg="#F0F0F0", 
            width=16
        )
        self.password_strength_label.grid(
            row=1, 
            column=1, 
            sticky="w", 
            padx=(10, 10), 
            pady=(0, 10)
        )

        self.strength_button = tk.Button(
            self.password_frame, 
            text="Verificar", 
            bg=self.AZUL_ESCURO, 
            fg="#F0F0F0", 
            command=self.verify_button
        )
        self.strength_button.grid(
            row=2, 
            column=0, 
            columnspan=2, 
            sticky="we", 
            padx=(10, 10), 
            pady=(5, 10)
        )

        self.footer_frame = tk.Frame(self)
        self.footer_frame.grid(
            row=4, 
            column=0, 
            columnspan=2, 
            sticky="w", 
            padx=(10, 10), 
            pady=(10, 10)
        )

        self.clear_button = tk.Button(
            self.footer_frame, 
            text="Limpar tudo", 
            bg=self.AZUL_ESCURO, 
            fg="#F0F0F0", 
            command=self.clear_all_button, 
            width=15
        )
        self.clear_button.grid(
            row=0, 
            column=0, 
            sticky="w", 
            padx=(10, 10), 
            pady=(10, 10)
        )

        self.copy_button = tk.Button(
            self.footer_frame, 
            text="Copiar senha", 
            bg=self.AZUL_ESCURO, 
            fg="#F0F0F0", 
            command=self.copy_password_button, 
            width=15
        )
        self.copy_button.grid(
            row=0, 
            column=1, 
            sticky="e", 
            padx=(20, 20), 
            pady=(10, 10)
        )


    def open_popup(self):
        self.popup_window = tk.Toplevel(self, bg=self.AZUL_ESCURO)
        self.popup_window.title("")
        self.popup_window.geometry("200x100")
        
        label = tk.Label(
            self.popup_window, 
            text="Senha copiada com sucesso!", 
            bg=self.AZUL_ESCURO, 
            font=("Arial", 10, "bold")
        )
        label.pack(pady=20)
        
        ok_button = tk.Button(
            self.popup_window, 
            text="OK", 
            command=self.close_popup, 
            bg=self.AZUL_ESCURO, 
            fg="#F0F0F0", 
            font=("Arial", 10, "bold")
        )
        ok_button.pack()
        
        # Interrompe a interação coma janela principal enquanto a popup estiver aberta
        self.copy_button.config(state="disabled")
        self.popup_window.protocol("WM_DELETE_WINDOW", self.close_popup)
        
    def close_popup(self):
        # Habilita o botão de cópia novamente quando a popup for fechada
        self.popup_window.destroy()
        self.copy_button.config(state="normal")

    def select_charset(self):
        charsetter = CS.CharsetSelector(
            lower_letters=self.var_lowercase.get(), 
            upper_letters=self.var_uppercase.get(), 
            digits=self.var_digits.get(), 
            punctuation=self.var_punctuation.get(), 
            whitespace=self.var_whitespaces.get()
        )
        self.charset = charsetter.configure_charset()
        
    def create_new_password(self):
        self.password_length = self.password_length_entry.get()

        if not self.password_length:
            self.password_length = 0

        password_creator = PG.PasswordGenerator(
            password_length=self.password_length, 
            charset=self.charset
        )
        self.generated_password = password_creator.generate_password()
        
    def validate_generated_password(self, password):
        validator = PV.PasswordValidator(password=password)
        self.password_strength = validator.validate()

    def update_password_strength_label(self):
        if self.password_strength:
            self.password_strength_label["text"], self.password_strength_label["fg"] = "SENHA FORTE", "green"
        else:
            self.password_strength_label["text"], self.password_strength_label["fg"] = "SENHA FRACA", "red"
        
    def generate_random_password_button(self):
        
        self.select_charset()
        self.create_new_password()
        self.validate_generated_password(self.generated_password)
        
        self.password_entry.delete(0, 'end')
        self.password_entry.insert(0, self.generated_password)

        if self.generated_password:
            self.update_password_strength_label()

    def verify_button(self):
        self.password = self.password_entry.get()
        self.validate_generated_password(self.password)

        if self.password:
            self.update_password_strength_label()
        else:
            self.password_strength_label["text"] = ""

    def clear_all_button(self):
        checkboxes = [
            self.check_lowercase,
            self.check_uppercase,
            self.check_digits,
            self.check_punctuation,
            self.check_whitespaces
        ]
        
        for checkbox in checkboxes:
            checkbox.deselect()

        self.password_length_entry.delete(0, 'end')

        self.password_entry.delete(0, 'end')

        self.password_strength_label["text"] = ""

    def copy_password_button(self):
        clipboard.copy(self.password_entry.get())
        self.open_popup()

"""    def generate_password_error_messagebox(self):
        # will ask for, at least, one of the checkboxes and the password length entry filled to able 
        # "generate password" button
        if not any(self.checkbox_vars.values()):
            messagebox.showerror("Erro", "Selecione pelo menos uma opção de caracteres.")
            return False
        else:
            return True"""

    
janela = Application()
janela.mainloop()