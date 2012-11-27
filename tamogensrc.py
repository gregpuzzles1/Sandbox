#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#    Title:   Tone Altering Mosaic Generator (TAMOGEN)
#    Version: 1.0
#    Author:  Jack Whitsitt
#    Contact: http://sintixerr.wordpress.com
#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

import os, sys
import Image, ImageStat
from string import atoi


# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# GET PROGRAM PARAMETERS FROM USER AT RUNTIME


imname=raw_input("Name of large image being recreated as a mosaic? (Include extention): ")
print ""

fillty=raw_input("Use larger image to fill itself (0) or use other image (1)? ")
filltype=atoi(fillty)
print ""

if filltype==1:
  fillimn=raw_input("Name of smaller image used to fill the large? (Include extension): ")
  print ""
  
numsquares=[0,0]
nusq=raw_input("How many columns of the smaller image should be generated? ")
numsquares[0]=atoi(nusq)
print ""

nusq=raw_input("How many rows of the smaller image should be generated? ")
numsquares[1]=atoi(nusq)
print ""

fimsize=[0,0]

fmsz=raw_input("How wide (x), in pixels, should the final mosaic be? ")
fimsize[0]=atoi(fmsz)
print ""

fmsz=raw_input("How long (y), in pixels, should the final mosaic be? ")
fimsize[1]=atoi(fmsz)
print ""

fimname=raw_input("What should the mosaic filename be? (Dont include extenstion): ")
print ""

docolstr=raw_input("Should the mosaic be black and white (0) or color (1)? ")
docolor=atoi(docolstr)
print ""

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# FUNCTION DEFINITIONS

def genThumbnail(imn, fsz, ns, dc):
  if dc == 0:
    thumbfile = os.path.splitext(imn)[0] + ".thumbnail.PNG"	
    tim = Image.open(imn).convert("L")
    ssz=(fsz[0]/ns[0], fsz[1]/ns[1])
    tim.thumbnail(ssz)
    tim.save(thumbfile, "PNG")
  elif dc == 1:
    thumbfile = os.path.splitext(imn)[0] + ".thumbnail.PNG"	

    tim = Image.open(imn).convert("RGB")
    ssz=(fsz[0]/ns[0], fsz[1]/ns[1])
    tim.thumbnail(ssz)
    tim.save(thumbfile, "PNG")

def createNewImage(fims,dc):
  if dc==0:
    finim = Image.new("L",fims)
  elif dc==1:
    finim = Image.new("RGB",fims)
  return finim
		
def getBaseImage(bimg, dc):
  if dc==0:
    bim = Image.open(bimg).convert("L")
  elif dc==1:
    bim = Image.open(bimg).convert("RGB")
  return bim

def getImgSize(bimg):
  return bimg.size

def getSectionSize(ns, isz):
  squaresize=(isz[0]/ns[0], isz[1]/ns[1])
  return squaresize
	
def getFillSize(fimg):
  return fimg.size 

def getFillImage(fillimg, dc):
  if dc==0:
    fimim = Image.open(fillimg).convert("L")
  elif dc==1:
    fimim = Image.open(fillimg).convert("RGB")
  return fimim
		
def getFillTone(finim, dc):
  thumbstat=ImageStat.Stat(finim)
  thumbtone=thumbstat.mean
  return thumbtone

def getSectionTone(sec, dc):
  sstat=ImageStat.Stat(sec)
  stone=sstat.mean
  return stone
		
def getToneDiff(st, ft, dc):
  if dc==0:
    diff=st[0]/ft[0]
  elif dc==1:
    diff=[0,0,0]
    diff[0]=st[0]/ft[0]
    diff[1]=st[1]/ft[1]
    diff[2]=st[2]/ft[2]
  return diff
		
def setNewTone(sec, finillim, tdiff, cbox, bim, dc, ro, co):
  if dc==0:
    newfim = finillim.point(lambda op: op * tdiff)	
    cbox3=(cbox[0],cbox[1])
    bim.paste(newfim,cbox3)
		
########im not sure if using dc==1 requires its own case here. just doing so for temporary convenience		
  elif dc==1:
    nflist=0
    mypixcol=0
    temppix=[]
    pixcol=0
    newfim=0
    nflist = list(finillim.getdata())
    for pixcol in nflist:
      mypixcol=[0,0,0]
      mypixcol[0]=int(pixcol[0]*tdiff[0])
      mypixcol[1]=int(pixcol[1]*tdiff[1])
      mypixcol[2]=int(pixcol[2]*tdiff[2])
      mypixcol=tuple(mypixcol)
      temppix.append(mypixcol)

    newfim=finillim
    newfim.putdata(temppix)	
    cbox3=(cbox[0],cbox[1])
    bim.paste(newfim,cbox3)

def saveImage(imn, nbim):
  finalfile = os.path.splitext(imn)[0] + ".final.PNG"
  nbim.save(finalfile, "PNG")
  
	
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# SET-UP FILL IMAGE AND GET SECTION SIZE FOR LATER USE

if filltype==0:
  genThumbnail(imname, fimsize, numsquares, docolor)
  fillim=getFillImage(os.path.splitext(imname)[0] + ".thumbnail.PNG", docolor)

elif filltype==1:
  genThumbnail(fillimn, fimsize, numsquares, docolor)
  fillim=getFillImage(os.path.splitext(fillimn)[0] + ".thumbnail.PNG", docolor)
	
#elif filltype==2:
  #ask for directory
  #ask for extention
  #scour directory and set filenames to array
  #set imgrot to 1 and rotate through in row/column loop

fsectionsize=getSectionSize(numsquares, fimsize) 

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# OPEN BASE IMAGE, RESERVE SPACE FOR FINAL MOSAIC IMAGE, GET SECTION SIZE OF BOTH FOR LATER USE

im=getBaseImage(imname, docolor)

finalim=createNewImage(fimsize,docolor)

imsize=getImgSize(im)

bsectionsize=getSectionSize(numsquares,imsize)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# GET FILL IMAGE PROPERTIES

fillsize=getFillSize(fillim)
filltone=getFillTone(fillim, docolor)

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# SET STARTING SECTION OF MAIN LOOP TO X=0, Y=0

curbsecbox=[0,0,bsectionsize[0],bsectionsize[1]]
curfsecbox=[0,0,fsectionsize[0],fsectionsize[1]]

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# LOOP THROUGH BASE IMAGE LEFT TO RIGHT, TOP TO BOTTOM. 
# AT EACH SECTION, COMPARE TONE OF CURRENT BASE IMAGE SECTION TO ENTIRE FILL IMAGE, 
# GET DIFFERENCE, CHANGE TONE IN COPY OF FILL IMAGE TO MATCH CURRENT SECTION OF BASE IMAGE,
# PASTE ADJUSTED COPY OF FILL IMAGE INTO FINAL MOSAIC IMAGE IN THE PROPER PLACE
print ""
print "----STARTING RENDER----"
print ""

for row in range(0,numsquares[1]):
  for column in range (0,numsquares[0]): 

    tmpfillim=fillim.copy()
			
    bsection = im.crop(curbsecbox)
    bsectone = getSectionTone(bsection, docolor)
    tonediff = getToneDiff(bsectone, filltone, docolor)
    setNewTone(bsection, tmpfillim, tonediff, curfsecbox, finalim, docolor, row, column)

    curbsecbox[0]=curbsecbox[0]+bsectionsize[0]
    curbsecbox[2]=curbsecbox[2]+bsectionsize[0]
		
    curfsecbox[0]=curfsecbox[0]+fsectionsize[0]
    curfsecbox[2]=curfsecbox[2]+fsectionsize[0]
    print row,

  curbsecbox[0]=0
  curbsecbox[2]=bsectionsize[0]
  curfsecbox[0]=0
  curfsecbox[2]=fsectionsize[0]
		
  curbsecbox[1]=curbsecbox[1]+bsectionsize[1]
  curbsecbox[3]=curbsecbox[3]+bsectionsize[1]
	
  curfsecbox[1]=curfsecbox[1]+fsectionsize[1]
  curfsecbox[3]=curfsecbox[3]+fsectionsize[1]
  print ""
	
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Save New Image

saveImage(fimname, finalim)

print ""
print "----RENDER COMPLETE----"
