import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from io import BytesIO
from PIL import Image, ImageOps
import docx2txt
from docx import Document
import base64

png_file_path =""
word_file_path = ""
def embed_text_to_image(text, image_path, output_path):
    global png_file_path,word_file_path
    # Code from RGB to Binary
    def rgb_to_binary(rgb):
        return ''.join(format(value, '08b') for value in rgb)

    def extracting_image_rgb(img_path):
        image = Image.open(img_path)
        pixel_values = list(image.getdata())
        binary_pixel_values = [rgb_to_binary(rgb) for rgb in pixel_values]
        image.close()
        bit = []
        k = ""
        i = 0

        for three_binary in binary_pixel_values:
            for binary in three_binary:
                i+=1
                k+=binary
                if i == 8 or i == 16 or i == 24:
                    bit.append(k)
                    k = ""
                    i = 0
        return bit
    
    def get_png_resolution(image_path):
        try:
            with Image.open(image_path) as img:
                width, height = img.size
                return width, height
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    png_binary = extracting_image_rgb(png_file_path)
    resolution = get_png_resolution(png_file_path)

    length = len(png_binary)
    print(length)
    for i in range(10):
        print(png_binary[i])

    # Code from Word to Binary
    def read_docx(file_path):
        doc = Document(file_path)
        
        # Initialize an empty string to store the text
        text_content = ""

        # Iterate through paragraphs and add text to the string
        for paragraph in doc.paragraphs:
            text_content += paragraph.text + "\n"

        return text_content

    def text_to_binary(text):
        binary_data = ''.join(format(ord(char), '08b') for char in text)
        return binary_data

    word_text = read_docx(word_file_path)
    word_binary = text_to_binary(word_text)

    # Extract binary from image
    png_binary = extracting_image_rgb(image_path) #ini kenapa

    # Extract binary from Word document
    word_text = read_docx(text)
    word_binary = text_to_binary(word_text)

    # Combine binary data
    new_png_binary = []
    length_png = len(png_binary)
    length_word = len(word_binary)

    for i in range(length_word):
        str_png_binary = png_binary[i]
        new_binary = str_png_binary[:-1] + word_binary[i]
        new_png_binary.append(new_binary)

    for i in range(length_word, length_png):
        new_png_binary.append(png_binary[i])

    # Code for construct binary png to png
    def create_image_from_pixel_data(pixel_data, width, height):
        # Create a new image with the specified width and height
        image = Image.new('RGB', (width, height))

        # Create a pixel access object
        pixels = image.load()

        # Set pixel values from the pixel data
        for y in range(height):
            for x in range(width):
                pixel_index = y * width * 3 + x * 3
                pixels[x, y] = (pixel_data[pixel_index], pixel_data[pixel_index + 1], pixel_data[pixel_index + 2])

        return image

    rgb_values = []
    dum_list = []

    for i in range(0, len(new_png_binary), 3):
        dum_list = []
        for j in range(3):
            dum_list.append(int(new_png_binary[i+j],2))
        rgb_values.append(dum_list)

    pixel_data = [value for rgb_list in rgb_values for value in rgb_list]

    image = create_image_from_pixel_data(pixel_data, resolution[0], resolution[1])
    image.save(output_path)

#Halaman 2
    # Function to convert binary to text
    def binary_to_text(binary_string):
        text = ''.join(chr(int(binary_string[i:i + 8], 2)) for i in range(0, len(binary_string), 8))
        return text
    
    # Function to embed text into an image
    def embed_text_to_image(text, image_path, output_path):
        binary_text = ''.join(format(ord(char), '08b') for char in text)
        png_binary = extracting_image_rgb(image_path)

        new_png_binary = []
        length_png = len(png_binary)
        length_text = len(binary_text)

        for i in range(length_text):
            str_png_binary = png_binary[i]
            new_binary = str_png_binary[:-1] + binary_text[i]
            new_png_binary.append(new_binary)

        for i in range(length_text, length_png):
            new_png_binary.append(png_binary[i])

        rgb_values = []
        dum_list = []

        for i in range(0, len(new_png_binary), 3):
            dum_list = []
            for j in range(3):
                dum_list.append(int(new_png_binary[i + j], 2))
            rgb_values.append(dum_list)

        pixel_data = [value for rgb_list in rgb_values for value in rgb_list]

        image = Image.new('RGB', (400, 400))
        pixels = image.load()

        for y in range(400):
            for x in range(400):
                pixel_index = y * 400 * 3 + x * 3
                pixels[x, y] = (pixel_data[pixel_index], pixel_data[pixel_index + 1], pixel_data[pixel_index + 2])

        image.save(output_path)
    # Code from PNG to Binary
def rgb_to_binary(rgb):
    return ''.join(format(value, '08b') for value in rgb)

def extracting_image_rgb(image):
    try:
        # Jika gambar adalah objek PIL, kita dapat melanjutkan
        if isinstance(image, Image.Image):
            pixel_values = list(image.getdata())
            binary_pixel_values = [rgb_to_binary(rgb) for rgb in pixel_values]

            bit = []
            k = ""
            i = 0

            for three_binary in binary_pixel_values:
                for binary in three_binary:
                    i += 1
                    k += binary
                    if i == 8 or i == 16 or i == 24:
                        bit.append(k)
                        k = ""
                        i = 0

            return bit
        else:
            raise ValueError("Objek gambar tidak valid.")
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_png_resolution(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return width, height
    except Exception as e:
        print(f"Error: {e}")
        return None

def binary_to_text(binary_string):
    text = ''.join(chr(int(binary_string[i:i + 8], 2)) for i in range(0, len(binary_string), 8))
    return text

def write_text_to_word(text, output_path='output.docx'):
    # Create a new Word document
    doc = Document()

    # Add the user-input text to the document
    doc.add_paragraph(text)

    # Save the document to the specified path
    doc.save(output_path)
    with open(output_path, 'rb') as file:
        byte_data = file.read()
    return byte_data if byte_data else b''

#Main Streamlit APP
st.set_page_config(
        page_title="STEGO~",
        page_icon=":key",
        initial_sidebar_state="auto",
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
    uploaded_image = st.file_uploader("Pilih file Foto", type=["jpg", "png"], accept_multiple_files=False)
    uploaded_text = st.file_uploader("Pilih file DOCX", type=["docx"], accept_multiple_files=False)

    if st.button("Submit"):
        if uploaded_image is not None and uploaded_text is not None:
            try:
                # Save image and text to temporary files
                temp_image_path = "temp_image.jpg" or "temp_image.png"
                temp_text_path = "temp_text.docx"
                png_file_path = "temp_image.jpg"
                word_file_path ="temp_text.docx"
                with open(temp_image_path, "wb") as temp_image_file:
                    temp_image_file.write(uploaded_image.read())

                with open(temp_text_path, "wb") as temp_text_file:
                    temp_text_file.write(uploaded_text.read())

                # Get image resolution
                with Image.open(temp_image_path) as img:
                    width, height = img.size

                # Embed text to image
                output_image_path = "output_image.png"
                embed_text_to_image(temp_text_path, temp_image_path, output_image_path)

                # Display the output image
                st.image(output_image_path, caption="Gambar yang telah disisipi teks", use_column_width=True)
                # Download button for the output image
                output_image_download_label = "Download Output Image"
                output_image_base64 = base64.b64encode(open(output_image_path, "rb").read()).decode()
                href = f'<a href="data:file/png;base64,{output_image_base64}" download="output_image.png">{output_image_download_label}</a>'
                st.markdown(href, unsafe_allow_html=True)                
            except Exception as e:
                st.error(f"Terjadi kesalahan: {e}")
        else:
            st.write("Silakan pilih file gambar (JPG or PNG) dan file teks (DOCX) sebelum menekan tombol Submit.")  
    def process_uploaded_file(uploaded_file):
        # Memeriksa apakah file telah diunggah
        if uploaded_file is not None:
            if uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":  # Mengecek jika file adalah docx
                # Menggunakan docx2txt untuk mengonversi dokumen Word ke teks
                text_data = docx2txt.process(uploaded_file)
                st.write("Data teks dari dokumen Word (docx):")
                st.write(text_data)
            elif uploaded_file.type == "image/jpeg" or uploaded_file.type == "image/jpg" or uploaded_file.type == "image/png": # Mengecek jika file adalah jpg
                # Menggunakan PIL untuk memuat dan menampilkan gambar JPG
                image = Image.open(uploaded_file)
                st.image(image, caption="Gambar yang diunggah", use_column_width=True)
            else:
                st.write("Tipe file tidak didukung. Harap pilih file dengan tipe docx atau jpg.")

   
elif(selected=="Halaman 2"):
    st.title("Halaman 2")
    uploaded_file = st.file_uploader("Pilih file JPG or PNG", type=["jpg","png"], accept_multiple_files=False)
    if st.button("Submit"):
        # Process the uploaded file
        def process_uploaded_file(uploaded_file):
            if uploaded_file is not None:
                if uploaded_file.type == "image/jpeg" or uploaded_file.type == "image/jpg" or uploaded_file.type == "image/png":
                    image = Image.open(uploaded_file)
                    st.image(image, caption="Gambar yang diunggah", use_column_width=True)
                    png_binary = extracting_image_rgb(image)

                    word_binary = ""
                    for i in range(0, 1600):
                        str_png_binary = png_binary[i]
                        word_binary += str_png_binary[-1]

                    text_result = binary_to_text(word_binary)

                    st.success("Word document created successfully.")

                    # Download button for Word document
                    if st.download_button("Download Word Document", write_text_to_word(text_result), key="download_button"):
                        pass  # Placeholder for button click event

                else:
                    st.write("Tipe file tidak didukung. Harap pilih file dengan tipe jpg.")

        # Process the uploaded file
        process_uploaded_file(uploaded_file)
        


