#recognize the pic text and save in excel
from aip import AipOcr
import re
import warnings
import os
import time
import pandas as pd
warnings.filterwarnings("ignore",category=DeprecationWarning)
# App_ID Api_Key  Secret_Key  Apply from Baidu Ai
App_ID = 'xxxxxxxxxx'
Api_Key = 'xxxxxxxx'
Secret_Key = 'xxxxxxxxxxxxxxxxxxxxx'
client = AipOcr(App_ID, Api_Key, Secret_Key)
def get_pic_name(dirs):
    list_pic = os.listdir(dirs)
    return list_pic
    #print(list_pic)t
#print(get_pic_name("D:/temp"))
if __name__ == '__main__':
    print(f"---------------------------Get Pic Text----------Raiden_bit-------------------------")
    pic_dir = input("Please input the pic_dir(eg:D:/temp):")
    print("Now reading pic words......")
    pic_list = get_pic_name(pic_dir)
    pic_words = []

    for each_pic in pic_list:
        #print('')# #相当于换行
        each_pic_words = ''
        print(f'Reading {each_pic} Now......')
        i = open(f'D:/temp/{each_pic}','rb')
        img= i.read()
        message = client.basicGeneral(img)
        #print(message)
        for each_word in message['words_result']:
            #print(each_word['words'],end = '   ')
            each_pic_words = each_pic_words + each_word['words'] +' '
        pic_words.append(each_pic_words)
    content_df = pd.DataFrame({'Pic_Name': pic_list, 'Pic_Words':pic_words})
    content_df.to_excel("D:/temp/content.xls",index= False)
    print(pic_words)
    #print(pic_list)
    print("\nDone! All words are save to the conten.xls,plese check it\nBye!!!!!!!!!!")
    time.sleep(5)
