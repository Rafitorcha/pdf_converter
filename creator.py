from PIL import Image
from pdf2image import convert_from_path
from pdf2docx import Converter
import img2pdf
import glob
import os

class PDFConverter:
    def __init__(self, folder="images", pdf_folder="pdf_files"):
        self.folder = folder
        self.pdf_folder = pdf_folder
        self.pdf_files = glob.glob(os.path.join(self.pdf_folder, "*.pdf"))
        os.makedirs(self.folder, exist_ok=True)
        os.makedirs(self.pdf_folder, exist_ok=True)

    def menu(self):
        """Menú interactivo para seleccionar el tipo de conversión"""
        print("\n" + "="*40)
        print("CONVERSOR PDF/IMÁGENES".center(40))
        print("="*40)
        print("1. PDF → Imágenes (PNG/JPG)")
        print("2. Imágenes → PDF")
        print("3. Salir")

        while True:
            opcion = input("\nSeleccione una opción (1-3): ")

            if opcion == "1":
                self.pdf_to_images(self.pdf_files)
                break
            elif opcion == "2":
                images_folder = "images_to_convert"
                output_pdf = input("Nombre del PDF resultante: ").strip() + ".pdf"
                self.images_to_pdf(images_folder, output_pdf)
                break
            elif opcion == "3":
                print("¡Hasta luego!")
                return False
            else:
                print("❌ Opción no válida. Intente nuevamente.")
        return True

    def pdf_to_images(self, pdf_path, dpi=300, fmt="PNG"):
        """PDF a imágenes"""
        try:
            number = 0
            for pdf_path in self.pdf_files:
                number = number + 1
                images=convert_from_path(
                    pdf_path,
                    dpi=dpi,
                    fmt=fmt,
                    output_folder=self.folder,
                    output_file=f"{os.path.splitext(os.path.basename(pdf_path))[0]}_page"
                )
                print(f"✅ PDF convertido a imágenes en: {self.folder} {number}/{len(self.pdf_files)}")
            return True
        except Exception as error:
            print(f"❌ Error al convertir PDF a imágenes: {error}")
            return False

    def images_to_pdf(self, img_folder, pdf):
        """Imágenes a PDF"""
        try:
            output_path=os.path.join(self.pdf_folder, pdf)
            img_files = sorted([
                os.path.join(img_folder, file)
                for file in os.listdir(img_folder)
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

    converter.menu()
