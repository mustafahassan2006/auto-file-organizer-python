import os
import shutil
import re

def main():
    path = os.path.dirname(os.path.abspath(__file__))
    folder = os.listdir(path)

    for files in folder:
        if files != os.path.basename(__file__):
            extention = get_extension(files)
            try:
                if not os.path.isdir(os.path.join(path, extention)):
                    make_new_folder(path, extention)
                shutil.move(os.path.join(path, files), os.path.join(path, extention))
            except:
                pass
    print("execution completed check folder for results")


def get_extension(file_name):
    match = re.search(r'\.(\w+)$', file_name)
    try:
        return match.group(1)
    except AttributeError:
        pass



def make_new_folder(path,format):
    os.mkdir(os.path.join(path,format))


if __name__=="__main__":
    main()

