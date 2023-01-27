import os
import time as time


def get_recent_files(path):
    print("File processing...")
    root_folder = path
    current_time = time.time()
    time_to_substract = 30*(24 * 60 * 60)
    recent_files = []

    include_file_exts = [".txt", ".doc", ".docx",
                         ".rtf", ".pdf", ".odt",
                         ".xls", ".xlsx", ".ods",
                         " .ppt", ".pptx", ".odp",
                         ".jpg,", ".jpeg", ".png", ".gif",
                         ".wma", ".wav", ".mp3",
                         ".mp4", ".mkv", ".avi",
                         ".py"]

    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            curr_file_path = os.path.join(dirpath, filename)
            if os.path.splitext(curr_file_path)[1].lower() in include_file_exts:
                if os.path.exists(curr_file_path):
                    file_stats = os.stat(curr_file_path)
                    file_acces_time = file_stats.st_atime
                    file_creation_time = file_stats.st_ctime
                    file_modification_time = file_stats.st_mtime
                    if file_creation_time > current_time - time_to_substract:
                        recent_files.append(
                            (curr_file_path, file_acces_time, file_creation_time, file_modification_time))
            else:
                recent_files.append((curr_file_path, None, None, None))

    print("File processing soon completed...")
    recent_files = [file for file in recent_files if file[2]
                    is not None and file[3] is not None]
    recent_files.sort(key=lambda x: x[2], reverse=True)

    print("File processing completed.")
    return recent_files
