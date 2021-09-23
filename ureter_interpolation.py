import numpy as np
import os
import cv2
import copy
from PIL import Image
from interpolate_two_image import inter

def find_max_1(input_path):
    input_list = next(os.walk(input_path))[2]
    input_list.sort()
    max_1 = []
    for input in input_list:
        path = os.path.join(input_path,input)
        if cv2.imread(path).max() != 0:
        # if np.array(Image.open(path)).max() != 0:
            max_1.append(input)

    return max_1


# case_0 = '/home/has/Datasets/Ureter_dataset2/case_00000'
# print(case_0)
# list = find_max_1(case_0)
# print(list)
#
# case_0_list = next(os.walk(case_0))[2]
# case_0_list.sort()
# print(case_0_list)



def find_blank_and_interpolation(input_path, max_1_list):
    input_list = next(os.walk(input_path))[2]
    input_list.sort()
    # print(input_list)

    for i in range(len(max_1_list)-1):
        bf_img = os.path.join(input_path, max_1_list[i])
        aft_img = os.path.join(input_path, max_1_list[i+1])

        cnt = int(max_1_list[i][-7:-4])
        next_cnt = int(max_1_list[i+1][-7:-4])
        # print(cnt)
        # print(next_cnt)
        sub = next_cnt - cnt - 1
        # print(sub)

        for j in range(sub):
            next_img_num = cnt + j + 1
            next_img = os.path.join(input_path,'pre_{0:03}.png'.format(next_img_num))
            if os.path.isfile(next_img)==True:
                os.remove(next_img)
            # print(next_img)
            ratio = (j+1)/(sub+1)
            print("ratio : ", ratio)
            out = inter(bf_img,aft_img,ratio)

            cv2.imwrite(next_img, out)
            print("img saved")


        print("next")
        print("")


path = '/home/has/Datasets/Ureter_dataset3'

case_list = next(os.walk(path))[1]
case_list.sort()

for case in case_list:
    case_path = os.path.join(path,case)
    print(case_path)
    list = find_max_1(case_path)
    print(list)

    find_blank_and_interpolation(case_path,list)