import sys
import subprocess
import importlib.util
import os

def ensure_package(package):
    if importlib.util.find_spec(package) is None:
        print(f"Installing required package: {package} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print("Restarting script ...")
        os.execv(sys.executable, [sys.executable] + sys.argv)

ensure_package("cryptography")

import datetime
from cryptography import x509
from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.hazmat.primitives import serialization

RED = "\033[31m"
BLUE = "\033[34m"
BLACK = "\033[30m"
RESET = "\033[0m"

ASCII_ART = (
    "██████╗ ███████╗██╗  ██╗ ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗\n"
    "██╔══██╗██╔════╝╚██╗██╔╝██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝\n"
    "██████╔╝█████╗   ╚███╔╝ ██║     ███████║█████╗  ██║     █████╔╝ \n"
    "██╔═══╝ ██╔══╝   ██╔██╗ ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ \n"
    "██║     ██║     ██╔╝ ██╗╚██████╗██║  ██║███████╗╚██████╗██║  ██╗\n"
    "╚═╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝\n"
    "                                                                "
)

TOOL_NAME = "P F X   C E R T I F I C A T E   A N A L Y Z E R"
VERSION = "Version 1.00"
AUTHOR = "By Joshua M Clatney - Ethical Pentesting Enthusiast"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    clear()
    print(f"{RED}{ASCII_ART}{RESET}")
    print(f"{BLUE}{TOOL_NAME}{RESET}   {RED}{VERSION}{RESET}")
    print(f"{BLACK}{AUTHOR}{RESET}")

def load_pfx(path, password):
    with open(path, "rb") as f:
        data = f.read()
    key, cert, _ = pkcs12.load_key_and_certificates(data, password.encode())
    return key, cert

def print_cert_info(label, value):
    print(f"{label}: {value}")

def analyze_certificate(cert):
    print_cert_info("Subject", cert.subject)
    print_cert_info("Issuer", cert.issuer)
    print_cert_info("Serial Number", cert.serial_number)
    print_cert_info("Valid From", cert.not_valid_before)
    print_cert_info("Valid To", cert.not_valid_after)
    print_cert_info("Version", cert.version)
    print_cert_info("Public Key Algorithm", cert.signature_algorithm_oid._name)
    print("\nExtensions:")
    for ext in cert.extensions:
        print(f"- {ext.oid._name}: {ext.value}")

def extend_certificate_expiry(cert, key, days=365):
    new_expiry = cert.not_valid_after + datetime.timedelta(days=days)
    builder = (
        x509.CertificateBuilder()
        .subject_name(cert.subject)
        .issuer_name(cert.issuer)
        .public_key(cert.public_key())
        .serial_number(cert.serial_number)
        .not_valid_before(cert.not_valid_before)
        .not_valid_after(new_expiry)
    )
    for ext in cert.extensions:
        builder = builder.add_extension(ext.value, ext.critical)
    return builder.sign(key, cert.signature_hash_algorithm)

def sanitize_path(path):
    return path.strip().strip('"').strip("'")

def home():
    while True:
        banner()
        print("\nPress Enter to start or Ctrl+C to exit.")
        try:
            inp = input()
        except KeyboardInterrupt:
            print("\nExiting.")
            sys.exit(0)
        if inp.strip() == "":
            main_menu()
            banner()
            print("\nPress Enter to exit.")
            input()
            sys.exit(0)

def main_menu():
    banner()
    raw_path = input("PFX file path: ")
    pfx_path = sanitize_path(raw_path)
    password = input("PFX password: ").strip()
    try:
        key, cert = load_pfx(pfx_path, password)
    except Exception as e:
        print(f"\nError loading PFX: {e}")
        print("Press Enter to return to home screen.")
        input()
        return
    print("\nChoose an option:")
    print("1. Analyze certificate")
    print("2. Extend certificate expiry by 1 year")
    print("3. Analyze and extend")
    choice = input("Selection (1/2/3): ").strip()
    if choice in {"1", "3"}:
        print()
        analyze_certificate(cert)
    if choice in {"2", "3"}:
        out_path = input("\nOutput path for extended certificate (PEM): ").strip()
        new_cert = extend_certificate_expiry(cert, key)
        with open(out_path, "wb") as f:
            f.write(new_cert.public_bytes(encoding=serialization.Encoding.PEM))
        print(f"Extended certificate saved to {out_path}")
    print("\nPress Enter to return to the home screen.")
    input()

if __name__ == "__main__":
    home()