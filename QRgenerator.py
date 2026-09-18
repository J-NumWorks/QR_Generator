# QR Generator for NumWorks
# J Wysocki, August 2026

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from pathlib import Path

def generate_qr_code(url, codename):
    """
    Create a QR code instance and save to folder
    :param url: the url to create into a QR code
    :param codename: Name of the image of the QR code
    :return: None
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=2,
    )

    # Add the URL to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    script_folder = Path(__file__).resolve().parent

    # Generate the QR code image
    img = qr.make_image(image_factory=StyledPilImage,
                        module_drawer=RoundedModuleDrawer(),
                        color_mask=SolidFillColorMask(
                            front_color=(255, 183, 52),   # QR-code modules: #ffb734
                            back_color=(255, 255, 255),   # Background: white
                            ),
                        embedded_image_path = script_folder / "N-Logo-Bordered.png")

    # Save the QR code image
    output_folder = script_folder / "codes"
    output_folder.mkdir(parents=True, exist_ok=True)
    #image_file = output_folder / f"{codename}.png"

    img.save(output_folder / f"{codename}.png")

    print(f"\nQR code generated and saved as '{codename}.png'.\n")


def main():
    website = input("\nWhat is the website you would like to QR? ")
    qr_name = input("\nWhat name would you like to give the QR code image? ")
    generate_qr_code(website, qr_name)

if __name__ == "__main__":
    while True:
        main()

        repeat = input("Would you like to create another? (Y or N) ")
        print("--------------------------------------------------\n")

        if repeat.upper() == "N":
            break
