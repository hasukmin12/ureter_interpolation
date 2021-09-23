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
- 
