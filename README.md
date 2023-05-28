# tesseract_persian_example
example to use tesseract with persian data

## Install Tesseract

```
sudo add-apt-repository ppa:alex-p/tesseract-ocr-devel
sudo apt install -y tesseract-ocr
tesseract --version
```

## Get Persian Weights

[Download](https://github.com/tesseract-ocr/tessdata/blob/main/fas.traineddata)

```
cp fas.traineddata /usr/share/tesseract-ocr/5/tessdata/
```
