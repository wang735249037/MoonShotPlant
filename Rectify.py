import cv2
import os
import sys
import argparse
import numpy as np
IMAGE_SIZE = 255
if __name__ =='__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument("--ims",type=str,help="directory of image")
    args = parse.parse_args()
    bRoi = True
    bUndistortion = True
    size = (IMAGE_SIZE,IMAGE_SIZE)
    cameraMatrix =0
    distCoeffs =0
    scope = "P200"
    if scope == 'P200_big':
        cameraMatrix = np.array([[280.3629*255/444, 0, 216.7025*255/444],
                        [0, 256.5163*255/440,190.1387*255/440],
                        [0, 0, 1]])
    elif scope == 'P200':
        #cameraMatrix = np.array([[280.3629*IMAGE_SIZE/410, 0, 216.7025*IMAGE_SIZE/410],
        #           [0, 256.5163*IMAGE_SIZE/373,190.1387*IMAGE_SIZE/373],
        #           [0, 0, 1]])
        cameraMatrix = np.array([[280.3629*IMAGE_SIZE/362, 0, 216.7025*IMAGE_SIZE/362],
                    [0, 256.5163*IMAGE_SIZE/370,190.1387*IMAGE_SIZE/370],
                    [0, 0, 1]])
    distCoeffs = np.array([-0.3485,0.0946, 0,0,0])
    
    size = (IMAGE_SIZE,IMAGE_SIZE)
    folder = r"\\taka2\data4\RBronchoScope"
    fname = args.ims
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')#MP42
    #videoWriter = cv2.VideoWriter(os.path.join(folder,fname)+"u.avi", fourcc, 30, size)
    videoWriter = cv2.VideoWriter(fname+"u.avi", fourcc, 30, size)
    cnt =0
    FrameCNT = 100000
    while cnt<(int)(FrameCNT) :
        path = os.path.join(folder,fname+r"a\%06d.tif"%cnt)
        im = cv2.imread(path)
        #print(im.shape)
        if im is not None:
            im[1::2]= im[::2]
            if bUndistortion:
                im = cv2.undistort(im, cameraMatrix, distCoeffs)
            if bRoi:
                im = cv2.resize(im, size, interpolation=cv2.INTER_AREA)
            videoWriter.write(im)
        cnt = cnt + 1