import os, shutil

'''
Pemanently deletes files in the 'Downloads' folder on Windows. Specify by file type (or name) or enter "all"
If you download a lot of files on your system but want to periodically clear the folder, this is for you.
You could use this with task scheduler, but it would require user input; maybe a simple delete all version would be better for that task.
'''


def delete():
    print("Select a file extension to delete or select \"all\":")
    type = input()
    fp = os.path.expanduser('~') + "/Downloads"

    # Delete all files in the directory
    if type == all:
        for file in os.listdir(fp):
            file_path = os.path.join(fp, file)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    # Otherwise we want to select a specific file type to delete
    else:
        ext = -len(type)
        for file in os.listdir(fp):
            filename = os.path.basename(file)
            if filename[ext:] == type:
                file_path = os.path.join(fp, file)
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)


delete()
