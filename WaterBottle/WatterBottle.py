import backend
from PIL.ExifTags import TAGS

filepath=input("File name:  ")

# Only for images
print("   ---= Exif Data =---   ")
exifdata=backend.metadata(filepath)
for tag_id in exifdata:
    tag = TAGS.get(tag_id, tag_id)
    data = backend.metadata(filepath).get(tag_id)
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")

# All files
print("   ---= All String > X Characters =---   ")
backend.embeddedStrings(filepath, 14)


