import customtkinter as ctk #Importanto bivliteoca de interface

# Configurando a aparência da interface

ctk.set_appearance_mode("dark") # Modo escuro

ctk.set_default_color_theme("blue")

app = ctk.CTk() # Criando a janela principal

app.title("Gerador de SQL - UHs") # Título da janela

app.geometry("700x500") # Tamanho da janela

app.mainloop() # Mantendo a janela aberta
