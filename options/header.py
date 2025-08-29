from options.color import *
import os
import platform

def clean():
    os.system('cls' if platform == 'nt' else 'clear')

def header():
    print(f"""{BOLD_BLUE}
 ___ _ __  _ __  ___ ___  
| __| |  \| | _\| __| _ \ 
| _|| | | ' | v | _|| v / {RESET}{BOLD_WHITE}
|_| |_|_|\__|__/|___|_|_\ 
     By : Bang yog{RESET}{BOLD_BLUE}
-------------------------{RESET}
""")