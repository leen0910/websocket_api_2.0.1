import hashlib

def md5(src):
    m= hashlib.md5()
    # m.update(src)
    m.update(src.encode(encoding='UTF-8'))
    return m.hexdigest()


if __name__=="__main__":

    print(md5("123"))

