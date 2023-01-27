import subprocess

dependencies = ['tkinter', 'cx_freeze', 'tkintertable', 'tkcalendar']

print("Installation des dépendances...")

for package in dependencies:
    subprocess.call(['pip', 'install', package])

print("Installation des dépendances terminée")
