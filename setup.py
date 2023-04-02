import os

if not os.path.exists('1color'):
    os.makedirs('1color')

with open('1color/__init__.py', 'w'):
    pass

with open('1color/colors.py', 'w') as f:
    f.write('''
import sys
import time


class Colors:
    # Codes de couleurs
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'

    # Effets de texte
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # Effets de couleurs
    FADE_IN = '\033[38;5;{code};48;5;0m'
    FADE_OUT = '\033[38;5;0;48;5;{code}m'
    RAINBOW = [
        '\033[31m',
        '\033[33m',
        '\033[32m',
        '\033[36m',
        '\033[34m',
        '\033[35m',
        '\033[31m'
    ]

    @staticmethod
    def color_text(text, color):
        """Retourne le texte avec la couleur spécifiée."""
        return color + str(text) + Colors.RESET

    @staticmethod
    def fade_in(text, color_code, duration=0.5):
        """Affiche le texte avec un effet de fondu en entrée."""
        steps = 50
        for i in range(steps):
            color = Colors.FADE_IN.format(code=color_code)
            fade = (i + 1) / steps
            fade_text = color + text + Colors.RESET
            print(fade_text, end='', flush=True)
            time.sleep(duration / steps)
            sys.stdout.write('\033[1D')
            sys.stdout.write('\033[K')
        print(text)

    @staticmethod
    def fade_out(text, color_code, duration=0.5):
        """Affiche le texte avec un effet de fondu en sortie."""
        steps = 50
        for i in range(steps):
            color = Colors.FADE_OUT.format(code=color_code)
            fade = (i + 1) / steps
            fade_text = color + text + Colors.RESET
            print(fade_text, end='', flush=True)
            time.sleep(duration / steps)
            sys.stdout.write('\033[1D')
            sys.stdout.write('\033[K')
        print()

    @staticmethod
    def rainbow(text, duration=0.1):
        """Affiche le texte avec un effet arc-en-ciel."""
        for i in range(len(text)):
            color = Colors.RAINBOW[i % len(Colors.RAINBOW)]
            print(color + text[i] + Colors.RESET, end='', flush=True)
            time.sleep(duration)
        print()
''')

print('Le module 1color a été installé avec succès !')
