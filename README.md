# ShapesExtraction
Extracting coordinates of shapes from the images

For Machine Learning - Shape Segmentation

Compatible with Anaconda 2.7, requires additional libraries:
[simplification](https://github.com/urschrei/simplification) and [imutils](https://github.com/jrosebr1/imutils)

"BirdSilhouettes" is to contain an amount of image files, each displaying a polygon of 12 vertices (see example images).
HCD.py will look through all the images in the Folder "BirdSilhouettes" and create two Text files "birdShapes.txt" and "birdAngles.txt".

HCD.py makes use of the libaries [simplification](https://github.com/urschrei/simplification) and [imutils](https://github.com/jrosebr1/imutils), as well as [opencv](https://github.com/opencv/opencv) in order to extract an array of pixel coordinates that represent the original polygon within a margin of error. It does so by first creating a shape-mask of the polygon from which the contours of the polygon are then extracted using [cv2.findcontours()](https://docs.opencv.org/3.1.0/d3/dc0/group__imgproc__shape.html#ga17ed9f5d79ae97bd4c7cf18403e1689a) and [imutils.grab_contours()](https://github.com/jrosebr1/imutils/blob/master/imutils/convenience.py).
Since the resulting shape woul contain too many vertices (about one for each border-pixel of the contour), a simplification-function simplify_coords(), using the [Ramer-Douglas-Peucker algorithm](https://en.wikipedia.org/wiki/Ramer%E2%80%93Douglas%E2%80%93Peucker_algorithm), is run over the vertices in order to remove uneeded vertices.
The resulting coordinate Arrays are then saved to "birdShapes.txt" and Bird_Angle_Calculator is being used next in order to create an Array of the 12 most prominent Angles in each polygon.

example images:

![Bird01.bmp](/BirdSilhouettes/Bird01.bmp) ![Bird02.bmp](/BirdSilhouettes/Bird02.bmp) ![Bird03.bmp](/BirdSilhouettes/Bird03.bmp) ![Bird05.bmp](/BirdSilhouettes/Bird05.bmp)


birdShapes.txt example:
> [(19.0, 6.0), (9.0, 15.0), (17.0, 15.0), (19.0, 17.0), (26.0, 29.0), (24.0, 37.0), (47.0, 39.0), (56.0, 50.0), (57.0, 61.0), (59.0, 62.0), (64.0, 58.0), (54.0, 31.0), (41.0, 30.0), (36.0, 10.0), (20.0, 6.0)]
>
> [(42.0, 18.0), (35.0, 28.0), (19.0, 25.0), (10.0, 39.0), (14.0, 51.0), (15.0, 46.0), (17.0, 44.0), (31.0, 41.0), (38.0, 47.0), (46.0, 27.0), (53.0, 23.0), (65.0, 23.0), (63.0, 18.0)]
>
> [(38.0, 19.0), (40.0, 22.0), (39.0, 25.0), (28.0, 20.0), (12.0, 26.0), (11.0, 28.0), (13.0, 31.0), (32.0, 28.0), (37.0, 35.0), (45.0, 35.0), (43.0, 31.0), (47.0, 26.0), (66.0, 24.0), (64.0, 21.0), (47.0, 19.0)]
>
> [(16.0, 14.0), (12.0, 18.0), (7.0, 17.0), (7.0, 25.0), (28.0, 22.0), (35.0, 28.0), (39.0, 22.0), (46.0, 20.0), (62.0, 20.0), (43.0, 14.0), (35.0, 21.0), (20.0, 14.0)]

birdAngles.txt example:
> [118.07248693585296, 138.01278750418336, 41.98721249581665, 135.0, 135.70731936854426, 80.93349726018383, 134.25914759061067, 121.75948008481281, 114.77514056883193, 108.33667142442715, 114.72184218465847, 108.43494882292202]
>
> [68.19859051364818, 111.80140948635182, 124.99202019855868, 114.37236492240353, 112.11557099595247, 128.8298249049704, 29.74488129694221, 146.30993247402023, 147.09475707701208, 127.30394827798344, 71.20011484134736, 141.54629078329404]
>
> [130.39990433373674, 56.309932474020215, 127.87498365109822, 83.99099404250548, 119.74488129694222, 114.71744091108339, 116.56505117707799, 125.5376777919744, 63.43494882292201, 114.77514056883193, 134.66881421158462, 62.31893843151474]
>
> [113.79718135619034, 154.9831065219, 135.0, 123.6900675259798, 78.69006752597979, 81.86989764584403, 131.26860300083956, 83.08877288097531, 139.63546342690267, 164.05460409907712, 17.52556837372288, 121.28850646056748]
