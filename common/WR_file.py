
def WriteFile(path,data):
    with open(path, 'w') as f:
        f.write(data)


def WriteFile_b(path,data):
    with open(path, 'wb') as f:
        f.write(data)

def WriteFile_add(path,data):
    with open(path, 'a+') as f:
        f.write(data)
        f.write('\n')


def ReadFile(path):
    with open(path,"r",encoding="gbk") as f1:
        list = f1.readlines()
        for i in range(0, len(list)):
            list[i] = list[i].rstrip('\n')
        return list