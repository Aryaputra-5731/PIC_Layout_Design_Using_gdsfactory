# PIC_Layout_Design_Using_gdsfactory

MZI Layout Design
This project uses gdsfactory, an open-source Python library, to design a thin-film lithium niobate (TFLN)-based Mach-Zehnder interferometer (MZI), a key component in electro-optic modulators.

Project Overview
The script creates a PIC layout for an MZI, connects waveguide components (splitters, bends, phase shifters), and exports the design as a GDSII file for fabrication. The layout is visualized using gdsfactory’s plotting tools, aligning with QCi’s requirement for chip design support.
Key Features:

Defines TFLN waveguide parameters (500 nm width, 200 nm thickness).
Assembles an MZI with Y-branch splitters, Euler bends, and phase shifters.
Exports the layout to mzi_layout.gds.
Provides bounding box analysis for layout verification.

Python Setup:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install gdsfactory



Usage
Run the script:
python MZI_Layout_Design.py


Outputs:
mzi_layout.gds: GDSII file of the MZI layout.
Console output: Layout visualization and bounding box details.



Dependencies

Python 3.8+
gdsfactory

Install dependencies:
pip install gdsfactory

Example Output

GDSII File: mzi_layout.gds (can be viewed in KLayout or Lumerical).
Console Output:Layout bounding box: [[x_min, y_min], [x_max, y_max]]


Visualization: MZI layout plotted in the console.

Resources

gdsfactory Documentation
gdsfactory GitHub
Ansys Lumerical: GDSII Export
YouTube: gdsfactory Tutorial

License
MIT License. See the LICENSE file for details.
Contact
For questions, open an issue or contact [aryaputradas8@gmail.com].
