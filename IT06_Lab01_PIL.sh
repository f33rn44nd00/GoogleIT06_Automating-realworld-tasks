# -- PART 1 - Assets and Install Pillow --
# First, download the website assets
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie

# list files
ls
# unzip the file
unzip images.zip
# list from unzipped file
ls ~/images


# Install Pillow
pip3 install pillow

# -- PART 2 - Python script --
# Create the script to:
#  1 - rotate 90 clockwise
#  2 - Resize from 192x192 to 128x128
#  3 - save .jpeg to new folder

# Run your script
chmod +x <script_name>.py
./<script_name>.py

ls /opt/icons

# To check images, use the python interpreter
<<python
python3
from PIL import Image
img = Image.open("/opt/icons/ic_edit_location_black_48dp")
img.format, img.size #to view image format and size
exit() #type exit to exit
python

# The end



