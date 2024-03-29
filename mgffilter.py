from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np


def start_app():

    ids = []
    new_ids = []
    mgf_array = []
    included = []
    scan_str = "SCANS="

    def open_txt_file():

        try:
            global ids_file
            global ids

            id_filename = filedialog.askopenfilename()
            ids_file = open(id_filename, "r")
            id_filter = ids_file.read()
            ids = id_filter.split("\n")

            for id in ids:
                if int(id) % 1 == 0:
                    each_id = id.replace(id, scan_str + id + "&")
                    new_ids.append(each_id)  # list

            ids_file.close()

            text_status.delete(1.0, "end")
            text_status.insert(1.0, "Woohoo! IDs file added!")

        except:
            text_status.delete(1.0, "end")
            text_status.insert(1.0, "Oops! Something wrong with the IDs file.")

    def open_mgf_file():
        global mgf_file
        global mgf_array

        mgf_filename = filedialog.askopenfilename()
        mgf_file = open(mgf_filename, "r")
        edited_mgf = mgf_file.read()  # string
        edited_mgf = edited_mgf.replace("\nPEPMASS", "&\nPEPMASS")
        edited_mgf = edited_mgf.replace("END IONS\n\nBEGIN IONS", "END IONS\n#BEGIN IONS")
        mgf_array = edited_mgf.split("#")  # list: each item is an entire mol

        for mol in mgf_array:
            for new_id in new_ids:
                if new_id in mol:
                    mol = mol.replace("&", "")
                    mol = mol.replace("SCANS", "NAME")
                    included.append(mol)

        mgf_file.close()

        text_status.delete(1.0, "end")
        text_status.insert(1.0, "Woohoo! MGF file added!")

    def reset():

        window.destroy()
        start_app()

    def create_file():

        result_filename = input_filename.get("1.0", "end-1c")
        np.savetxt(f"{result_filename}.mgf", included, delimiter=", ", newline="\n", fmt="% s")
        text_status.delete(1.0, "end")
        text_status.insert(1.0, "Filtered file was created!")
        reset()

    window = Tk()
    window.title("MGF Filter")
    window.iconbitmap("mgf-filter.ico")
    window.minsize("500", "300")
    window.configure(bg="#d4eefc")

    # Logo
    logo = Image.open("mgf-filter.png")
    logo = ImageTk.PhotoImage(logo)
    logo_label = Label(image=logo, bg="#d4eefc")
    logo_label.pack(padx=5, pady=30)
    signature = Label(window, text="by Joana Paula Oliveira", bg="#d4eefc", fg="#bf1782", font="Arial").pack(padx=5, pady=0)

    file_btn_1 = Button(window,
                        text="Open IDs File (.txt)",
                        command=open_txt_file,
                        font="Arial",
                        bg="#4dbbeb",
                        fg="#000",
                        activebackground="#bf1782",
                        activeforeground="#FFF").pack(padx=5, pady=20)
    file_btn_2 = Button(window,
                        text="Open MGF Original File (.mgf)",
                        command=open_mgf_file,
                        font="Arial",
                        bg="#4dbbeb",
                        fg="#000",
                        activebackground="#bf1782",
                        activeforeground="#FFF").pack(padx=5, pady=20)
    text_filename = Label(window, text="Choose a filename:", bg="#d4eefc", fg="#000", font="Arial").pack(padx=5, pady=2)
    input_filename = Text(window, height=1, width=30)
    input_filename.pack(padx=5, pady=2)

    label_status = Label(window, text="Status", bg="#d4eefc", fg="#bf1782", font="Arial").pack(padx=5, pady=2)
    text_status = Text(window, bg="#d4eefc", fg="#bf1782", bd=0, font=("Arial", 10), height=2, width=30)
    text_status.config(state='normal')
    text_status.pack(expand=False, padx=5, pady=2)

    run_app = Button(window,
                    text="Filter, please.",
                    command=create_file,
                    font="Arial",
                    bg="#bf1782",
                    fg="#fff",
                    activebackground="#4dbbeb",
                    activeforeground="#000").pack(padx=10, pady=20, side=BOTTOM)

    window.mainloop()

start_app()