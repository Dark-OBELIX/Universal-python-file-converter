import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QVBoxLayout, QLabel, QComboBox
from PyQt5.QtCore import QDir
import os
from conversion import convert_image  # Import the conversion function

class FileSelectorApp(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize the UI
        self.initUI()

    def initUI(self):
        # Create a label to display the selected file and its extension
        self.label = QLabel('No file selected', self)

        # Create a button to open the file selection dialog
        self.button = QPushButton('Choose a file', self)
        self.button.clicked.connect(self.open_file_dialog)

        # Create a dropdown menu to choose the source file format (PNG, JPEG, JPG)
        self.source_combo = QComboBox(self)
        self.source_combo.addItems(['PNG', 'JPEG', 'JPG'])
        self.source_combo.setDisabled(True)  # Disabled until a file is selected

        # Create a dropdown menu to choose the target file format (PNG, JPEG, JPG)
        self.target_combo = QComboBox(self)
        self.target_combo.addItems(['PNG', 'JPEG', 'JPG'])
        self.target_combo.setDisabled(True)  # Disabled until a file is selected

        # Create a button to start the conversion
        self.convert_button = QPushButton('Start conversion', self)
        self.convert_button.setDisabled(True)  # Disabled initially
        self.convert_button.clicked.connect(self.convert_file)  # Connect to the conversion function

        # Layout for arranging the widgets vertically
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        layout.addWidget(self.source_combo)
        layout.addWidget(self.target_combo)
        layout.addWidget(self.convert_button)

        # Set the layout for the main window
        self.setLayout(layout)

        # Window configuration
        self.setWindowTitle('File Selector and Conversion')
        self.setGeometry(300, 300, 400, 300)

    def open_file_dialog(self):
        # Open a file dialog to choose any file
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFiles)
        dialog.setFilter(QDir.AllEntries)  # Allow all file types

        if dialog.exec_():
            # Get the selected file
            file_name = dialog.selectedFiles()[0]

            # Extract the file extension
            file_extension = os.path.splitext(file_name)[1].lower()

            # Display the selected file and its extension in the label
            self.label.setText(f'Selected file: {file_name}\nExtension: {file_extension}')

            # Enable the dropdown menus and the conversion button
            self.source_combo.setEnabled(True)
            self.target_combo.setEnabled(True)
            self.convert_button.setEnabled(True)

            # Set the source format based on the selected file's extension
            if file_extension == '.png':
                self.source_combo.setCurrentText('PNG')
            elif file_extension == '.jpg' or file_extension == '.jpeg':
                self.source_combo.setCurrentText('JPEG')

            # Save the file path for later use
            self.selected_file = file_name

    def convert_file(self):
        # Get the selected source and target formats
        source_extension = self.source_combo.currentText().lower()
        target_extension = self.target_combo.currentText().lower()

        # Check if the source and target formats are different
        if source_extension == target_extension:
            self.label.setText("The source and target formats must be different.")
            return

        # Generate the output file name with the target extension
        output_file = os.path.splitext(self.selected_file)[0] + f'.{target_extension}'

        # Call the conversion function
        success = convert_image(self.selected_file, output_file)

        if success:
            self.label.setText(f'File successfully converted: {output_file}')
        else:
            self.label.setText(f'Conversion failed')

if __name__ == '__main__':
    # Create and start the Qt application
    app = QApplication(sys.argv)
    window = FileSelectorApp()
    window.show()
    sys.exit(app.exec_())
