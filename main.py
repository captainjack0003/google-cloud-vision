# ********************************************************************************************
# ********************************************************************************************
# ********************************************************************************************
#  Rohan Jain                   02-06-2023               Adding Different Test Cases
# ********************************************************************************************
# ********************************************************************************************
# ********************************************************************************************


# Authentication to Google API
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='ENTER YOUR JSON KEY'

from google.cloud import vision

# re is used to extract 
import re

vision_client = vision.ImageAnnotatorClient()
image = vision.Image()

#image url
#image_uri = 'https://staticimg.amarujala.com/assets/images/2016/12/13/aadhar-card_1481617623.jpeg'
#image_uri='https://i.pinimg.com/originals/4e/5a/27/4e5a27c06d8c8c7ada75c3ff7541b381.jpg'
#image_uri='https://i.pinimg.com/564x/3c/82/51/3c8251d9382b42a43a26bdb240cd5324.jpg'
image_uri='https://i.pinimg.com/564x/07/79/1f/07791f1c1762a50fb7f2e477c2d3a747.jpg'


#storing data
image.source.image_uri = image_uri
response = vision_client.text_detection(image=image)
data=response.text_annotations[0].description

#print(data)

# Extract name
#name = re.findall(r"(?:Government of India\.\s)([^\n]*)", data)
#name = name[0].strip() if name else None


# Split the data into lines
lines = data.split('\n')

# Find the line index containing "GOVERNMENT OF INDIA" or "Government of India"
govt_of_india_index = -1

tracker=False

for i, line in enumerate(lines):
    
    if "GOVERNMENT OF INDIA" == line:
        govt_of_india_index = i
        tracker=True
        break
    
    elif "Government of India" == line:
        govt_of_india_index = i
        tracker=True
        break


if not tracker:
    print("image is not clear unable to detect data")
    
   
hindi_name=None
english_name=None

# Extract the Hindi and English names from the lines following "GOVERNMENT OF INDIA"
if govt_of_india_index != -1 and govt_of_india_index + 1 < len(lines):
    hindi_name = lines[govt_of_india_index + 1].strip()
    if govt_of_india_index + 2 < len(lines):
        english_name = lines[govt_of_india_index + 2].strip()


#Extract Father name
#father_name = re.findall(r"Father:\s([^\n]*)", data)
#father_name = father_name[0].strip() if father_name else None


# Extract date of birth
dob = re.findall(r"DOB:\s(\d{2}/\d{2}/\d{4})", data)
dob = dob[0] if dob else None

# Extract Aadhaar number
aadhaar = re.findall(r"(\d{4}\s?\d{4}\s?\d{4})", data)
aadhaar = aadhaar[0] if aadhaar else None


#print relevent data
#print("Father's Name:", father_name)
#print("Name:", name)

if tracker:
    print("Hindi Name:", hindi_name)
    print("English Name:", english_name)
    print("Date of Birth:", dob)
    print("Aadhaar Number:", aadhaar)




