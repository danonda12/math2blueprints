import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from io import BytesIO 
import tempfile

st.title("Architectural Blueprint Generator")

# Sidebar options
st.sidebar.header("Blueprint Settings")
#width = st.sidebar.slider("Blueprint Width (in meters):", 10, 50, 50)
width = 50
#height = st.sidebar.slider("Blueprint Height (in meters):", 10, 50, 10)
height = 10
num_rooms = st.sidebar.number_input("Number of Rooms:", 1, 10, 3, step=1)

# Create the blueprint
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, width)
ax.set_ylim(0, height)
ax.set_aspect('equal', adjustable='box')
ax.set_axis_off()

# Generate rooms
for i in range(num_rooms):
    room_width = st.sidebar.slider(f"Room {i + 1} Width (meters):", 1, width, 5)
    room_height = st.sidebar.slider(f"Room {i + 1} Height (meters):", 1, height, 5)
    room_x = st.sidebar.slider(f"Room {i + 1} X-coordinate:", 0, width - room_width, 0)
    room_y = st.sidebar.slider(f"Room {i + 1} Y-coordinate:", 0, height - room_height, 0)

    room_rect = Rectangle((room_x, room_y), room_width, room_height, edgecolor='blue', facecolor='none')
    ax.add_patch(room_rect)

# Display the blueprint
st.pyplot(fig)

# Export the blueprint as an image and provide a download link

with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
    fig.savefig(temp_file, format="png", dpi=300, bbox_inches='tight')

#st.success("Blueprint exported as blueprint.png")

# Create a download link for the image
with open(temp_file.name, "rb") as f:
    data = f.read()
st.download_button(
    label="Download Blueprint",
    data=data,
    file_name="blueprint.png",
    mime="image/png",
)