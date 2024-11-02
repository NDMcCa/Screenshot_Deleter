import os, shutil

'''
Pemanently deletes all .pln files in the 'Downloads' folder on Windows; useful for some flight sim players using ActiveSky with SimBrief flight plans
This was built purely out of my own need for a simple script that does this
'''


def delete():
    fp = os.path.expanduser('~') + "/Downloads"
    for file in os.listdir(fp):
        filename = os.path.basename(file)
        if filename[-3:] == 'pln':
            file_path = os.path.join(fp, file)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)


delete()
