# Drawing a bounding box on a image from the data available in xml files

## Input
- IMAGES- [images](https://github.com/shrutimary15/Bounding-box-on-a-image/tree/main/Images)       

- DATA FILES- [datafile](https://github.com/shrutimary15/Bounding-box-on-a-image/tree/main/XML%20file)

## Theory
The theoretical explaination can be found in this [ppt](https://github.com/shrutimary15/Bounding-box-on-a-image/blob/main/Background%20details.pptx). 

## Psuedo Code

- Import all required packages
- Read the image using cv.imread() into a variable.
- Import the data by reading from a xml file.
- Find xmin, xmax, ymin and ymax value from the file and store each in different variable.
- Use cv.Rectangle() to draw a rectangle.
- Save the image to a file using cv.imwrite().

## Program
The program is written in a way to input one image and corresponding xml file and obtained the required output.


[Code](https://github.com/shrutimary15/Bounding-box-on-a-image/blob/main/boundingboxindividual.py)

## Result
The output obtained can be found in this [link](https://github.com/shrutimary15/Bounding-box-on-a-image/tree/main/Output).
