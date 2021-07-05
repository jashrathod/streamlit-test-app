import streamlit as st
# from CogView import cogview, model_stop # Backend file which would be responsibe for all of CogView's functionality

st.title("Creating Images from Text")

st.write("Once you are done, type in \"stop\" as the text prompt.")

text_prompt = st.text_area("Text prompt")

if st.button("Generate Image"):
    if text_prompt == "stop":
        # model_stop() # A function which would stop the model
        st.write("Model has been stopped!")
    elif text_prompt == "denim chair":
        path_to_imgs = ["output_images/00000000.jpg", 
                        "output_images/00000001.jpg", 
                        "output_images/00000002.jpg", 
                        "output_images/00000003.jpg"] # Taking random images for now
        # path_to_imgs = cogview(text_prompt) # This function would give out the final image paths

        col1, col2, col3, col4 = st.beta_columns(4)
        with col1:
            st.image(path_to_imgs[0], width=150)
        with col2:
            st.image(path_to_imgs[1], width=150)
        with col3:
            st.image(path_to_imgs[2], width=150)
        with col4:
            st.image(path_to_imgs[3], width=150)
    
    else:
        path_to_imgs = ["output_images/00000004.jpg", 
                        "output_images/00000005.jpg", 
                        "output_images/00000006.jpg", 
                        "output_images/00000007.jpg"] # Taking random images for now
        # path_to_imgs = cogview(text_prompt) # This function would give out the final image paths

        col1, col2, col3, col4 = st.beta_columns(4)
        with col1:
            st.image(path_to_imgs[0], width=150)
        with col2:
            st.image(path_to_imgs[1], width=150)
        with col3:
            st.image(path_to_imgs[2], width=150)
        with col4:
            st.image(path_to_imgs[3], width=150)
        