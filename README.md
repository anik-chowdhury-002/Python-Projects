Python Projects
This repository contains various Python projects showcasing different functionalities and applications. Below are the details of each project:

1. QR Code Generator
Description
This Python script generates a QR code with a specified URL and saves it as an image file with custom colors.

Prerequisites
Make sure you have Python installed on your machine. You will also need the following Python libraries:

qrcode
Pillow
You can install these dependencies using the following commands:

pip install qrcode[pil]
pip install Pillow

Usage
Save the script as QR_Modified.py.
Modify the URL and the fill and back colors as needed.
Run the script to generate the QR code image.

Output
The script will generate a QR code with the specified URL and save it as c_prog.png in the same directory.
==========================================================================================================

2. Email Validation Program
Description
This Python script validates an email address based on specific criteria. It checks for length, valid characters, proper placement of special characters, and more. If the email address fails any of the checks, the script provides specific error messages indicating why the email is invalid. If the email address passes all checks, it is considered valid.
Algorithm
The algorithm for email validation follows these steps:

1 Input: The user is prompted to enter an email address.
2 Length Check: The email address must be at least 6 characters long.
3 Starting Character: The first character of the email address must be an alphabet letter.
4 Single '@' Character: The email address must contain exactly one '@' character.
5 Dot Position: A dot ('.') must appear either at the 3rd or 4th position from the end of the email address.
6 No Spaces: The email address must not contain any spaces.
7 No Capital Letters: The email address must not contain any capital letters.
8 Allowed Special Characters: Only the special characters '_', '.', and '@' are allowed in the email address.
9 Error Handling: If any of the above checks fail, appropriate error messages are appended to a list and displayed to the user. If no errors are found, the email is declared valid.

Example Inputs and Outputs

1 Input: john.doe@example.com
  Output: Valid email
2 Input: johndoe@ex ample.com
  Output: Email should not contain any spaces.
