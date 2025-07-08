# PFXCheck, a PFX Certificate Analyzer

**By Joshua M Clatney — Ethical Pentesting Enthusiast**

---

## Overview

**PFX Certificate Analyzer** is a Python tool for analyzing and managing PKCS#12 (`.pfx` / `.p12`) certificates.
It is designed for professionals who need a straightforward way to extract, inspect, and optionally extend X.509 certificates bundled in PFX files, with a strong focus on usability and automation.

Key features include:

* **Automatic dependency installation** (installs `cryptography` if missing, no user action needed)
* **User-friendly CLI interface** with ASCII art and colored output for clarity
* **Detailed certificate information** including subject, issuer, validity, version, algorithm, and all extensions
* **One-click certificate expiry extension** (adds 1 year to expiry and exports as PEM)
* **Robust handling of file paths**, including paths pasted with surrounding quotes

---

## Features

* **Certificate Analysis:**
  Quickly extracts and displays all important fields and extensions from any `.pfx`/`.p12` file.

* **Expiry Extension:**
  Easily extend the expiry of a certificate by one year and export the new cert as a PEM file.

* **Zero-Hassle Setup:**
  On first run, the script checks for required Python packages and installs them automatically.

* **Smart Path Handling:**
  The script automatically strips leading/trailing quotes (`"`, `'`) from pasted file paths, reducing user error.

* **Interactive Home Screen:**
  After each operation, users can return to the main menu or exit cleanly.

---

## Installation

1. **Requirements:**

   * Python 3.8 or newer

2. **No manual dependencies required.**
   The script will auto-install `cryptography` the first time it runs.

3. **Get the script:**

   * Download `PFXCheck` from this repository.

---

## Usage

1. **Run the script:**

2. **Follow the prompts:**

   * Press Enter at the welcome screen to begin.
   * Paste or type the path to your `.pfx` or `.p12` file (quotes around the path are fine).
   * Enter the PFX password when prompted.
   * Select an action:

     * `1` Analyze the certificate
     * `2` Extend expiry by one year and export
     * `3` Analyze and extend

3. **Output:**

   * For analysis, detailed certificate info is printed to the screen.
   * For extension, you will be prompted to provide an output filename (e.g. `mycert_extended.pem`).

4. **Navigation:**

   * After any operation, press Enter to return to the home screen, or Enter again to exit.

---

## Example Session

```
██████╗ ███████╗██╗  ██╗ ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗
██╔══██╗██╔════╝╚██╗██╔╝██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝
██████╔╝█████╗   ╚███╔╝ ██║     ███████║█████╗  ██║     █████╔╝ 
██╔═══╝ ██╔══╝   ██╔██╗ ██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ 
██║     ██║     ██╔╝ ██╗╚██████╗██║  ██║███████╗╚██████╗██║  ██╗
╚═╝     ╚═╝     ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
P F X   C E R T I F I C A T E   A N A L Y Z E R   Version 1.00
By Joshua M Clatney - Ethical Pentesting Enthusiast

Press Enter to start or Ctrl+C to exit.

PFX file path: "C:\Users\you\Desktop\certificate.pfx"
PFX password: *****
Choose an option:
1. Analyze certificate
2. Extend certificate expiry by 1 year
3. Analyze and extend
Selection (1/2/3): 1

Subject: <Name(CN=example.com,...)>
Issuer: <Name(CN=CA,...)>
Serial Number: ...
Valid From: ...
Valid To: ...
...

Press Enter to return to the home screen.
```

---

## Troubleshooting

* If you receive a file not found error, double-check your path. The script ignores extra quote marks.
* The script must be run in a terminal/console that supports ANSI color codes (most modern terminals do).

---

## License

This project is released under the Apache 2.0 License

---

**Questions, issues, or suggestions?**
Open an issue or PR on GitHub, or contact the author.

---
