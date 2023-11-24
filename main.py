import os
import base64
from tkinter import *
from tkinter.filedialog import askdirectory

extensoes = {"audio": [".aac", ".aa", ".aac", ".dvf",
                       ".m4a", ".m4b", ".m4p", ".mp3",
                       ".msv", "ogg", "oga", ".raw",
                       ".vox", ".wav", ".wma"],
             "video": [".avi", ".mkv", ".flv", ".wmv",
                       ".mov", ".mp4", ".webm", ".vob",
                       ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
             "imagens": [".jpeg", ".jpg", ".tiff", ".gif",
                         ".bmp", ".png", ".bpg", "svg", ".heif", ".psd"]}


def organizar():
    diretorio = askdirectory(title="Selecione uma pasta")
    if os.path.isdir(diretorio):
        for arquivo in os.listdir(diretorio):
            caminho_completo = f"{diretorio}/{arquivo}"
            try:
                if os.path.isfile(caminho_completo):
                    for extensao in extensoes["audio"]:
                        if extensao in arquivo:
                            if os.path.exists(f"{diretorio}/audios"):
                                os.rename(caminho_completo, diretorio + "/audios/" + arquivo)
                            else:
                                os.mkdir(f"{diretorio}/audios")
                                os.rename(caminho_completo, diretorio + "/audios/" + arquivo)
                    for extensao in extensoes["video"]:
                        if extensao in arquivo:
                            if os.path.exists(f"{diretorio}/videos"):
                                os.rename(caminho_completo, diretorio + "/videos/" + arquivo)
                            else:
                                os.mkdir(f"{diretorio}/videos")
                                os.rename(caminho_completo, diretorio + "/videos/" + arquivo)
                    if ".pdf" in arquivo:
                        if os.path.exists(f"{diretorio}/pdfs"):
                            os.rename(caminho_completo, diretorio + "/pdfs/" + arquivo)
                        else:
                            os.mkdir(f"{diretorio}/pdfs")
                            os.rename(caminho_completo, diretorio + "/pdfs/" + arquivo)
                    if ".doc" in arquivo:
                        if os.path.exists(f"{diretorio}/words"):
                            os.rename(caminho_completo, diretorio + "/words/" + arquivo)
                        else:
                            os.mkdir(f"{diretorio}/words")
                            os.rename(caminho_completo, diretorio + "/words/" + arquivo)
                    for extensao in extensoes["imagens"]:
                        if extensao in arquivo:
                            if os.path.exists(f"{diretorio}/imagens"):
                                os.rename(caminho_completo, diretorio + "/imagens/" + arquivo)
                            else:
                                os.mkdir(f"{diretorio}/imagens")
                                os.rename(caminho_completo, diretorio + "/imagens/" + arquivo)
                    if ".exe" in arquivo:
                        if os.path.exists(f"{diretorio}/programas"):
                            os.rename(caminho_completo, diretorio + "/programas/" + arquivo)
                        else:
                            os.mkdir(f"{diretorio}/programas")
                            os.rename(caminho_completo, diretorio + "/programas/" + arquivo)
            except PermissionError:
                pass
    texto.configure(text="Arquivos organizados")


janela = Tk()
janela.configure(bg="#294a71")
foto = PhotoImage(data=base64.b64decode(
    """iVBORw0KGgoAAAANSUhEUgAAAIAAAACACAYAAADDPmHLAAAAIGNIUk0AAHomAACAhAAA 
    +gAAAIDoAAB1MAAA6mAAADqYAAAXcJy6UTwAAAAGYktHRAD/AP8A 
    /6C9p5MAAAABb3JOVAHPoneaAAAJKUlEQVR42u3db4xcVRnH8e9zzp07s7vd7bYsFGQriIHyR0KNCS+kCRIbiL7AF6Yv2Bhf 
    +KrvFBSRRInRGoOYQOIbfWViTG3SEKEJ0eoLkYhEDYgJ/gECgq2Gmnbb7rLz5957zuOLO1uEQLk7s8vMcp9PMmk2nT333HN+c865Z 
    +/kgjHGGGOMMcYYY4wxxhhjjDHGGGOMeV+Rtf7Cwrd+hboIqqCCOFlzGRtJoyqiIIJEx8H7bh11lcZa5c67 
    /f5H2ZI1UQVUEe88IorGCOAaLX56zydGchKfu 
    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"""))
janela.iconphoto(False, foto)
janela.title("Organizador de arquivos")
janela.geometry("200x200+550+250")
janela.resizable(False, False)
botao = Button(janela, text="Pasta", font=("arial", "10", "bold"), bg="#5294E2", fg="white", command=organizar,
               width=10, height=2)
botao.pack(pady=10)
texto = Label(janela, font=("arial", "10", "bold"), bg="#294a71", fg="white")
texto.pack(pady=20)
janela.mainloop()
