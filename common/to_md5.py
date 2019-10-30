import hashlib

def md5(src):
    m= hashlib.md5()
    # m.update(src)
    m.update(src.encode('utf-8'))
    return m.hexdigest()

def md5_b(src):
    m= hashlib.md5()
    m.update(src)
    return m.hexdigest()

if __name__=="__main__":

    print(md5("123"))
