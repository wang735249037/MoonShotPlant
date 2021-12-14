import cv2
import glob
import numpy as np
labels = glob.glob("/dataT0/Free/chwang/Moonshot/root-moro/nuvat/Label/*.png")
#labels = glob.glob(r"\\taka2new\dataT0\Free\chwang\Moonshot\root-moro\nuvat\Label\*.png")
Paires= []
mw,mh =0,0
for fn in labels:
	im = cv2.imread(fn,-1)
	#print(im.shape)
	for target in range(1,np.max(im)+1):
		lab = np.where(im==target,255,0).astype(np.uint8)
		contours, hierarchy = cv2.findContours(lab,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
		mov = cv2.imread(fn.replace("Label","Movie").replace("label","movieFrame"))
		tmp =cv2.bitwise_and(mov,mov,mask =lab)#crop target area
		for one in contours:
			x,y,w,h = cv2.boundingRect(one)
			img = tmp[y:y+h,x:x+w]
			mw = w if mw < w else mw
			mh = h if mh < h else mh 
			cur =[]
			cur.append(img)
			cur.append(fn.replace("Label","Movie").replace("label_","movieFrame/").replace(".png","-"+str(target)+".bmp"))
			Paires.append(cur)
			#cv2.imwrite(fn.replace("Label","Movie").replace("label_","movieFrame/").replace(".png","-"+str(target)+".bmp"),img)
#print(mw,mh)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
vd = cv2.VideoWriter("combine.avi",fourcc,10,(mw,mh),True)
for one in Paires:
	img = np.zeros((mh, mw, 3), np.uint8)
	w,h,c = one[0].shape
	scale = min(mw/w,mh/h)
	out = cv2.resize(one[0],(int(mw*scale),int(mh*scale)))
	#print(out.shape,img.shape)
	img[0:out.shape[0],0:out.shape[1]] = out
	#cv2.imwrite(one[1],img)
	vd.write(img)
vd.release()

