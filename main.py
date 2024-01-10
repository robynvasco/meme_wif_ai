import streamlit as st
import replicate
import os

# Set your replicate API token
REPLICATE_API_TOKEN = "r8_F9k**********************************"

# Authenticate using the API token
replicate.set_api_key(REPLICATE_API_TOKEN)

# Streamlit app
st.title("Image Inpainting with replicateAPI")

# Image and mask paths

image_path = "images/your_image.jpg"
mask_path = "images/your_mask.png"


# Prompt input
prompt = st.text_input("Prompt", "Inpaint the image within the masked area.")

# Inpaint button
if st.button("Inpaint"):
    if os.path.exists(image_path) and os.path.exists(mask_path):
        # Read image and mask contents
        with open(image_path, "rb") as img_file, open(mask_path, "rb") as mask_file:
            image_content = img_file.read()
            mask_content = mask_file.read()

        # Run the model with replicateAPI
        output = replicate.run(
            "pagebrain/dreamshaper-v8:6cb38fe374c4fd4d5bb6a18dcdd71b08512f25bbf1753f8db4bb22f1d5fea9be",
            input={"image": image_content, "mask": mask_content, "prompt": prompt},
        )

        # Display the inpainted image
        st.image(output[0], caption="Inpainted Image", use_column_width=True)
    else:
        st.warning("Please enter valid paths for both the image and the mask.")
