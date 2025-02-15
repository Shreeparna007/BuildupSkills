import cv2
import glob
images = glob.glob("*.jpg")
for image in images:
    img = cv2.imread(image, 0)
    re = cv2.resize(img, (100, 100))
    cv2.imshow("hey", re)
    cv2.imwrite("resize_"+image, re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()