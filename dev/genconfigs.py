import os.path
import shutil

from pyguiadapter.tools.easyconfigs import get_configs_code_generator

OUTPUT_DIR = "./generated_configs"


def prepare_output_dir(path: str):
    if os.path.isdir(path):
        shutil.rmtree(path)

    if not os.path.isdir(path):
        os.makedirs(path, exist_ok=True)


def gen_base_encoder_configs():
    from easy_barcode.common.encoder import BaseEncoder

    output_dir = os.path.join(OUTPUT_DIR, "base_encoder")
    prepare_output_dir(output_dir)

    generator = get_configs_code_generator()

    generator.generate_configs_file(
        func=BaseEncoder.encode, dest_dir=output_dir, onefile=False
    )


def gen_barcode_encoder_configs():
    from easy_barcode.barcode_1d.encoder import BarcodeEncoder

    output_dir = os.path.join(OUTPUT_DIR, "barcode_encoder")
    prepare_output_dir(output_dir)

    generator = get_configs_code_generator()

    generator.generate_configs_file(
        func=BarcodeEncoder.encode, dest_dir=output_dir, onefile=False
    )


def gen_qrcode_encoder_configs():
    from easy_barcode.qrcode_2d.encoder import QRCodeEncoder

    output_dir = os.path.join(OUTPUT_DIR, "qrcode_encoder")
    prepare_output_dir(output_dir)
    generator = get_configs_code_generator()
    generator.generate_configs_file(
        func=QRCodeEncoder.encode, dest_dir=output_dir, onefile=False
    )


if __name__ == "__main__":
    gen_base_encoder_configs()
    gen_barcode_encoder_configs()
    gen_qrcode_encoder_configs()
