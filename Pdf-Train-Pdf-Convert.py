import os
from pdf2image import convert_from_path
import img2pdf
from datetime import datetime

# Use below function only before running model on images and not after (Comment all)


def pdf_to_images(pdf_path, annotated_img_folder, value = 100):
    os.makedirs(annotated_img_folder, exist_ok=True)

    pages = convert_from_path(pdf_path, dpi=value)

    for i, page in enumerate(pages):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S%f")
        filename = f"page_{i+1}_{timestamp}.png"

        page.save(os.path.join(annotated_img_folder, filename), 'PNG')

    print("All pages from PDF successfully converted into images")


# Use below function only after running model on images and not before (Comment all)


def images_to_pdf(annotated_img_folder, output_pdf_file):
    image_files = [os.path.join(annotated_img_folder, f) for f in os.listdir(annotated_img_folder) if os.path.isfile(os.path.join(annotated_img_folder, f))]

    image_files.sort()

    images = []

    for image in image_files:
        if image.endswith(".png"):
            images.append(os.path.join(annotated_img_folder, image))

    with open(output_pdf_file, "wb") as f:
        f.write(img2pdf.convert(images))

    print("All images succesfully converted into a PDF")

pdf_path = "C:\\Users\\SAGAR DEEP\\Desktop\\Applying_trained_model\\arxiv2.pdf"
image_folder = "C:\\Users\\SAGAR DEEP\\Desktop\\Applying_trained_model\\Extracted_images_3"

annotated_img_folder = "C:\\Users\\SAGAR DEEP\\Desktop\\Applying_trained_model\\Final_Result_arxiv\\exp"

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S%f")
output_pdf_file = f"C:\\Users\\SAGAR DEEP\\Desktop\\Applying_trained_model\\output_{timestamp}.pdf"

pdf_to_images(pdf_path, image_folder)
images_to_pdf(annotated_img_folder, output_pdf_file)