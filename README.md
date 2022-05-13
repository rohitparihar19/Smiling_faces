# Smiling_faces
 
 To accomplish this task, we have used dlib library for detection of face and the facial landmark detector is an implementation of the approach presented by Kazemi et al.which gives us 68 land mark featugres .

 # Installation
 1. Install Visual studio: as dilib is a c based library with that need to install additional packages for C, C++ programming, which is Packages CMake tools for Windows
 2. pip install CMake
 3. pip install dlib


 # Dlib's 68 Face Features:
 The face detector is made using the Histogram of Oriented Gradients (HOG) feature combined with a linear classifier, an image pyramid, and sliding window detection scheme.The facial landmark detector is an implementation of the approach presented by Kazemi et al. It returns an array of 68 points in form of (x,y) coordinates that map to facial structures of the face, as shown in figure.

![68-facial-landmarks](https://user-images.githubusercontent.com/102134613/168282641-2c76ad91-edee-4a11-a31b-3b3de285bda3.jpg)


 we have used the facial landmarks to detect weather a person is smiling or not and we have used the length of lips and jwaline and calcculated a ratio and defined threshold of 0.28.


 # Results:
System Configuration: AMD Ryzen5 processor, 8 gb RAM , 4 gb GPU

It was givig in between 25 to 35 fps on cpu

![Screenshot (71)](https://user-images.githubusercontent.com/102134613/168282808-0bebf2cb-a860-4060-8690-9b07c672adea.png)




# Further Improvement and Application :

Face smile detection and emotion detection is having a wide application in current era like: happyness dtection ,drowsiness detection,etc.

For the further improvement in place of using facial landmark model we can use Deep learning based approaches for refrance we can use this research paper 
@ A Comparison of Face Verification with Facial Landmarks and Deep Features
Link- https://www.researchgate.net/publication/338048224_A_Comparison_of_Face_Verification_with_Facial_Landmarks_and_Deep_Features
