import numpy as np
import cv2



mask_1 = '/home/has/Datasets/CT_annotated/00138812 김영대 180517/Marked_nooverlay_png/00138812 김영대 180517 pre0042.png'
mask_2 = '/home/has/Datasets/CT_annotated/00138812 김영대 180517/Marked_nooverlay_png/00138812 김영대 180517 pre0047.png'


def blob_detecter(img_1, img_2):


    img = cv2.imread(img_1)
    img2 = cv2.imread(img_2)

    # cv2.imwrite('color_img.jpg', img)
    # cv2.imshow("image", img)
    # cv2.waitKey()


    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img_binary = cv2.threshold(img_gray, 127, 255, 0)
    contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    blob1 = [[0,0],[0,0]]
    blob2 = [[0,0],[0,0]]

    for cnt in contours:

        M = cv2.moments(cnt)

        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        cv2.circle(img, (cx, cy), 10, (0,0,255), -1)

        # print(cx, cy)
        if blob1[0] == [0, 0]:
            blob1[0] = [cx, cy]
        else:
            blob1[1] = [cx, cy]

    # print(blob1)



    img_gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret2, img_binary2 = cv2.threshold(img_gray2, 127, 255, 0)
    contours2, hierarchy2 = cv2.findContours(img_binary2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for cnt2 in contours2:

        M = cv2.moments(cnt2)

        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])

        cv2.circle(img2, (cx, cy), 10, (0,0,255), -1)

        # print(cx, cy)
        if blob2[0] == [0,0]:
            blob2[0] = [cx,cy]
        else:
            blob2[1] = [cx,cy]


    # print(blob2)

    img_list = [img_gray, img_gray2]

    blob1 = np.array(blob1)
    blob2 = np.array(blob2)

    return blob1,blob2


blob1, blob2 = blob_detecter(mask_1,mask_2)

# print(blob1)
# print(blob2)