import cv2 as cv
import numpy as np
img=cv.imread('D:/intern-assignment/images/75940.jpg')
import xml.etree.ElementTree as ET
tree = ET.parse('D:/intern-assignment/75940.xml')
root = tree.getroot()
sample_annotations = []
for neighbor in root.iter('bndbox'):
    xmin = np.int0(float(neighbor.find('xmin').text))
    ymin = np.int0(float(neighbor.find('ymin').text))
    xmax = np.int0(float(neighbor.find('xmax').text))
    ymax = np.int0(float(neighbor.find('ymax').text))
    sample_annotations.append([xmin, ymin, xmax, ymax])
    print(sample_annotations)
    bounded=cv.rectangle(img,(xmin,ymin),(xmax,ymax),(0,255,0),1)
cv.imshow('Bounded',bounded)
cv.imwrite('D:/intern-assignment/images/75940out.png',bounded)
cv.waitKey(0)
cv.destroyAllWindows()
