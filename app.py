import os

import streamlit as st
from PIL import Image

# import tkinter as tk
# from tkinter import filedialog

# # import emoji
# # from matplotlib import container


# # favicon = "man-man-girl-girl"
# def pick_folder(container, key):
#     # Set up tkinter
#     root = tk.Tk()
#     root.withdraw()

#     # Make folder picker dialog appear on top of other windows
#     root.wm_attributes('-topmost', 1)

#     # Folder picker button
#     # container.text('Folder Picker')
#     container.write(f'Please select a folder ({key}):')
#     clicked = container.button('Folder Picker', key=f"Folder Picker button {key}")
#     dirname = None
#     if clicked:
#         dirname = container.text_input('Selected folder:', filedialog.askdirectory(master=root))
#         return dirname

def main():

    st.set_page_config(page_title='Compare Photos ' +
                       u'\U0001F5BC', page_icon=u'\U0001F5BC', layout="wide")
    # print(emoji.emojize(':framed_picture:'))

    container_input = st.sidebar.container()
    num_directories = int(container_input.number_input(
        "Number of directories", min_value=1, max_value=10, value=2, step=1))
    column_num = container_input.slider(
        "Column", min_value=1, max_value=num_directories, value=2, step=1, key="col")
    row_num = -(-1*num_directories//column_num)
    # st.text(f"{row_num=}")
    container_images = st.container()
    container_images_dict = {}
    image_path_dict = {}
    max_length = 0
    for row in range(row_num):
        cols = container_images.columns(column_num)
        for col, container_col in enumerate(cols):
            idx = row*column_num + col
            key = str(idx)
            container_images_dict[idx] = container_col
            if idx >= num_directories:
                break
            # dirname = pick_folder(container_col, key=f"{row=}, {col=}")
            dirname = None
            dirname = container_col.text_input(
                "directory", key=f"directory path {key}")
            image_path_dict[idx] = {"len": 0}
            if dirname is not None and dirname != "":
                # container_col.write(f"{dirname=}")
                # container_col.write(f"{os.listdir(dirname)=}")
                onlyfiles = [f for f in os.listdir(dirname) if os.path.isfile(
                    os.path.join(dirname, f)) and f.split('.')[-1] in ["jpg", "jpeg", "png"]]
                # container_col.write(f"{onlyfiles=}")
                image_path_dict[idx]["dirname"] = dirname
                image_path_dict[row*column_num +
                                col]["filename"] = sorted(onlyfiles)
                image_path_dict[idx]["len"] = len(onlyfiles)
                if image_path_dict[idx]["len"] > max_length:
                    max_length = image_path_dict[idx]["len"]
    num = int(container_input.number_input(
        "Num", min_value=1, max_value=max_length, value=2, step=1))
    # zoom_img = container_input.slider('', min_value=10, max_value=5000, value=2000, step=1,)
    for row in range(row_num):
        cols = container_images.columns(column_num)
        for col, container_col in enumerate(cols):
            idx = row*column_num + col
            key = f"{idx}"
            if idx >= num_directories:
                break
            if image_path_dict[idx]["len"] > 0:
                if image_path_dict[idx]["len"] > num-1:
                    # im = Image.open("/home/jitesh/prj/belt-hook/sample_2.png")
                    im = Image.open(os.path.join(
                        image_path_dict[idx]["dirname"], image_path_dict[idx]["filename"][num-1]))
                    container_images_dict[idx].header(
                        f'{image_path_dict[idx]["filename"][num-1]} {key=}')
                    container_images_dict[idx].image(im,
                                                                      # width=zoom_img,
                                                                      use_column_width=True
                                                                      )


if __name__ == '__main__':
    main()
