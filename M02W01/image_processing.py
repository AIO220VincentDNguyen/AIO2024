# Download image
!gdown 1i9dqan21DjQoG5Q_VEvm0LrVwAlXD0vB

import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('/content/dog.jpeg')

# question 12
gray_img_01 = (np.max(img, axis=2) + np.min(img, axis=2)) / 2
gray_img_01 [0 , 0]

# question 13
gray_img_02 = np.average(img, axis=2)
gray_img_02[0 , 0]

#question 14
gray_img_03 = 0.21 * img[:, :, 0] + 0.72 * img[:, :, 1] + 0.07 * img[:, :, 2]
gray_img_03[0 , 0]