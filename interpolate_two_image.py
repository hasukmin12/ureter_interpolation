from scipy.ndimage.measurements import center_of_mass
from scipy.ndimage.interpolation import shift
import numpy as np
import os
import cv2
import copy
from blob_detecter import blob_detecter


mask_1 = '/home/has/Datasets/CT_annotated/00138812 김영대 180517/Marked_nooverlay_png/00138812 김영대 180517 pre0042.png'
mask_2 = '/home/has/Datasets/CT_annotated/00138812 김영대 180517/Marked_nooverlay_png/00138812 김영대 180517 pre0047.png'


def inter(img_1, img_2, t):
#input:
# images: list of arrays/frames ordered according to motion
# t: parameter ranging from 0 to 1 corresponding to first and last frame
#returns: interpolated image

#direction of movement, assumed to be approx. linear

    img_array_1 = cv2.imread(img_1)
    img_array_2 = cv2.imread(img_2)

    img1 = cv2.cvtColor(img_array_1, cv2.COLOR_RGB2GRAY)
    img2 = cv2.cvtColor(img_array_2, cv2.COLOR_RGB2GRAY)

    img_list = [img1,img2]


    blob1, blob2 = blob_detecter(img_1,img_2)



    a1 = blob1[0]
    a2 = blob1[1]

    b1 = blob2[0]
    b2 = blob2[1]

    # print(blob1)
    # print(blob2)


    mid_num = int((a1[0] + a2[0])/2)
    print("mid_num",mid_num)

    if a1[0] == 0 or a2[0] == 0:
        mid_num = 512
    # print(a1[0])
    # print(a2[0])

    left_img = copy.deepcopy(img_list)
    right_img = copy.deepcopy(img_list)



    for img in left_img:
        for i in range(0, 1024):
            for j in range(mid_num, 1024):
                    img[i][j] = 0

    for img in right_img:
        for i in range(0, 1024):
            for j in range(0, mid_num):
                    img[i][j] = 0


    # cv2.imshow("image", right_img[-1])
    # cv2.waitKey()



    # direction of movement, assumed to be approx. linear
    a = np.array(center_of_mass(left_img[0]))
    b = np.array(center_of_mass(left_img[-1]))


    # print("left_img first", a)
    # print("left_img second", b)

    # print(left_img[0].max())
    # print(left_img[-1].max())

    if left_img[0].max() != 0 or left_img[-1].max() != 0:

        print("pass_left")
        # find index of two nearest frames
        arr = np.array([center_of_mass(left_img[i]) for i in range(len(left_img))])
        v = a + t * (b - a)  # convert t into vector
        idx1 = (np.linalg.norm((arr - v), axis=1)).argmin()
        arr[idx1] = np.array([0, 0])  # this is sloppy, should be changed if relevant values are near [0,0]
        idx2 = (np.linalg.norm((arr - v), axis=1)).argmin()
        # print(idx2)

        rst = 0
        rst2 = 0

        if idx1 > idx2:
            b = np.array(center_of_mass(left_img[idx1]))  # center of mass of nearest contour
            a = np.array(center_of_mass(left_img[idx2]))  # center of mass of second nearest contour
            tstar = np.linalg.norm(v - a) / np.linalg.norm(
                b - a)  # define parameter ranging from 0 to 1 for interpolation between two nearest frames
            im1_shift = shift(left_img[idx2], (b - a) * tstar)  # shift frame 1
            im2_shift = shift(left_img[idx1], -(b - a) * (1 - tstar))  # shift frame 2
            rst = im1_shift + im2_shift
            # for i in range(0, 512):
            #     for j in range(0, 512):
            #         if -1 < rst[i][j] < 1:
            #             rst[i][j] = 0
            #         else:
            #             rst[i][j] = 1

            # return rst  # return average

        if idx1 < idx2:
            b = np.array(center_of_mass(left_img[idx2]))
            a = np.array(center_of_mass(left_img[idx1]))
            tstar = np.linalg.norm(v - a) / np.linalg.norm(b - a)
            im1_shift = shift(left_img[idx2], -(b - a) * (1 - tstar))
            im2_shift = shift(left_img[idx1], (b - a) * (tstar))
            rst = im1_shift + im2_shift
            # for i in range(0, 512):
            #     for j in range(0, 512):
            #         if -1 < rst[i][j] < 1:
            #             rst[i][j] = 0
            #         else:
            #             rst[i][j] = 1

            # return rst
    else:
        rst = 0


    print("go next")
    # direction of movement, assumed to be approx. linear
    a = np.array(center_of_mass(right_img[0]))
    b = np.array(center_of_mass(right_img[-1]))

    # print("right_img first", a)
    # print("right_img second", b)


    if right_img[0].max() != 0 or right_img[-1].max() != 0:

        print("pass_right")

        # find index of two nearest frames
        arr = np.array([center_of_mass(right_img[i]) for i in range(len(right_img))])
        v = a + t * (b - a)  # convert t into vector
        idx1 = (np.linalg.norm((arr - v), axis=1)).argmin()
        arr[idx1] = np.array([0, 0])  # this is sloppy, should be changed if relevant values are near [0,0]
        idx2 = (np.linalg.norm((arr - v), axis=1)).argmin()
        # print(idx2)

        if idx1 > idx2:
            b = np.array(center_of_mass(right_img[idx1]))  # center of mass of nearest contour
            a = np.array(center_of_mass(right_img[idx2]))  # center of mass of second nearest contour
            tstar = np.linalg.norm(v - a) / np.linalg.norm(
                b - a)  # define parameter ranging from 0 to 1 for interpolation between two nearest frames
            im1_shift = shift(right_img[idx2], (b - a) * tstar)  # shift frame 1
            im2_shift = shift(right_img[idx1], -(b - a) * (1 - tstar))  # shift frame 2
            rst2 = im1_shift + im2_shift
            # for i in range(0, 512):
            #     for j in range(0, 512):
            #         if -1 < rst[i][j] < 1:
            #             rst[i][j] = 0
            #         else:
            #             rst[i][j] = 1
            # cv2.imshow("image", im2_shift)
            # cv2.waitKey()

            # return rst  # return average

        if idx1 < idx2:
            b = np.array(center_of_mass(right_img[idx2]))
            a = np.array(center_of_mass(right_img[idx1]))
            tstar = np.linalg.norm(v - a) / np.linalg.norm(b - a)
            im1_shift = shift(right_img[idx2], -(b - a) * (1 - tstar))
            im2_shift = shift(right_img[idx1], (b - a) * (tstar))
            rst2 = im1_shift + im2_shift
            # for i in range(0, 512):
            #     for j in range(0, 512):
            #         if -1 < rst[i][j] < 1:
            #             rst[i][j] = 0
            #         else:
            #             rst[i][j] = 1

            # return rst
    else:
        rst2 = 0



    return rst + rst2
#

# out_1 = inter(mask_1, mask_2,0.8)
#
# cv2.imwrite('0.8shift_ureter.png', out_1)
# print("img saved")
#
# cv2.imshow("image", out_1)
# cv2.waitKey()