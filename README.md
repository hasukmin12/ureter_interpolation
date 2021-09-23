[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/hasukmin12)](https://hits.seeyoufarm.com) 
![Hits](https://img.shields.io/github/followers/hasukmin12?label=Follow)

## **Ureter Interpolation** 
this code is to create new image by interpolate two image.
I made this code to make Ureter dataset


## **Why Interpolation?**
- Research is underway to find ureter in CT images without contrast agents.
- Dataset was provided by Hanyang University Seoul Hospital, and in the CT image, only one slice out of five was provided.
- I made the code to find the ureter for the remaining four slices.


## **Code description**
- blob_detecter.py : Find two blobs in the image and output the center coordinates of each blob.
- interpolate_two_image.py : by using blob_detecter, create new image by interpolate two image. Using 't' parameter ranging from 0 to 1 corresponding to first and last frame.
- test.py : you can test upper code by this code
- ureter_interpolation : find masked ureter slice by find_max_1, count blank slice and create new image by interpolate two image on both ends.


## **Results**
before interpolation
![before_inter](https://user-images.githubusercontent.com/56622945/134477729-e0c0a52c-74b9-4d9c-97e4-4a1dfaa95b46.png)

after interpolation
![after_inter](https://user-images.githubusercontent.com/56622945/134477801-492fcf1b-2b2f-4cdf-ae88-e7cc2088cd35.png)




before interpolation (CT view)
![before_inter_CT](https://user-images.githubusercontent.com/56622945/134477836-54a2e719-1ad3-4ebd-a376-c299acc15397.png)

after interpolation (CT view)
![after_inter_CT](https://user-images.githubusercontent.com/56622945/134477861-c9531fea-bca0-41a3-8604-d909d553dd89.png)







