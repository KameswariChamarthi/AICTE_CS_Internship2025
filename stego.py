import cv2
import os

# Load Image
image_path = r"d:\Downloads\project_supportfiles-main\project_supportfiles-main\5825739.jpg"
 # Ensure this is the correct path
img = cv2.imread(image_path)

if img is None:
    print("Error: Image not found. Check the file path!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Create character lookup tables
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

height, width, _ = img.shape  # Get image dimensions

n, m, z = 0, 0, 0  # Initialize pixel position

# Embed the message into the image
for i in range(len(msg)):
    if n >= height or m >= width:
        print("Error: Message too long for this image!")
        exit()
    
    img[n, m, z] = d[msg[i]]  # Modify the pixel value
    m += 1
    if m >= width:  # Move to the next row if width limit is reached
        m = 0
        n += 1
    z = (z + 1) % 3  # Rotate between R, G, B

# Save the stego image
stego_path = "stego_image.jpg"
cv2.imwrite(stego_path, img)
print(f"Message hidden successfully! Saved as {stego_path}")

# Open image
os.system(f"start {stego_path}")

# Decryption
message = ""
n, m, z = 0, 0, 0  # Reset position

pas = input("Enter passcode for decryption: ")
if password == pas:
    for i in range(len(msg)):
        if n >= height or m >= width:
            break
        message += c[img[n, m, z]]
        m += 1
        if m >= width:
            m = 0
            n += 1
        z = (z + 1) % 3
    print("Decrypted message:", message)
else:
    print("Unauthorized access! Decryption failed.")
