import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from io import BytesIO
from PIL import Image, ImageOps
import docx2txt



st.set_page_config(
        page_title="STEGO~",
        page_icon=":dinosaurs",
        #layout="wide",