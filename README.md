# Signature-Authentication-for-Cheque
Overview
The Signature Authentication for Cheque project is a Python-based graphical user interface (GUI) application designed to verify the authenticity of signatures on cheques. This application utilizes computer vision techniques to compare an uploaded cheque image with a reference signature image to determine if they match. The application is built using Tkinter for the GUI and OpenCV for image processing.

Features
User-Friendly Interface: A clean and intuitive interface created using Tkinter.
Image Upload: Allows users to upload images of the cheque and the reference signature.
Signature Comparison: Utilizes the ORB (Oriented FAST and Rotated BRIEF) algorithm for feature detection and the BFMatcher (Brute Force Matcher) for comparing the features.
Result Display: Displays a message indicating whether the signatures match or not, along with a match percentage.

How It Works
User Interface:

The application window is created using Tkinter.
Labels and buttons are placed on the window to allow users to upload images and check the signature authentication.
Image Upload:

Users can upload the cheque image and the reference signature image using the provided buttons.
The uploaded images are displayed in the application window.
Signature Comparison:

The check function reads the uploaded images in grayscale.
ORB (Oriented FAST and Rotated BRIEF) is used for feature detection.
The BFMatcher (Brute Force Matcher) compares the features.
The application calculates the distance between matched features and determines the similarity percentage.
A message box displays whether the signature is authentic or forged based on the calculated similarity.
