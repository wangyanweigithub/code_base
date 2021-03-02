import os
import sys


flag = True


def rm_anno(fs):
    fs = path + fs 
    with open(fs, 'r') as f:
        lines = f.readlines()

    lines = [i for i in lines if not i.strip().startswith("#")]
    #lines = [i for i in lines if i.strip() and not i.strip().startswith("#")]

    lines = list(filter(filter1, lines))

    new_files = os.path.splitext(os.path.basename(fs))[0]
    with open(new_files+"_back.py", 'w') as f:
        f.writelines(lines)


def filter1(line):
    line = line.strip()
    global flag

    if (line.startswith('"""') or line.startswith('r"""')) and len(line) > 3 and line.endswith('"""'):
        return False

    elif flag and (line.startswith('"""') or line.startswith('r"""')):
        flag = False
        return flag

    elif not flag and line.endswith('"""'):
        flag = True
        return False 
    else:
        return flag
    

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "../tornado/" 

    fs = os.listdir(path)
    fs = [i for i in fs if i.endswith(".py")]
    list(map(rm_anno, fs))
