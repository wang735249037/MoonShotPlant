# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 10:03:11 2021

@author: chwang
"""
import glob
import os
import shutil
# some file name may exist japanese, so change it before image procesing
if __name__ == '__main__':
    data_dir = r"\\taka2\chwang\pywork\RA\data\root\211028_plant growth\211028_plant growth"
    files = glob.glob(os.path.join(data_dir,"*.jpg")) 
    if os.path.exists(os.path.join(data_dir,"converted1")) ==False:
        os.makedirs(os.path.join(data_dir,"converted1"))
    with open(os.path.join(data_dir,"map.txt"),"w") as f:
        for i,fn in enumerate(files):
            new_dir = os.path.join(data_dir,"converted",str(i)+".jpg")
            shutil.copy(fn,new_dir)
            f.write(fn+","+new_dir+"\n")
        
        