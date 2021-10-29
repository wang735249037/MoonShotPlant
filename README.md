# MoonShotPlant
This code is for the project named Moonshot.
Currently(2021.10.28) The project will do the following steps:
   (1) read the raw tif data and conver to nii format.
   (2) use 3D visualization software (Morilab's software: Pluto) for 3D visualization.
   (3) use Plant-seg to segment the cell wall and find each cell in 3D space.
   (4) use transfer learning with paired data of our own dataset.
   (5) use Pluto to visualize the segmented cell in 3D. and use script to set the poistion of virtual camera and save screenshot to files.
   (6) use open3D to visualize 3D result and pick up one cell.
