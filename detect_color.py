import numpy as np
import argparse
import cv2

#constructing the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",help = "C:/Users/ankita upadhyay/Documents/Python/Python codes/2021/Color Detection")
args = vars(ap.parse_args())

#load the image
image = cv2.imread(args["image"])

#define the list of boundaries
boundaries = [
    ([17,15,100],[50,56,200]) ,#red
    ([86,31,4], [220,88,50]), #blue
    ([25,46,190] , [62,174,250]), #yellow
    ([103, 86, 65], [145, 133, 128]) #gray
]

#loop over the boundaries
for (lower, upper) in boundaries:
    #create NumPy arrays from  the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    #find colour within the specified boundaries and apply the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, upper , mask=mask)

    #show the images
    cv2.imshow("image", np.hstack([image,output]))
    cv2.waitKey(0)