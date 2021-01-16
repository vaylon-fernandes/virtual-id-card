import tkinter as tk
from tkinter import Label, StringVar, Toplevel, messagebox
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import askyesno
from tkcalendar import DateEntry
from PIL import Image, ImageTk, ImageDraw, ImageFont
from random import randint
import pyqrcode
from pyperclip import copy

class App:
    def __init__(self, root):
        #setting title
        root.title("Virtual ID card creator")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        name_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        name_label["font"] = ft
        name_label["fg"] = "#333333"
        name_label["justify"] = "center"
        name_label["text"] = "Name"
        name_label.place(x=40,y=70,width=70,height=25)

        id_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        id_label["font"] = ft
        id_label["fg"] = "#333333"
        id_label["justify"] = "center"
        id_label["text"] = "ID"
        id_label.place(x=50,y=110,width=70,height=25)

        dob_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        dob_label["font"] = ft
        dob_label["fg"] = "#333333"
        dob_label["justify"] = "center"
        dob_label["text"] = "DOB:"
        dob_label.place(x=40,y=140,width=70,height=25)

        blood_group_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        blood_group_label["font"] = ft
        blood_group_label["fg"] = "#333333"
        blood_group_label["justify"] = "center"
        blood_group_label["text"] = "Blood Group"
        blood_group_label.place(x=20,y=180,width=91,height=30)

        mobile_number_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        mobile_number_label["font"] = ft
        mobile_number_label["fg"] = "#333333"
        mobile_number_label["text"] = "Mobile Number"
        mobile_number_label.place(x=10,y=220,width=91,height=30)

        address_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        address_label["font"] = ft
        address_label["fg"] = "#333333"
        address_label["justify"] = "center"
        address_label["text"] = "Address"
        address_label.place(x=30,y=260,width=70,height=25)

        self.picture_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.picture_label["font"] = ft
        self.picture_label["fg"] = "#333333"
        self.picture_label["justify"] = "center"
        self.picture_label["text"] = "Picture"
        self.picture_label.place(x=340,y=50,width=70,height=25)

        vcmd = root.register(self.validate_name)

        self.name_entry=tk.Entry(root)
        self.name_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.name_entry["font"] = ft
        self.name_entry["fg"] = "#333333"
        self.name_entry["validate"]="key"
        self.name_entry["validatecommand"]= (vcmd, '%S')
        self.name_entry.bind('<space>')
        self.name_entry.place(x=110,y=70,width=147,height=25)

        self.dob_entry=DateEntry(root)
        self.dob_entry["width"] = 12
        ft = tkFont.Font(family='Times',size=10)
        self.dob_entry["font"] = ft
        self.dob_entry["foreground"] = "white"
        self.dob_entry["background"] = "darkblue"
        self.dob_entry.place(x=110,y=140,width=70,height=25)

        self.blood_group_entry=tk.Entry(root)
        self.blood_group_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.blood_group_entry["font"] = ft
        self.blood_group_entry["fg"] = "#333333"
        self.blood_group_entry.place(x=110,y=180,width=70,height=25)
    
        vcmd = root.register(self.validate)

        mobile_number_entry=tk.Entry(root)
        mobile_number_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        mobile_number_entry["font"] = ft
        mobile_number_entry["fg"] = "#333333"
        mobile_number_entry["validate"]="key"
        mobile_number_entry["validatecommand"] = (vcmd,'%P')
        mobile_number_entry.place(x=110,y=220,width=147,height=25)

        self.address_entry=tk.Text(root)
        self.address_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.address_entry["font"] = ft
        self.address_entry["fg"] = "#333333"
        self.address_entry.place(x=110,y=260,width=147,height=58)
        
        gen_id_button=tk.Button(root)
        gen_id_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        gen_id_button["font"] = ft
        gen_id_button["fg"] = "#000000"
        gen_id_button["justify"] = "center"
        gen_id_button["text"] = "Generate ID Card"
        gen_id_button.place(x=120,y=360,width=117,height=30)
        gen_id_button["command"] = self.gen_id

        show_qr_btn=tk.Button(root)
        show_qr_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        show_qr_btn["font"] = ft
        show_qr_btn["fg"] = "#000000"
        show_qr_btn["justify"] = "center"
        show_qr_btn["text"] = "Show QR"
        show_qr_btn.place(x=400,y=360,width=70,height=30)
        show_qr_btn["command"] = self.show_qr

        show_id_btn=tk.Button(root)
        show_id_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        show_id_btn["font"] = ft
        show_id_btn["fg"] = "#000000"
        show_id_btn["justify"] = "center"
        show_id_btn["text"] = "Show ID Card"
        show_id_btn.place(x=280,y=360,width=90,height=30)
        show_id_btn["command"] = self.show_id

        copy_button=tk.Button(root)
        copy_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        copy_button["font"] = ft
        copy_button["fg"] = "#000000"
        copy_button["justify"] = "center"
        copy_button["text"] = "Copy"
        copy_button.place(x=200,y=110,width=35,height=25)
        copy_button["command"] = self.copy_id

        self.id_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.id_label["font"] = ft
        self.id_label["fg"] = "#333333"
        self.id_label["justify"] = "center"
        id_text = f"{self.random_id()}"
        self.id_label["text"] = id_text
        self.id_label.place(x=110,y=110,width=70,height=25)

        virtual_id_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        virtual_id_label["font"] = ft
        virtual_id_label["fg"] = "#333333"
        virtual_id_label["justify"] = "center"
        virtual_id_label["text"] = "Virtual ID Card"
        virtual_id_label.place(x=200,y=0,width=164,height=49)

        self.image_pick_entry=tk.Entry(root)
        self.image_pick_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.image_pick_entry["font"] = ft
        self.image_pick_entry["fg"] = "#333333"
        self.image_pick_entry["justify"] = "center"
        self.image_pick_entry.place(x=280,y=90,width=128,height=25)

        choose_image_btn=tk.Button(root)
        choose_image_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        choose_image_btn["font"] = ft
        choose_image_btn["fg"] = "#000000"
        choose_image_btn["justify"] = "center"
        choose_image_btn["text"] = "Choose Image"
        choose_image_btn.place(x=410,y=90,width=80,height=25)
        choose_image_btn["command"] = self.choose_image

        confirm_button=tk.Button(root)
        confirm_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        confirm_button["font"] = ft
        confirm_button["fg"] = "#000000"
        confirm_button["justify"] = "center"
        confirm_button["text"] = "Confirm"
        confirm_button.place(x=490,y=90,width=70,height=25)
        confirm_button["command"] = lambda: self.confirm(self.get_path())

        exit_button=tk.Button(root)
        exit_button["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        exit_button["font"] = ft
        exit_button["fg"] = "#000000"
        exit_button["justify"] = "center"
        exit_button["text"] = "Exit"
        exit_button.place(x=260,y=410,width=70,height=25)
        exit_button["command"] = self.exit

    def validate(self, text):
        if text == "":
            return True
        elif text == "<space>":
            return True
        elif text.isdigit():
            return True
        else:
            return False

    def validate_name(self, text):
        if text == "":
            return True
        elif text.isspace():
            return True
        elif text.isalpha():
            return True
        else:
            return False

    def get_name(self):
        return self.name_entry.get().title()
    
    def random_id(self):
        lower_limit = 1111111111
        upper_limit = 9999999999
        return randint(lower_limit, upper_limit)

    def get_id(self):
        return self.id_label["text"]

    def get_date(self):
        return self.dob_entry.get()
    
    def get_blood_group(self):
        return self.blood_group_entry.get()
    
    def get_address(self):
        return self.address_entry.get("1.0", "end")

    def get_details(self):
        details = f'''
        Name: {self.get_name()}
        ID: {self.get_id()}
        DoB: {self.get_date()}
        Blood Group: {self.get_blood_group()}
        Address: {self.get_address()}
        '''
        return details
        
    def gen_qr(self):
        data = self.get_details()
        qr = pyqrcode.create(data)
        qr.png("virt_id_qr.png", scale=2)

    def get_qr(self):
        self.gen_qr()
        qr = Image.open('virt_id_qr.png')
        return qr

    def get_template(self):
        path = "templates/vid.png"
        image = Image.open(path)
        return image

    def load_font(self):
        font = ImageFont.truetype('fonts/Calibri Regular.ttf', 40)
        return font

    def gen_id(self):
        details = self.get_details()
        image = self.get_image()
        qr = self.get_qr()
        id_template = self.get_template()
        id_template.paste(im=image, box=(33, 175))
        id_template.paste(im=qr, box=(815, 463))
        edit_image = ImageDraw.Draw(id_template)
        edit_image.text((200, 150), text=details, font=self.load_font(), fill=128)
        id_template.save("Id.png")

    def show_qr(self):
        new_win = tk.Toplevel(root)
        img = Image.open("virt_id_qr.png")
        img = img.resize((186, 186))
        tkimage= ImageTk.PhotoImage(img)
        image_lbl = Label(new_win, image=tkimage)
        image_lbl.image = tkimage
        image_lbl.pack()

    def show_id(self):
        new_win = tk.Toplevel(root)
        img = Image.open("id.png")
        tkimage= ImageTk.PhotoImage(img)
        image_lbl = Label(new_win, image=tkimage)
        image_lbl.image = tkimage
        image_lbl.pack()


    def choose_image(self):
        path = askopenfilename(initialdir='/home/vaylon/github/qr_id/', filetypes=[('Jpeg files','*.jpg *.jpeg'), ('PNG files', '*.png')])
        self.set_path(path) 

    def set_path(self, path):
        self.clear_image_pick_entry()
        self.image_pick_entry.insert(0, path)
    
    def get_path(self):
        return self.image_pick_entry.get()

    def get_image(self):
        image = Image.open(self.get_path())
        image = image.resize((192, 192))
        return image
    
    def clear_image_pick_entry(self):
        self.image_pick_entry.delete(0,"end")

    def confirm(self, path):
        image = self.get_image()
        tkimage = ImageTk.PhotoImage(image)
        display_picture = tk.Label(root, image=tkimage)
        display_picture.image=tkimage
        display_picture.place(x=290,y=130,width=192,height=192)
       
    def copy_id(self):
        text = copy(self.id_label['text'])
        messagebox.showinfo("Copied to clipboard", "Your ID has been copied to the clipboard")

    def exit(self):
        ask_exit = askyesno("Exit", "Do you want to exit?")
        if ask_exit:
            root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    
