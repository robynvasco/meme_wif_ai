import streamlit as st
import replicate

# Set your replicate API token
REPLICATE_API_TOKEN = "r8_F9k**********************************"

# Authenticate using the API token
replicate.set_api_key(REPLICATE_API_TOKEN)

# Streamlit app
st.title("Image Inpainting with replicateAPI")

# Upload image and mask files
uploaded_image = st.file_uploader("Upload Image", type=["jpg", "png"])
uploaded_mask = st.file_uploader("Upload Mask", type=["jpg", "png"])

# Prompt input
prompt = st.text_input("Prompt", "Inpaint the image within the masked area.")

# Inpaint button
if st.button("Inpaint"):
    if uploaded_image is not None and uploaded_mask is not None:
        # Run the model with replicateAPI
        output = replicate.run(
            "pagebrain/dreamshaper-v8:6cb38fe374c4fd4d5bb6a18dcdd71b08512f25bbf1753f8db4bb22f1d5fea9be",
            input={
                "image": uploaded_image.read(),
                "mask": uploaded_mask.read(),
                "prompt": prompt,
            },
        )

        # Display the inpainted image
        st.image(output[0], caption="Inpainted Image", use_column_width=True)
    else:
        st.warning("Please upload both an image and a mask before inpainting.")

