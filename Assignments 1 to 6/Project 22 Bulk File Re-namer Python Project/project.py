import os

def bulk_rename(folder_path, new_name, file_ext=None):
    files = os.listdir(folder_path)
    count = 1

    for file in files:
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1]

            # Only rename files with given extension if specified
            if file_ext and ext != file_ext:
                continue

            new_filename = f"{new_name}_{count}{ext}"
            new_full_path = os.path.join(folder_path, new_filename)

            os.rename(full_path, new_full_path)
            print(f"Renamed: {file} → {new_filename}")
            count += 1

# Example usage
folder = r"D:\MyFiles\Images"
bulk_rename(folder, "image", ".jpg")
