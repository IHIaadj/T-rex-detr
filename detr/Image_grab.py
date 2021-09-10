from PIL import Image
import cv2
import numpy as np
from mss import mss


def capture_screenshot(x, y, w, h):
    # Capture entire screen

    with mss() as sct:
        monitor = sct.monitors[1]
        sct_img = sct.grab(monitor)
        # Convert to PIL/Pillow Image
        return np.array(Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX'))



def resize(img, percent=0.2):
    img = img[200 :500, 100:800]
    width = int(img.shape[1] * percent)
    height = int(img.shape[0] * percent)
    dim = (width, height)
    return cv2.resize(img, dim), dim



def midpoint(p1, p2):
    return (p1 + p2) / 2




# path = '/Users/Nuttapong/Desktop/Dino Images'
# count = 0

# import datetime
#
# start = datetime.datetime.now()
#
# while True:
#
#     fname = os.path.join(path, 'Dino' + str(count).zfill(4) + '.jpg')
#
#     image_np, (dim) = resize(cv2.cvtColor(capture_screenshot(x=150, y=400), cv2.COLOR_BGR2RGB), percent=0.5)
#
#     cv2.imshow('screen', image_np)
#
#     cv2.imwrite(fname, image_np)
#
#     count +=1
#
#     if cv2.waitKey(1) == ord('q'):
#         cv2.destroyAllWindows()
#         break;
#
# end = datetime.datetime.now()
#
# print(count / int((end - start).seconds))
# print(dim)