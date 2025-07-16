from PIL import Image
from pdf2image import convert_from_path
# from pdf2docx import Converter
import img2pdf
import os

class PDFConverter:
    def __init__(self, folder="images"):
        self.folder = folder
        os.makedirs(self.folder, exist_ok=True)

    def pdf_to_images(self, pdf_path, dpi=300, fmt="PNG"):
        """PDF a imágenes"""
        try:
            images=convert_from_path(
                pdf_path,
                dpi=dpi,
                fmt=fmt,
                output_folder=self.folder,
                output_file="page"
            )
            print(f"✅ PDF convertido a imágenes en: {self.folder}")
            return True
        except Exception as error:
            print(f"❌ Error al convertir PDF a imágenes: {error}")
            return False

    def images_to_pdf(self, folder, pdf):
        """Imágenes a PDF"""
        try:
            output_path=os.path.join(self.folder, pdf)
            img_files = sorted([
                os.path.join(folder, file)
                for file in os.listdir(folder)
                if file.lower().endswith(('.jpg', '.jpeg', '.png'))
            ])
            if not img_files:
                print("❌ No hay imágenes válidas en la carpeta.")
                return False

            with open(output_path, "wb") as pdf_file:
                pdf_file.write(img2pdf.convert(img_files))

            print(f"✅ Imágenes convertidas a PDF en: {output_path}")
            return True
        except Exception as error:
            print(f"❌ Error al convertir imágenes a PDF: {error}")
            return False

if __name__ == "__main__":
    converter = PDFConverter()
    converter.pdf_to_images(pdf_path="pdf_files/prueba.pdf")
    # converter.images_to_pdf(folder="images_to_convert", pdf="prueba.pdf")
