# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 11:03:53 2021
This file combines the images into video by reading the images created by NUVAT project
combine movie and blend (in png format) into avi file. you should set width and height 
@author: chwang
"""
import os
import glob
import cv2
if __name__ == '__main__':
    pro_dir = "/dataT0/Free/chwang/Moonshot/kikou-seg/Anotated"
    fns = glob.glob(os.path.join(pro_dir,"Movie/*.png"))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(os.path.join(pro_dir,"combie.avi"),fourcc,10,(256,128),True)
    fns.sort();
    for one in fns:
        #print(one, one.replace("movieFrame","blend").replace("Movie","Blend"))
        movie = cv2.imread(one)
        blend = cv2.imread(one.replace("movieFrame","blend").replace("Movie","Blend"))
        idx = os.path.basename(one).replace("movieFrame_","").replace(".png","")
        if movie is not None and blend is not None:
            print("add: " + idx)
            movie = cv2.putText(movie,idx,(0,20),3,1,(0,0,0),1)
            new = cv2.hconcat([movie,blend])
            out.write(new)
    out.release()