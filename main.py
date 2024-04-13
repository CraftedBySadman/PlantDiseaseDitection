import google.generativeai as genai
import config
import tkinter as tk
import customtkinter as ctk
from customtkinter import filedialog 
import PIL.Image

def generate():
    file_path = filedialog.askopenfilename()
    img = PIL.Image.open(file_path)
    image = ctk.CTkImage(light_image=img,dark_image=img,size=(250,250))
    label.configure(image=image)

    genai.configure(api_key=config.GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(["I want to know what plant it is? Is it healthy or not.If it has a disease which disease is it? why it happends. and How to cure it.", img], stream=True)
    response.resolve()

    print(response.text)
    result.insert("0.0",response.text)

root = ctk.CTk()
root.geometry("750x550")
root.title("Plant Disease Ditection")
titleLable = ctk.CTkLabel(root,text="🌱 Plant Disease Ditection",
                          font=ctk.CTkFont(family="Montserrat",size = 30,weight = "bold"))
titleLable.pack(padx = 10,pady = (40,20))
frame = ctk.CTkFrame(root,bg_color="gray85")
frame.pack(fill = "x",padx = 100,pady = 20)
upload_image_labl = ctk.CTkLabel(frame,text="Upload an image",
                                font=ctk.CTkFont(size = 15,weight="bold") )
upload_image_labl.pack(side="left",padx = (20,10),pady =10)
maxsize_label = ctk.CTkLabel(frame,text="Limit 200 MB per file (JPG,JPEG,PNG)",
                                font=ctk.CTkFont(size = 10) )
maxsize_label.pack(side="left")

button = ctk.CTkButton(frame, text="Browse File", fg_color="black",command=generate)
button.pack(padx=10, pady=10)
image_frame = ctk.CTkFrame(root)
image_frame.pack(padx=100,pady=5)


label = ctk.CTkLabel(image_frame,text="")
label.pack(pady=10)

result =ctk.CTkTextbox(root,font=ctk.CTkFont(size=15))
result.pack(padx=100,fill="x",pady =10)

nlabel = ctk.CTkLabel(root,text="NB: All the responses are generated by AI.")
nlabel.pack()

# Run the Tkinter event loop
root.mainloop()
