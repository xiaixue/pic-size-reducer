# Picture size reducer

This is a script that helps you reduce the size of your images by scaling them to a specified width. It is an useful tool where manual resizing is tedious or unavailable on mobile, hundreds of high-res images eat up space or there is limited cloud storage. You can apply this to:
* All images inside a single folder.
* All images inside multiple subfolders.

This tool is ideal for:

* Compressing images before sharing or uploading.
* Standardizing image sizes across directories.
* Reducing storage usage for large image sets.

It has the following features:
* Resize all `.jpg`, `.jpeg`, and `.png` files to a target width.
* Choose whether to resize a single folder or a directory with multiple subfolders.
* Automatically skips images that are already smaller than the target size.
* Preserves aspect ratio while resizing.
* Simple and clean GUI to select folders using a file dialog

### Notes

> 🖼️ The aspect ratio is preserved, the height is automatically adjusted.

> 📏 The script does not upscale images smaller than the target width.

> 💾 All images are overwritten in-place with the resized versions.

---
## Example

> Run `picture_resizer.py`.

> Choose whether to resize. A for a single folder and B across multiple subfolders

> Enter the desired target width in pixels

> Select the folder using the file dialog window that pops up.

## Folder Structure Examples
Option A: Single folder
```
root_folder/
├── img1.jpg
├── img2.png
├── img3.jpeg
```
Option B: Multiple subfolders
```
root_folder/
├── project1/
│   ├── img1.jpg
│   ├── img2.png
├── project2/
│   ├── img3.jpg
│   └── img4.png
```