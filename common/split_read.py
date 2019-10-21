
# encoding: utf-8
import os

def total_count(fpath,Block_Size):
    with open(fpath,"r",encoding="utf-8") as f:
        # All_Size=os.path.getsize(fpath)
        All_Size=len(f.read())
        if All_Size%Block_Size!=0:
            total=All_Size//Block_Size+1
        else:
            total=All_Size//Block_Size
        return total

def total_count_b(fpath,Block_Size):
    with open(fpath,"rb") as f:
        # All_Size=os.path.getsize(fpath)
        All_Size=len(f.read())
        if All_Size%Block_Size!=0:
            total=All_Size//Block_Size+1
        else:
            total=All_Size//Block_Size
        return total



def read_file(fpath,Block_Size):
    with open(fpath,"r",encoding="utf-8") as f:
        while True:
            block = f.read(Block_Size)
            if block:
                yield block
            else:
                return

def read_file_b(fpath,Block_Size):
    with open(fpath,"rb") as f:
        while True:
            block = f.read(Block_Size)
            if block:
                yield block
            else:
                return

def read_a_file(fpath):
    # f = open(fpath,'rb')
    # file=f.read()
    # f.close()
    # return file
    with open(fpath,"r",encoding="utf-8") as f:
        return f.read()

def read_a_file_b(fpath):
    # f = open(fpath,'rb')
    # file=f.read()
    # f.close()
    # return file
    with open(fpath,"rb") as f:
        return f.read()

# fpath='../update/QRSP4-034015-00-09-T-2019-09-26.tar.gz'
# Block_Size =1024
# print(total_count(fpath,Block_Size))
# count=0
# for i in read_file(fpath,Block_Size):
#     print(i)
#     count=count+1
#
# print(count)


