import gdsfactory as gf
from gdsfactory.components import mzi
from gdsfactory.generic_tech import get_generic_tech

# Set technology parameters for TFLN
tech = get_generic_tech()
tech.layer_stack.layers["waveguide"].thickness = 0.2  # 200 nm
tech.layer_stack.layers["waveguide"].width = 0.5  # 500 nm

# Create MZI component
mzi_component = mzi(
    delta_length=10.0,  # Phase shifter length (µm)
    splitter=gf.components.y_branch(),
    bend=gf.components.bend_euler(),
    straight=gf.components.straight(length=5.0),
)

# Add ports and labels
mzi_component.add_labels()
mzi_component.add_ports()

# Visualize layout
mzi_component.plot()

# Export to GDSII
mzi_component.write_gds("mzi_layout.gds")
print("MZI layout exported to mzi_layout.gds")

# Analyze dimensions
bbox = mzi_component.bbox
print(f"Layout bounding box: {bbox}")