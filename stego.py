import cv2
import os
import string

# Load the image
img = cv2.imread("car.jpg")  # Replace with the correct image path

if img is None:
    print("Error: Unable to load image. Please check the image path.")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {}
c = {}

# Mapping characters to integers and vice versa
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

height, width, channels = img.shape  # Get the dimensions of the image

m, n, z = 0, 0, 0  # Initialize coordinates for the pixel

# Encode the message into the image
for i in range(len(msg)):
    if m >= width:
        m = 0
        n += 1
    if n >= height:
        print("Message is too long to hide in the image.")
        exit()

    img[n, m, z] = d[msg[i]]  # Assign the encoded value to the image pixel
    m += 1
    z = (z + 1) % 3  # Cycle through the RGB channels

# Save the modified image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Open the image on Windows

# Decrypt the message
message = ""
n, m, z = 0, 0, 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):
        if m >= width:
            m = 0
            n += 1
        if n >= height:
            break

        message += c[img[n, m, z]]  # Extract the encoded character
        m += 1
        z = (z + 1) % 3  # Cycle through the RGB channels

    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED.")

