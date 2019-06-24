
def WriteFile(path,data):
    with open(path, 'w') as f:
        f.write(data)

def WriteFile_add(path,data):
    with open(path, 'a+') as f:
        f.write(data)
        f.write('\n')


def ReadFile(path):
    with open(path,"r",encoding="utf-8") as f1:
        list = f1.readlines()
        for i in range(0, len(list)):
            list[i] = list[i].rstrip('\n')
        return list