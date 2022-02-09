# PollyLab2021FALL

## Usage

Clone this repository to local.

## unsplash.py

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
