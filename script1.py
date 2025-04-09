import cv2

# === Predefined image path ===
IMAGE_PATH = "pic_1.jpg"

def load_image():
    image = cv2.imread(IMAGE_PATH)
    if image is None:
        print(f"Error: Could not load image from {IMAGE_PATH}")
        return None
    return image


def display_image(window_name, img):
    cv2.imshow(window_name, img)


def resize_image(img, scale_percent=25):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    return cv2.resize(img, (width, height))


def convert_to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def main_menu():
    image = load_image()
    if image is None:
        return

    while True:
        print("\n=== Image Processing Menu ===")
        print("1. Show Original Image")
        print("2. Resize Image (75%)")
        print("3. Convert to Grayscale")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_image("Original Image", image)

        elif choice == "2":
            resized = resize_image(image)
            display_image("Resized Image (25%)", resized)

        elif choice == "3":
            gray = convert_to_grayscale(image)
            display_image("Grayscale Image", gray)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

        print("Press any key in the image window to continue...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)


if __name__ == "__main__":
    main_menu()
