import subprocess

def clear_terminal():
    subprocess.run('cls' if subprocess.os.name == 'nt' else 'clear', shell=True)