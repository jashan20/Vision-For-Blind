# Title: God's Eye (AI based spectacles for Blind people) (Hardware Project)
<ul>
  <li><h3>This project was the winner of Ionathon 1.0 on global level</h3></li>
  <li><h3>SIH finalist 2022</h3></li>
</ul>

## 1. Description
![photo_2022-03-26_03-15-10](https://user-images.githubusercontent.com/73690811/160207334-b364c377-c9cf-4186-84c6-8de8132e0629.jpg)
### Solution:
AI-based spectacles that will tell blind people about their surroundings in real-time.

### Features:
1) It will assist visually impaired person in navigating from one place to another.
2) It will have OCR technology which will help the visually impaired person to read books and newspapers.
3) The facial recognition module will help the visually impaired person to know the person sitting in front of him/her.

### Working:
![Methodology](https://user-images.githubusercontent.com/73690811/160275683-16184713-08c2-4a5c-b63b-46d872144097.png)

### Modules:
#### <b>A)</b> Module 1 (Voice Module) - 
It uses GTTS library(Google Text to Speech) to convert string to voice and Playsound Library is used to play the voice returned by GTTS <br> 
#### <b>B)</b> Module 2 (Optical Character Recognition) - 
It uses Tesseract library w, which takes opencv frame as input, recognizes text in it and return text as string. <br>
#### <b>C)</b> Module 3 (Live-Environment Captioning) - 
We have trained our own deep learning model. It works on a multimodal neural network that uses feature vectors obtained using both RNN and CNN, so consequently, for training, two inputs have to be taken. One is the image we need to describe, a feed to the CNN, and the second is the words in the text sequence produced till now as a sequence as the input to the RNN. This module takes OpenCV frame as input and returns a description of the frame. <br>
#### <b>D)</b> Module 4 (Facial Recognition Module) - 
It works on face_recognition that uses dlib's deep learning algorithm implementation to recognize the person in the image. It takes OpenCV frame as input and returns name as string. <br>
<br>


## 2. Methodology:
![Arnav-01](https://user-images.githubusercontent.com/73690811/160275549-182cb6fa-22ff-49da-af27-9cf341b9bb09.jpg)

## 3. Live Links:
### Website Link : http://godseye.epizy.com/
### Youtube videos: 
<ul>
  <li>https://youtu.be/tzNpARxmF44</li>
  <li>https://youtu.be/hwHHWGiZTyw</li>
</ul>

## 4. Instructions to run God's Eye ?
Step 1: Download the repository as zipped file <br>
Step 2: Extract zip<br>
Step 3: Install dependencies from requirements.txt<br>
Step 4: Run main.py <br>
Step 5: Web Cam will start working. We have 3 Modes, Initially Live-environment captioning module will work (Mode 1, press 1 to start this mode), enter 2 to start Facial Recognition mode and enter 3 to start Optical Character Recognition Mode (i.e enter 1, 2 or 3 to switch between modes)<br>
Step 6: Enter ESC button to end <br>

    
