import streamlit as st
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

st.set_page_config(
  page_title="Virtual Try-On",
  page_icon=None,
  layout="wide",
  menu_items={
      "Get Help": None,
      "Report a bug": "https://twitter.com/sageOlamide",
      "About": None
  }
)
# Title with a link to Gemini 2.0
st.markdown('# Virtual Try-On with [Gemini 2.0](https://developers.googleblog.com/en/experiment-with-gemini-20-flash-native-image-generation/)') 

with st.expander("How to use"):
    st.write("""
        - Enter the fashion item you want to try on in the text box.
        - Upload an image of the fashion item.
        - Upload an image of yourself or another person.
        - The app will generate an image of the person wearing the fashion item using Gemini.
        - Click the "Reset App" button to start over.
    """)

if st.button("Reset App"):
    st.rerun()

# Text input for fashion item
fashion_item = st.text_input("What fashion item would you like to try on?", placeholder="sneakers")

# Check if fashion item is entered
if not fashion_item.strip():
    st.error("Please enter a fashion item to proceed.")
else:
    # Create columns for images and uploaders
    col1, col2, col3 = st.columns(3)

    with col1:
        # Upload picture of a fashion item
        fashion_item_image = st.file_uploader("Upload image of fashion item (cloth, shoe, etc.)", type=["jpg", "png", "jpeg"])

        # Display fashion item image
        if fashion_item_image is not None:
            fashion_image = Image.open(fashion_item_image)
            st.image(fashion_image, caption='Fashion Item', use_container_width=True)

    with col2:
        # Upload user's picture
        user_image = st.file_uploader("Upload image of person to try it on", type=["jpg", "png", "jpeg"])

        # Display user's image
        if user_image is not None:
            person_image = Image.open(user_image)
            st.image(person_image, caption='Your Picture', use_container_width=True)

    # Ensure both images and fashion item text are provided
    if fashion_item and fashion_item_image and user_image:
        with col3:
            with st.spinner("Generating image...", show_time=True):
                try:
                    # Initialize Google Gemini AI Client
                    client = genai.Client(api_key=st.secrets["gemini_api_key"])

                    # Define the text input prompt
                    text_input = (
                    f"Here are two images: one of a person and one of a {fashion_item}. "
                    f"Please edit the image so that the person is wearing the {fashion_item}."
                    f"The generated image should be the same height and width as the {person_image}."
                )

                    # Generate response from Gemini 2.0
                    response = client.models.generate_content(
                        model="gemini-2.0-flash-exp-image-generation",
                        contents=[text_input, person_image, fashion_image],  # Pass both images
                        config=types.GenerateContentConfig(response_modalities=['Text', 'Image'])
                    )

                    # Process the response and display the generated image
                    for part in response.candidates[0].content.parts:
                        if part.text is not None:
                            st.write(part.text)  # Display any textual response
                        elif part.inline_data is not None:
                            try:
                                output_image = Image.open(BytesIO(part.inline_data.data))
                                st.write("")
                                st.write("")
                                st.write("")
                                st.write("")
                                st.write("")
                                st.write("")
                                st.title("Generated Image")
                                st.image(output_image, caption='Generated Image', use_container_width=True)
                            except Exception as e:
                                st.error(f"Error loading generated image: {e}")
                except Exception as e:
                    st.error(f"Failed to generate image: {e}")
