from PIL import Image
import os
from tkinter import filedialog as fd

def resize_images_in_folder(folder_path, target_width=800):
  for filename in os.listdir(folder_path):
    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
      continue

    filepath = os.path.join(folder_path, filename)

    try:
      with Image.open(filepath) as img:
        width, height = img.size
        rate = target_width / width

        if rate >= 1:
          continue  # No agrandar

        new_size = (int(width * rate), int(height * rate))
        resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
        resized_img.save(filepath, dpi=(72, 72))
        print(f"Resized: {filepath}")

    except Exception as e:
      print(f"Error resizing {filepath}: {e}")

def resize_images_in_subfolders(base_dir, target_width=800):
  for subfolder in os.listdir(base_dir):
    subfolder_path = os.path.join(base_dir, subfolder)
    if not os.path.isdir(subfolder_path):
      continue

    for filename in os.listdir(subfolder_path):
      if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

      filepath = os.path.join(subfolder_path, filename)

      try:
        with Image.open(filepath) as img:
          width, height = img.size
          rate = target_width / width

          if rate >= 1:
            continue

          new_size = (int(width * rate), int(height * rate))
          resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
          resized_img.save(filepath, dpi=(72, 72))

      except Exception as e:
        print(f"Error resizing {filepath}: {e}")
        
def isInt(num):
  try:
    int(num)
    return True
  except:
    return False
  
def main():
  print("""
📷 Picture size reducer

A) Reduce pictures in a single folder
B) Reduce pictures in multiple subfolders
""")

  while True:
    folder_mode = input("Choose A or B: ").strip().lower()
    if folder_mode in ["a", "b"]:
      break

  while True:
    width_input = input("Choose the desired width for the pictures (in px): ").strip()
    if isInt(width_input):
      target_width = int(width_input)
      if target_width > 0:
        break
    print("❌ Not a valid width. Please enter a positive number.")

  selected_folder = fd.askdirectory(title="Select folder")
  if not selected_folder:
    print("❌ No folder selected. Exiting.")
    return

  if folder_mode == "a":
    resize_images_in_folder(selected_folder, target_width=target_width)
  else:
    resize_images_in_subfolders(selected_folder, target_width=target_width)

  print("✅ Resizing complete.")
      
if "__main__" == __name__:
  main()