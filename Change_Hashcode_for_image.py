import hashlib
import random


def modify_file_byte(file_path):
    with open(file_path, 'rb') as file:
        data = bytearray(file.read())

    # Generate a random index to modify
    index = random.randint(0, len(data) - 1)

    # Generate a random byte to replace the existing byte
    new_byte = random.randint(0, 255)

    # Modify the byte at the randomly chosen index
    data[index] = new_byte

    # Write the modified data to a new file
    modified_file_path =  'modified-' + file_path
    with open(modified_file_path, 'wb') as modified_file:
        modified_file.write(data)

    return modified_file_path


def calculate_hash(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        hash_obj = hashlib.sha256(data)
        return hash_obj.hexdigest()


# Example usage
input_file_path = 'example.jpg'  # Replace with the path to your input file

original_hash = calculate_hash(input_file_path)
print(f'Original Hash: {original_hash}')

modified_file_path = modify_file_byte(input_file_path)
modified_hash = calculate_hash(modified_file_path)
print(f'Modified Hash: {modified_hash}')
