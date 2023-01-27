from cx_Freeze import setup, Executable

includes = ["tkinter", "tkcalendar"]

include_files = ["project\\get_recent_files.py", "project\\functions.py"]

setup(
    name="File Facility",
    version="1.0",
    description="Logiciel de trie et de recherches de dossier/fichiers",
    options={"build_exe": {"includes": includes,
                           "include_files": include_files}},
    executables=[Executable("project\\tkinter_interface.py",
                            icon="project\\others\\icon.ico")]
)
