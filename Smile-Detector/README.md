# Smile-Detector
Smile detection by implementation of Viola-Jones algorithm.

Viola-Jones is quite powerful and its application has proven to be exceptionally notable in real-time face detection.

There are two stages in the Viola - Jones algorithm:
1.Training
2.Detection

# Step 1
Importing the libraries

# Step 2
Loading the cascades
 1. frontal face cascade ( Haar-like features)
 2. eye cascade (Haar-like features)
 3. smile cascade (Haar-like features)

# Step 3
Create a function that takes as input the image in black and white (gray) and the original image (frame), and that will return the same image with the detector rectangles. 

# Step 4
Turn the video camera on, and infintely repeat the follwing
 1. Get the last frame
 2. Do color transformations
 3. Get output of the detection function
 4. Display the output
Until we press 'q' on the keyboard

# Step 5
Turn off the web camera
Destroy all windows inside which the which the images were displayed.
