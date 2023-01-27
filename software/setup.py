from cx_Freeze import setup, Executable

options = {
    'build_exe': {
        'includes': ['tkinter']
        # si nécessaire
        # 'include_files':['path/to/image1.jpg', or other]
    }
}

executables = [
    Executable('project\\tkinter_interface.py')
]

setup(name='File Facility',
      version='1.0',
      description='Logiciel de trie et de recherches de dossier/fichiers',
      options=options,
      executables=executables)

# executez la commande cx_freeze : python setup.py build
