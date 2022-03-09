# Boggler - Letter Recognition API

Mobile app available on iOS and Android

App Store - Apple - https://apps.apple.com/us/app/boggler/id1609487300

Play Store - Google - https://play.google.com/store/apps/details?id=com.rbzla.boggler&hl=en_US&gl=US

## Description

Instantly find all words in Boggle. Simply take a picture and the app will search the board. It will display the total words found, the inferred board letters, and the list of all words found, categorized by length. Only 3-letter or longer words, are listed. This is according to Boggle rules. The app processes the picture and converts it to the letters on the board. It has over 90% accuracy in determining the correct letter. In case the app incorrectly identifies a letter, the user can manually change any letter on the board. The app will then find the words possible with the corrected board. The app is available on iOS and Android.

## Implementation of Letter Recognition API

The mobile app sends the image to a Letter Recognition API to determine the current dice letters. First the image is cropped and split into 16 smaller images. Then each individual image is processed and passed through a prediction model. The model will output, based on the training data, the letter with the highest probability score. The API was built using the machine learning framework, TensorFlow. Over 10,000 images were used to train the letter recognition model. Finally, the API sends the inferred board back to the mobile app.

Built using: Python, Flask, TensorFlow, AWS, Docker
