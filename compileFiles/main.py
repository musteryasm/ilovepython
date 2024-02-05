from google.colab import drive
import os

folder_path = '/content/drive/MyDrive/data-20240205T160148Z-001/data'

output_file_path = '/content/drive/MyDrive/d2k/combined_file.txt'

print(f"Folder path: {folder_path}")
print(f"Output file path: {output_file_path}")

for file_name in os.listdir(folder_path):
    print(f"Processing file: {file_name}")
    if file_name.endswith('.txt'):
        file_path = os.path.join(folder_path, file_name)
        print(f"Reading file: {file_path}")
        with open(file_path, 'r') as input_file:
            content = input_file.read()
            print(f"Content length: {len(content)}")

        # Add a breakpoint to pause execution for debugging
        # Uncomment the line below
        # breakpoint()

        with open(output_file_path, 'a') as output_file:
            output_file.write(content + '\n')

print("Combining files completed.")
