from removebg import RemoveBg
import os
from PIL import Image
def get_pic_names(dirs):
    list_pic = os.listdir(dirs)
    return list_pic
def remove_pic(key,pic_list):
    rmbg = RemoveBg(key, "error.log")
    for each_pic in pic_list:
        rmbg.remove_background_from_img_file("D:/removebg/temp_pic/" + each_pic,bg_color= 'white')
def resize_pic(pic_blist,pic_alist):
    for each_pic in pic_alist:
        if len(pic_alist) == len(pic_blist):        
            print('No pic need resize')
            break
        if each_pic not in pic_blist:
            print(each_pic)
            r_pic = Image.open("D:/removebg/temp_pic/" + each_pic)
            r_pic = r_pic.resize((800, 800))
            r_pic.save("D:/removebg/resize_pic/" + each_pic)
if __name__ == '__main__':
    pic_b = get_pic_names("D:/removebg/temp_pic")      
    app_key = input("Please input the app_key>>>")                    #apply api key from removebg
    print("Loading,removing pic background!!!")
    remove_pic(app_key,pic_b)
    print("Done!!!")
    pic_a = get_pic_names("D:/removebg/temp_pic")
    print("Loading,resize the pic!!!")
    resize_pic(pic_b,pic_a)
    print("Done!!!")
