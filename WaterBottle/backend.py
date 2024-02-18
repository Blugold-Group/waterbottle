from PIL import Image, ExifTags
from PIL.ExifTags import TAGS
import subprocess

def metadata(imagepath):
    file = Image.open(imagepath)
    exifdata = file.getexif()
    return(exifdata)

def embeddedFiles(imagepath):
    #Binwalk
    print("Embedded files")

def embeddedStrings(imagepath, length=10):
    subprocess.run(["strings", "-"+str(length), imagepath]) 

def brokenChunks(imagepath):
    print("Broken chunks")

def optionalChunks(imagepath):
    print("Broken chunks")

def colorBitPlanes(imagepath):
    print("Color and bit planes")

def lsbData(imagepath):
    print("Extract LSB data")

def rgbValues(imagepath):
    print("RGB values")

def stegenography(imagepath):
    print("Steaganography")

def colorPalette(imagepath):
    print("Browse color palette")

def pixelValueDifferencing(imagepath):
    print("Pixel value differencing")



