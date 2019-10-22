import os, zipfile
#打包目录为zip文件（未压缩）
def make_zip(source_dir, output_filename):

    zipf = zipfile.ZipFile(output_filename, 'w')
    pre_len = len(os.path.dirname(source_dir))
    for parent, dirnames, filenames in os.walk(source_dir):
        for filename in filenames:
            pathfile = os.path.join(parent, filename)
            arcname = pathfile[pre_len:].strip(os.path.sep)   #相对路径
            zipf.write(pathfile, arcname)
    zipf.close()

if __name__=='__main__':
    source_dir="C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\zip"
    output_filename="test1.zip"
    make_zip(source_dir, output_filename)
