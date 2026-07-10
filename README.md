# PolyaticCipher 

PolyaticLingo is a lightweight, secure single file local desktop application built in Python that translates text using a custom substitution cipher. It features a modern, clean graphical user interface (GUI), tracking history saved directly to a local CSV log, and a seamless Windows integration that supports custom taskbar pinning.

---

## 🚀 Features

* **Custom Polyatic Cipher:** A unique, letter-swapping translation system based on a custom layout seed.
* **Persistent Translation History:** Automatically logs your previous inputs, outputs, and timestamps to a local `codes.csv` file.
* **Clipboard Integration:** Copy your results with a single click.
* **Windows Taskbar Optimization:** Uses custom `ctypes` Application User Model IDs to ensure your application logo displays correctly on both the window title bar and the taskbar.

---

## 🗺️ The Code Map

The translation engine relies on a bidirectional letter-swapping map. Non-alphabetical characters and spaces remain completely untouched to preserve syntax and numbers.

| Input | Output |   | Input | Output |   | Input | Output |
| :---: | :----: | - | :---: | :----: | - | :---: | :----: |
|  **a** |   h    |   |  **j** |   q    |   |  **s** |   g    |
|  **b** |   y    |   |  **k** |   w    |   |  **t** |   n    |
|  **c** |   i    |   |  **l** |   e    |   |  **u** |   v    |
|  **d** |   f    |   |  **m** |   r    |   |  **v** |   u    |
|  **e** |   l    |   |  **n** |   t    |   |  **w** |   k    |
|  **f** |   d    |   |  **o** |   x    |   |  **x** |   o    |
|  **g** |   s    |   |  **p** |   z    |   |  **y** |   b    |
|  **h** |   a    |   |  **q** |   j    |   |  **z** |   p    |
|  **i** |   c    |   |  **r** |   m    |   | **space** | space |

---

## LATEST RELEASE: 1.1.0S 

### Prerequisites
* Python 3.10+
---
### ROAD MAP
* make it C++ or C# to run without downloading anything
* add style

