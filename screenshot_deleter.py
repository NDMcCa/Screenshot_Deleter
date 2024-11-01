import os, shutil

'''
Pemanently deletes all files in the 'Screenshots' folder on Windows; configured to work on systems with or without OneDrive enabled.
If you take a lot of screenshots on your system but want to periodically clear the folder, this is for you.
Useful for students who take screenshots of lecture slides and paste them in their notes.
When compiled as an .exe, you can schedule it to run in Windows Task Scheduler.
'''
def delete():

    # Try the default directory with OneDrive enabled
    try:
        fp = os.path.expanduser('~') + "/OneDrive/Pictures/Screenshots"
        for file in os.listdir(fp):
            file_path = os.path.join(fp, file)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    # Otherwise OneDrive must not be enabled and '/Screenshots' is in the default Windows location
    except:
        fp = os.path.expanduser('~') + "/Pictures/Screenshots"
        for file in os.listdir(fp):
            file_path = os.path.join(fp, file)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

delete()
