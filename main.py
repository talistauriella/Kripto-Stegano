import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from io import BytesIO
from PIL import Image, ImageOps
import docx2txt
from docx import Document



st.set_page_config(
        page_title="STEGO~",
        page_icon=":key",
        #layout="wide",
        initial_sidebar_state="auto",
        menu_items={
                'Get Help' : None,
                'About' : None, 
        }
)

with st.sidebar:
    selected = option_menu("Main Menu", ["Home", "Halaman 1", "Halaman 2"],
    icons=['house', 'gear', 'key'], menu_icon="cast", default_index=0)
if(selected=="Home"):
    st.title("About Steganografi Paper")
    st.caption("Ini adalah halaman utama web")
    st.text_area("Definisi Steganografi",
                    "Menurut Munir (2009), Steganografi adalah ilmu dan seni menyembunyikan"
                    "pesan rahasia (hiding message) sedemikian sehingga keberadaan (eksistensi)"
                    "pesan yang tidak terdeteksi oleh indera manusia." )
    st.subheader("Cara Kerja")
    st.markdown("***Cara Kerja Steganografi***")
    st.markdown("1. Input Image dan Input Text")
    st.markdown("2. Program dieksekusi")
    st.markdown("3. Output Image yang mempunyai pesan tersembunyi didalamnya")
    st.markdown("***Cara Program Mengeksekusi***")
    st.markdown("1. Mengekstrak setiap bit dari Image dan Mengekstrak bit dari test")
    st.markdown("2. Menggunakan LSB untuk menyisipkan setiap digit bit text ke Image")
    st.markdown("3. Menciptakan kembali Image yang telah disisipi bit di akhir bitnya")

elif(selected=="Halaman 1"):
    st.title("Halaman 1")
    # Membuat komponen untuk mengunggah file dengan dukungan untuk beberapa file.
    uploaded_file = st.file_uploader("Pilih file (docx atau jpg)", 
                                    type=["docx", "jpg"],
                                    accept_multiple_files=False)

    def process_uploaded_file(uploaded_file):
        # Memeriksa apakah file telah diunggah
        if uploaded_file is not None:
            if uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":  # Mengecek jika file adalah docx
                # Menggunakan docx2txt untuk mengonversi dokumen Word ke teks
                text_data = docx2txt.process(uploaded_file)
                st.write("Data teks dari dokumen Word (docx):")
                st.write(text_data)
            elif uploaded_file.type == "image/jpeg" or uploaded_file.type == "image/jpg": # Mengecek jika file adalah jpg
                # Menggunakan PIL untuk memuat dan menampilkan gambar JPG
                image = Image.open(uploaded_file)
                st.image(image, caption="Gambar yang diunggah", use_column_width=True)
            else:
                st.write("Tipe file tidak didukung. Harap pilih file dengan tipe docx atau jpg.")

    if st.button("Submit"):
        # Memeriksa apakah file telah diunggah
        if uploaded_file is not None:
            # Memproses file yang diunggah
            process_uploaded_file(uploaded_file)
        else:
            st.write("Silakan pilih file sebelum menekan tombol Submit.")
elif(selected=="Halaman 2"):
    st.title("Halaman 2")
    # Membuat komponen untuk mengunggah file dengan dukungan untuk beberapa file.
    uploaded_file = st.file_uploader("Pilih file JPG", 
                                    type=["jpg"],
                                    accept_multiple_files=False)
    def process_uploaded_file(uploaded_file):
        # Memeriksa apakah file telah diunggah
        if uploaded_file is not None:
            if uploaded_file.type == "image/jpeg" or uploaded_file.type == "image/jpg":  # Mengecek jika file adalah jpg
                # Menggunakan PIL untuk memuat dan menampilkan gambar JPG
                image = Image.open(uploaded_file)
                st.image(image, caption="Gambar yang diunggah", use_column_width=True)
            else:
                st.write("Tipe file tidak didukung. Harap pilih file dengan tipe jpg.")
    if st.button("Submit"):
        # Memeriksa apakah file telah diunggah
        if uploaded_file is not None:
            # Memproses file yang diunggah
            process_uploaded_file(uploaded_file)
        else:
            st.write("Silakan pilih file sebelum menekan tombol Submit.")
    


