# Image File Converter

This project allows you to select an image file, choose a source format (PNG, JPEG, JPG), select a target format (PNG, JPEG, JPG), and convert the file into the chosen format.

## Features:
- Choose any image file (PNG, JPEG, JPG).
- Select a source and target file format.
- Convert between PNG, JPEG, and JPG formats.

---

## Table of Contents
1. [How to Add a Source Format](#how-to-add-a-source-format)
2. [How to Add a Target Format](#how-to-add-a-target-format)
3. [Running the Application](#running-the-application)

---

## How to Add a Source Format

If you'd like to support additional source formats (besides PNG, JPG, and JPEG), follow these steps:

### Step 1: Install Pillow (if not installed already)

Ensure you have the Pillow library installed, as it is used for handling image files. You can install it with the following command:

```bash
pip install Pillow
```
### Step 2: Open main.py
In the main.py file, you'll find a dropdown menu (QComboBox) where you select the source format. To add a new source format, you will need to modify the self.source_combo part of the code.

### Step 3: Add the new source format in the source_combo dropdown
Locate the initUI() method in main.py and find the section where source formats are added to the source_combo:

```python
self.source_combo.addItems(['PNG', 'JPEG', 'JPG'])
```
Add your new format to the list inside addItems. For example, to add .bmp (Bitmap) as a new source format:

```python
self.source_combo.addItems(['PNG', 'JPEG', 'JPG', 'BMP'])
```

### Step 4: Enable image conversion for the new format
In the convert_image() function in conversion.py, Pillow already supports many image formats. However, if the new format requires special handling, make sure to add it in the convert_image function.

The existing code automatically handles PNG, JPG, and JPEG. If needed, add specific code for your new format (e.g., bmp handling), but generally, Pillow should handle most image types.

### How to Add a Target Format
To add a new target format (for example, converting to .gif), follow these steps:

### Step 1: Open main.py
As with the source format, the target formats are defined in the target_combo dropdown. Find this code inside the initUI() method:

```python
self.target_combo.addItems(['PNG', 'JPEG', 'JPG'])
```

### Step 2: Add the new target format in the target_combo dropdown
Add your desired target format in the list. For example, to add .gif as a target format:

```python
self.target_combo.addItems(['PNG', 'JPEG', 'JPG', 'GIF'])
```
###  Step 3: Ensure the new target format is supported in the convert_image function
Pillow supports a wide range of formats. If your new target format is supported, you don’t need to add any extra handling. However, if it requires special handling (for example, for .webp or .tiff), you can modify the convert_image() function to account for it.

If no special processing is needed, the convert_image() function should automatically support it, as it uses Pillow's .save() method which works with multiple formats, like .png, .jpg, .jpeg, .gif, etc.

### Running the Application
Once you have added the source or target formats, follow these steps to run the application:

### Step 1: Clone the repository or download the files
If you haven’t already, clone or download the repository to your local machine.

### Step 2: Install the required dependencies
Navigate to your project folder and install the required dependencies (like Pillow) using the following command:

```python
pip install -r requirements.txt
```
If you don't have a requirements.txt, you can manually install Pillow:

```
pip install Pillow
```

### Step 3: Run the main.py file
Open a terminal and navigate to the project directory. Then run the following command:

```bash
python main.py
```

### Step 4: Use the Interface
The application window will appear. Click on the Choose a file button to select an image file.
Choose the source format (if needed).
Choose the target format.
Click Start conversion to convert the file to the target format.
Example: Adding a New Format
If you wanted to add .bmp as both a source and a target format, here’s what you would do:

### Step 1: Add .bmp to the source_combo and target_combo dropdowns
```python
self.source_combo.addItems(['PNG', 'JPEG', 'JPG', 'BMP'])
self.target_combo.addItems(['PNG', 'JPEG', 'JPG', 'BMP'])
```
### Step 2: Modify the convert_image() function (if necessary) to handle .bmp images
However, since Pillow supports BMP natively, no changes should be needed. If you need to perform special handling, use Pillow's .save() function with the appropriate extension (e.g., output_file will automatically handle .bmp).

Conclusion
With these simple steps, you can easily add more image formats as source and/or target formats. Make sure that Pillow supports the format you're adding, and if any specific handling is required, update the convert_image() function accordingly.

Let me know if you need further assistance or clarifications!
