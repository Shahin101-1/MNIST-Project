# MNIST Handwritten Digit Recognition (MindSpore)/ huawei course project

A neural network built with MindSpore that recognizes handwritten digits (0-9) from the MNIST dataset. It also includes a small drawing window (PyQt5) so you can draw your own digit and have the model predict it.

# Results
- Model: 3-layer fully connected network (784 -> 512 -> 128 -> 10)
- Training: 10 epochs, Adam optimizer, learning rate 0.0003 (you can increase it if your PC is better than mine)
- Test accuracy: 97.9%  (for me it got some numbers wrong but not too far off I advise you to draw in 40 to 50 width so the AI can understand it)

# Requirements
- Python 3.11
- mindspore, numpy, matplotlib, pillow, PyQt5

Install with:
pip install mindspore numpy matplotlib pillow PyQt5

# How to run
1. Download this repository, the file name is "Mnist_file"
2. Open a terminal in the project folder.
3. Run: python Mnist_file
4. When you run the script make sure to run it twice, the first time draw your number and the second time The script trains the model and prints the test accuracy and the guessed number.
5. A drawing window then opens. Draw a digit, save it as a number only ex: "5" and it will appear as 5.png in the project folder) and close the window.
6. The script loads the image and prints the predicted digit (make sure to change the directory in the code at line 258).

# Files
- Mnist_file: The Main code
- test.py: A file I used to test the drawing app, not necessary but you can use it to draw your number (from 0-9) to skip starting the main code twice.
- datasets/: MNIST training and test data
