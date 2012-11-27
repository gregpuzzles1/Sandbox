# Python version = 2.7.2
# Platform = win32

from PIL import Image
import math
import operator
import os
import time

from collections import deque

def quads(im_width, im_height, start_x, start_y):
        quad_1 = (start_x, start_y, start_x + im_width / 2, \
                       start_y + im_height / 2)
        quad_2 = (start_x + im_width / 2, start_y, \
                       start_x + im_width, start_y + im_height / 2)
        quad_3 = (start_x, start_y + im_height / 2, \
                       start_x + im_width / 2, start_y + im_height)
        quad_4 = (start_x + im_width / 2, start_y + im_height / 2, \
                       start_x + im_width, start_y + im_height)
        return quad_1, quad_2, quad_3, quad_4

def compare(img, x):
    image2 = Image.open(x)
    h1 = img.histogram()
    h2 = image2.histogram()
    """print "One = ", h2[:256]
    print "\n"
    print "Two = ", h2[256:512]
    print "\n"
    print "Three = ", h2[512:768]
    print "\n"
    print sum(h2)
    print "\n"""
    rms = math.sqrt(reduce(operator.add,
                           map(lambda a,b: (a-b)**2, h1, h2))/len(h1))
    return rms

def compare_color(img, d):    
    dirname = 'C:\\Python27\\Sandbox\\photomosaic\\dali'
    pictdb = os.listdir(dirname)
    place_holder = 0
    for i in pictdb:
        x = os.path.join('C:\\Python27\\Sandbox\\photomosaic\\dali', i)
        td = compare(img, x)
        if td > place_holder:
            place_holder = td
            pict = x
            #print "pict = ", pict
    return pict
            
def copy_picture():
        pass

def resize_picture(resize_pic, resize_pic_width, resize_pic_height):
    """Resizes the picture database picture to the size of the
    cropped quadrant picture, and returns as value 'out'"""    
    out = resize_pic.resize((resize_pic_width, resize_pic_height))
    return out

def find_match(img, d):
    dirname = 'C:\\Python27\\Sandbox\\photomosaic\\dali'
    pictdb = os.listdir(dirname)
    color_value = img_getdata(img)
    closest_match = 1000000
    for key, value in d.items():
        ismatch_red = abs(value[0] - color_value[0])
        ismatch_green = abs(value[1] - color_value[1])
        ismatch_blue = abs(value[2] - color_value[2])
        ismatch = ismatch_red + ismatch_green + ismatch_blue
        if closest_match > ismatch:
            closest_match = ismatch
            match_key = key
    return pictdb[match_key]
        
def img_getdata(img):
    """Returns a 3-length tuple of the average Red, Green and Blue
    color values"""    
    img = img.getdata()    
    red_counter = 0
    green_counter = 0
    blue_counter = 0
    for rgb in img:
        red = rgb[0]
        green = rgb[1]
        blue = rgb[2]
        red_counter += red
        green_counter += green
        blue_counter += blue
    red_average = red_counter / len(img)
    green_average = green_counter / len(img)
    blue_average = blue_counter / len(img)
    color_value = (red_average, green_average, blue_average)
    return color_value

def pictdb_getdata(pictdb):
    """Creates a dictionary entry for each picture in the picture database.
    The key will be the counter, the value will be the Red, Green, and Blue
    averages as a 3-length tuple. Returns the dictionary 'd'"""    
    d = {}
    counter = 0
    for i in pictdb:
        dbpic = os.path.join('C:\\Python27\\Sandbox\\photomosaic\\dali', i)
        dbpic = Image.open(dbpic)
        dbpic = dbpic.getdata()
        counter += 1
        red_counter = 0
        green_counter = 0
        blue_counter = 0
        for rgb in dbpic:
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]
            red_counter += red
            green_counter += green
            blue_counter += blue
        red_average = red_counter / len(dbpic)
        green_average = green_counter / len(dbpic)
        blue_average = blue_counter / len(dbpic)
        color_value = (red_average, green_average, blue_average)
        d[counter] = color_value
    return d
        
def create_mosaic(filename, min_size):
    """Creates the mosaic"""    
    dirname = 'C:\\Python27\\Sandbox\\photomosaic\\dali'
    pictdb = os.listdir(dirname)    
    outdir = 'C:\\Python27\\Sandbox\\photomosaic\\'    
    counter = 0
    imc = Image.open(filename)
    im = imc.copy()
    im_width, im_height = im.size
    start_x = 0
    start_y = 0
    d = pictdb_getdata(pictdb)
    Q = []
    switch = 1
    xy = quads(im_width, im_height, start_x, start_y)
    for i in range(0,4):
        Q.append(xy[i])
    while switch == 1:
        Q = deque(Q)
        qn = Q.popleft()
        im_width = qn[2] - qn[0]
        im_height = qn[3] - qn[1]
        start_x = qn[0]
        start_y = qn[1]
        a = start_x + im_width
        b = start_y + im_height
        xy = quads(im_width, im_height, start_x, start_y)
        if (xy[0][2] - xy[0][0]) < min_size or (xy[0][3] - xy[0][1]) < min_size:
             for i in range(0, 4):
                 #print xy[i]
                 img = im.crop((xy[i][0], xy[i][1], xy[i][2], xy[i][3]))
                 #x = compare_color(img, d)
                 print d
                 yy = img_getdata(img)
                 print "yy = ", yy
                 #print x
                 
                 """match = find_match(img, d)
                 resize_pic = os.path.join('C:\\Python27\\Sandbox\\photomosaic\\dali', match)
                 resize_pic = Image.open(resize_pic)
                 resize_pic_width = xy[i][2] - xy[i][0]
                 resize_pic_height = xy[i][3] - xy[i][1]
                 paste_pic = resize_picture(resize_pic, resize_pic_width, resize_pic_height)
                 im.paste(paste_pic, (xy[i][0], xy[i][1]))
                 counter += 1
                 if counter == 5:
                     pass"""
        else:
             for i in range(0, 4):
                 Q.append(xy[i])
        if len(Q) == 0:
                switch = 0
    im.save(outdir + 'im.jpg', quality = 100)

def save_as(self, filename): 
    self.filename = filename

def main():
    """Main Program"""    
    start_time = time.clock()
    dirname = "C:\\Python27\Sandbox\photomosaic\dali"
    pictdb = os.listdir(dirname)
    filename = "C:\\Python27\Sandbox\photomosaic\karan.jpg"
    min_size = 10
    create_mosaic(filename, min_size)
    run_time = time.clock() - start_time
    print "Run time = ", run_time

if __name__ == '__main__':
    main()

    
