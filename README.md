# PollyLab2021FALL

## Usage

Clone this repository to local.

Part 1 => Canny edge detection

Part 2 => YOLO custom training


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

The output will be like

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

reference: https://colab.research.google.com/github/roboflow-ai/yolov5-custom-training-tutorial/blob/main/yolov5-custom-training.ipynb#scrollTo=7iiObB2WCMh6

my google colab: https://colab.research.google.com/drive/1ZhpQ1h8S3bcGtd1mqgbPcpwc_KczS7yv?usp=sharing
