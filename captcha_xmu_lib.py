import urllib3
import numpy as np
import matplotlib.pyplot as plt
import imageio
from scipy import ndimage

def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

# Retrieve the captcha image from website
url = "http://catalog.xmu.edu.cn/reader/captcha.php"
http = urllib3.PoolManager()
response = http.request('GET', url)
image = np.array(rgb2gray(imageio.mimread(response.data)[0]))

# Optional, show the image using matplotlib
# plt.imshow(image)
# plt.show()

# crop the image array into four piece, containing only the numbers
number_imgs = []
for i in range(4):
    number_imgs.append(image[15:27,i*12+5:i*12+15])

# load pre-stored digit images
digit_imgs = np.load('digits.npy')

# L2 distance to decide the outcome
out_numbers = []
for j, number_img in enumerate(number_imgs):
    for i, digit_img in enumerate(digit_imgs):
        if np.mean(np.absolute(number_img - digit_img))< 0.01:
            #print(j, i, np.mean(np.absolute(number_img - digit_img)))
            out_numbers.append(i)

print(out_numbers)