# Computer Vision PlayGround

## Usage

Clone this repository to local.

Part 1: Canny edge detection

Part 2: YOLO custom training


## Canny edge detection

### canny_edge_detection.py
---

command usage:
```
python canny_edge_detection.py -i [input file] -o [output file]
```

command expamples:
```
python canny_edge_detection.py -i ./img/BL_01.jpg -o ./img/BL_01_EDGE_01.jpg
```

output expamples:
```
../
  canny_edge_detection.py
  draw_boundingbox.py
  img/
    BL_01.jpg
    BL_01_EDGE_01.jpg
```

### draw_boundingbox.py
---

-g [input gray file] => the img that is processed by canny edge detection

-c [input colorful file] => the original img that we can draw bounding box on

-o [output file] => the img path that we will store the img that have bounding box on in

command usage:
```
python draw_boundingbox.py -g [input gray file] -c [input colorful file] -o [output file]
```

command expamples:
```
python draw_boundingbox.py -g ./img/LB_04_EDGE_example.jpg -c ./img/LB_04.jpg -o ./img/LB_04_BD_example.jpg
```

### feature_detector.py
---

Use ORB methods to match feature between two pictures.

If you get error like:
```
AttributeError: module 'cv2' has no attribute 'xfeatures2d'
```

This means your openCV is possible too new, you have to downgrade the version. However, many many old versions are Yanked already. You will have to try different versions. Not Recommended though, I will recommend you find other methods to do feature detection. You can see /canny/img/feature_detector_example1 and /canny/img/feature_detector_example2 if you are curious about the results.

command usage:
```
python feature_detector.py -i1 [image 1] -i2 [image 2]
```

command expamples:
```
python feature_detector.py -i1 ./img/LB_03 -i2 ./img/LB_01
```

## YOLO custom training

### unsplash.py
---

Crawling pictures from [Unsplash](<https://unsplash.com>)

command usage:

```
python unsplash.py -w unsplash -q [query] -o [output directory] -p [number of pages - 4]
```

command expamples:
```
python unsplash.py -w unsplash -q temple -o . -p 15
```

output expamples:
```
../
  README.md
  findLabeledImg.py
  imgScaler.py
  splitImg.py
  unsplash.py
  temple/
    pic1.jpg
    pic2.jpg
    (19 pages of pictures)
```

command expamples:
```
python unsplash.py -w unsplash -q temple -o ./Temple -p 10
```

output expamples:
```
../
  README.md
  findLabeledImg.py
  imgScaler.py
  splitImg.py
  unsplash.py
  temple/
    Temple/
      pic1.jpg
      pic2.jpg
      (14 pages of pictures)
```

### imgScaler.py
---

Resize images into certain size.

Move & rename images into another folder having names like 1.jpg 2.jpg 3.jpg

Size parameters, input folder path and output folder path are fixed in code.

Not yet support python argument.

### Label Image Yourself
---

Use image labeling tools like [LabelImg](<https://github.com/tzutalin/labelImg>).

Or go to [roboflow](<https://app.roboflow.com>) to built your own object detection dataset.

### findLabeledImg.py
---

If you are not using [roboflow](<https://app.roboflow.com>), then you can use this python file to find labled images

Find the jpg images with txt files (the YOLO format of label files)

Use image labling tools to label images

Or go to app.roboflow.com to upload images and label them

example:
```
input_folder/
  1.jpg
  2.jpg
  2.txt
  3.jpg
  4.jpg
  4.txt
  5.jpg
  6.jpg
  7.jpg
```

The output will be like:
```
output_folder/
  2.jpg
  2.txt
  4.jpg
  4.txt
```

After this step, I upload my output folder to roboflow and use roboflow to create YOLO trainable dataset.

### Bulid dataset for training custom YOLO using roboflow
---

Just follow the instructions on the website, it is not complicated.

### Train custom YOLO
---

[YOLOv5 google colab](<https://colab.research.google.com/github/roboflow-ai/yolov5-custom-training-tutorial/blob/main/yolov5-custom-training.ipynb#scrollTo=7iiObB2WCMh6>)

[Altered google colab](<https://colab.research.google.com/drive/1ZhpQ1h8S3bcGtd1mqgbPcpwc_KczS7yv?usp=sharing>)

### Reference
---

[YOLOv5](<https://github.com/ultralytics/ultralytics>)
