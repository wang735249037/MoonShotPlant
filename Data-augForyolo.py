#!/usr/bin/env python
# coding: utf-8

# In[15]:


import imageio
from imgaug import augmenters as iaa
import imgaug as ia
import os
import glob
import shutil
import sys
seq = iaa.Sequential(
        [
            # apply the following augmenters to most images
            #iaa.Fliplr(0.5),  # horizontally flip 50% of all images
            #iaa.Flipud(0.5), # horizontally flip 50% of all images
            #iaa.Dropout2d(p=0.5, nb_keep_channels=0),
            #iaa.GaussianBlur(sigma=(0.0, 3.0)),
            #iaa.EdgeDetect(),
            iaa.Canny(sobel_kernel_size=[3, 3])            
        ])
roots = r"\\taka2new\dataT0\Free\chwang\Moonshot\kikou"
root_train_img =glob.glob(os.path.join(roots,'images',r"train\*.jpg"))
root_val_img =glob.glob(os.path.join(roots,'images',r"val\*.jpg"))
'''
for fn in root_train_img:
    image = imageio.imread(fn)
    images_aug = [seq(image=image) for _ in range(8)]
    for i,one in enumerate(images_aug):
        ##target_imgP =os.path.join(roots,r'images\train-au',str(i)+"_"+os.path.basename(fn))
        target_imgP =os.path.join(roots,r'images\train-au',os.path.basename(fn).replace(".jpg","")+"_"+str(i)+".jpg")
        src_LabelP = fn.replace("images","labels").replace("jpg","txt")
        target_LabelP =target_imgP.replace("images","labels").replace("jpg","txt")   
        shutil.copy(src_LabelP,target_LabelP)
        imageio.imsave(target_imgP,one)
'''
for fn in root_val_img:
    image = imageio.imread(fn)
    images_aug = [seq(image=image) for _ in range(8)]
    for i,one in enumerate(images_aug):
        ##target_imgP =os.path.join(roots,r'images\train-au',str(i)+"_"+os.path.basename(fn))
        target_imgP =os.path.join(roots,r'images\val-au',os.path.basename(fn).replace(".jpg","")+"_"+str(i)+".jpg")
        src_LabelP = fn.replace("images","labels").replace("jpg","txt")
        target_LabelP =target_imgP.replace("images","labels").replace("jpg","txt")   
        shutil.copy(src_LabelP,target_LabelP)
        imageio.imsave(target_imgP,one)
        #continue
    #continue

#print(type(images_aug))
#print(images_aug[0].shape)
#print("Augmented:")
#ia.imshow(ia.draw_grid(images_aug, cols=4, rows=2))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




