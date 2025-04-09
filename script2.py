### This script performs various image processing techniques on a grayscale image.
# It includes contrast stretching, thresholding, graylevel slicing, and bit plane slicing.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load grayscale image
image_path = "pic_2.jpg"  # Replace with your image file
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found.")
    exit()


def plot_histogram(img):
    plt.figure(figsize=(8, 4))
    plt.title("Grayscale Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Frequency")
    plt.hist(img.ravel(), 256, [0, 256], color='gray')
    plt.grid(True)
    plt.show()


def contrast_stretching(img):
    min_val = np.min(img)
    max_val = np.max(img)
    stretched = ((img - min_val) / (max_val - min_val) * 255).astype(np.uint8)
    return stretched


def thresholding(img):
    _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    return thresh


def graylevel_slicing(img, lower=100, upper=150):
    sliced = np.where((img >= lower) & (img <= upper), 255, 0).astype(np.uint8)
    return sliced


def bit_plane_slicing(img):
    planes = []
    for i in range(8):
        plane = cv2.bitwise_and(img, 1 << i)
        plane = np.where(plane > 0, 255, 0).astype(np.uint8)
        planes.append(plane)
        cv2.imshow(f"Bit Plane {i}", plane)
    return planes


def main_menu():
    while True:
        print("\n=== Image Processing Menu ===")
        print("1. Plot Grayscale Histogram")
        print("2. Contrast Stretching")
        print("3. Thresholding")
        print("4. Graylevel Slicing")
        print("5. Bit Plane Slicing")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            plot_histogram(image)

        elif choice == "2":
            result = contrast_stretching(image)
            cv2.imshow("Contrast Stretched", result)

        elif choice == "3":
            result = thresholding(image)
            cv2.imshow("Thresholded Image", result)

        elif choice == "4":
            lower = int(input("Enter lower bound (0–255): "))
            upper = int(input("Enter upper bound (0–255): "))
            result = graylevel_slicing(image, lower, upper)
            cv2.imshow(f"Graylevel Slicing ({lower}-{upper})", result)

        elif choice == "5":
            bit_plane_slicing(image)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

        # Keep images open until a key is pressed
        cv2.imshow("Original", image)
        print("Press any key on the image window to continue...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)


if __name__ == "__main__":
    main_menu()
