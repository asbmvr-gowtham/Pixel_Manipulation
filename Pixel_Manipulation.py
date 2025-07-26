import random
from PIL import Image
def process_image(input_path, output_path, key, mode='encrypt'):

    try:
        img = Image.open(input_path)
        pixels = img.load()
        width, height = img.size

        all_coords = [(x, y) for x in range(width) for y in range(height)]
        
        shuffled_coords = list(all_coords)
        random.seed(key)
        random.shuffle(shuffled_coords)

        new_img = Image.new(img.mode, (width, height))
        new_pixels = new_img.load()

        print(f"Processing '{input_path}' with pixel scramble...")
        
        if mode == 'encrypt':
            for i, (x, y) in enumerate(all_coords):
                new_pixels[shuffled_coords[i]] = pixels[x, y]
        elif mode == 'decrypt':
            for i, (x, y) in enumerate(all_coords):
                new_pixels[x, y] = pixels[shuffled_coords[i]]
        
        new_img.save(output_path)
        print(f"Successfully saved to '{output_path}'")

    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return

if __name__ == "__main__":

    print("Select an operation to perform:")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == '1':
        mode = 'encrypt'
    elif choice == '2':
        mode = 'decrypt'
    else:
        print("Invalid choice. Please enter 1 or 2. Exiting.")
        exit(1)

    try:
        input_image = input("Enter the path for the input image: ").strip()
        output_image = input("Enter the path for the output image: ").strip()
        key = int(input("Enter the secret integer key: ").strip())
    except ValueError:
        print("Invalid key. Please enter a whole number. Exiting.")
        exit(1)
    except Exception as e:
        print(f"An error occurred with the input: {e}")
        exit(1)

    process_image(input_image, output_image, key, mode)
