import os
from io import BytesIO
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button, Frame, filedialog


def image_to_pdf(image_path, pdf_path):
    for image in image_path:
        # Open image using Pillow library
        image = Image.open(image_path)


        # Add a page to the PDF file
        image = image.convert('RGB')

        img_list = []

        img_list.append(image)

    # Save the PDF file into the given directory.
    image.save(pdf_path, save_all=True)

class ImageToPdfConverter:
    def __init__(self, window):
        self.window = window
        window.title("Image to PDF Converter")

        self.image_paths = []

        self.frame = Frame(window)
        self.frame.pack()

        self.browse_button = Button(self.frame, text="Browse", command=self.browse_images)
        self.browse_button.pack(side="left")

        self.convert_button = Button(self.frame, text="Convert", command=self.convert_images)
        self.convert_button.pack(side="right")

        self.preview_labels = []

    def browse_images(self):
        filetypes = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
        file_paths = filedialog.askopenfilenames(initialdir="./", title="Select Images", filetypes=filetypes)
        self.image_paths = list(file_paths)
        self.show_previews()

    def show_previews(self):
        # Remove existing preview labels
        for label in self.preview_labels:
            label.pack_forget()
        self.preview_labels.clear()

        # Create preview frames for each row of previews
        row_frames = []
        current_frame = None
        for i, image_path in enumerate(self.image_paths):
            if i % 3 == 0:
                current_frame = Frame(self.window)
                current_frame.pack(side="top")
                row_frames.append(current_frame)

            # Open image using Pillow library
            image = Image.open(image_path)
            # Resize image to fit in preview label
            image.thumbnail((100, 100))
            # Convert image to Tkinter PhotoImage
            photo = ImageTk.PhotoImage(image)

            # Create label for preview
            label = Label(current_frame, text=os.path.basename(image_path), image=photo, compound="top", width=100, height=100)
            label.photo = photo
            label.pack(side="left", padx=10, pady=10)

            # Add label to list of preview labels
            self.preview_labels.append(label)



    def convert_images(self):
        output_dir = filedialog.askdirectory(initialdir="./", title="Save PDFs to")

        for image_path in self.image_paths:
            # Create PDF filename based on image filename
            pdf_path = os.path.join(output_dir, os.path.basename(image_path).replace('.jpg', '.pdf'))

            # Convert image to PDF
            image_to_pdf(image_path, pdf_path)

        # Show success message
        success_label = Label(self.window, text="Conversion complete!")
        success_label.pack()

root = Tk()
converter = ImageToPdfConverter(root)
root.mainloop()
