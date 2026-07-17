import customtkinter as ctk
from tkinter import filedialog

from hotel_manager import listar_nomes, buscar_id
from excel_reader import ler_planilha
from sql_generator import gerar_sql_manutencao

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Gerador SQL - Sistema IO")
        self.geometry("900x650")
        self.resizable(False, False)

        self.caminho_excel = ""

        self.criar_componentes()

    def criar_componentes(self):

        # ---------- HOTEL ----------

        self.label_hotel = ctk.CTkLabel(
            self,
            text="Hotel",
            font=("Arial", 18, "bold")
        )
        self.label_hotel.pack(pady=(20, 5))

        self.combo_hotel = ctk.CTkComboBox(
            self,
            values=listar_nomes(),
            width=400
        )
        self.combo_hotel.pack()

        # ---------- EXCEL ----------

        self.label_excel = ctk.CTkLabel(
            self,
            text="Arquivo Excel",
            font=("Arial", 18, "bold")
        )
        self.label_excel.pack(pady=(20, 5))

        self.frame_excel = ctk.CTkFrame(self)
        self.frame_excel.pack()

        self.label_arquivo = ctk.CTkLabel(
            self.frame_excel,
            text="Nenhum arquivo selecionado",
            width=350,
            anchor="w"
        )
        self.label_arquivo.pack(side="left", padx=10, pady=10)

        self.botao_excel = ctk.CTkButton(
            self.frame_excel,
            text="Selecionar",
            command=self.selecionar_excel
        )
        self.botao_excel.pack(side="left", padx=10)

        # ---------- BOTÃO GERAR ----------

        self.botao_gerar = ctk.CTkButton(
            self,
            text="GERAR SQL",
            width=250,
            height=40,
            command=self.gerar_sql
        )
        self.botao_gerar.pack(pady=20)

        # ---------- SQL ----------

        self.label_sql = ctk.CTkLabel(
            self,
            text="SQL Gerado",
            font=("Arial", 18, "bold")
        )
        self.label_sql.pack()

        self.textbox = ctk.CTkTextbox(
            self,
            width=800,
            height=250
        )
        self.textbox.pack(pady=10)

        # ---------- BOTÕES ----------

        self.frame_botoes = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_botoes.pack()

        self.botao_copiar = ctk.CTkButton(
            self.frame_botoes,
            text="Copiar SQL",
            command=self.copiar_sql
        )
        self.botao_copiar.pack(side="left", padx=10)

        self.botao_limpar = ctk.CTkButton(
            self.frame_botoes,
            text="Limpar",
            command=self.limpar
        )
        self.botao_limpar.pack(side="left")

    def selecionar_excel(self):

        caminho = filedialog.askopenfilename(
            filetypes=[("Excel", "*.xlsx *.xls")]
        )

        if caminho:
            self.caminho_excel = caminho
            self.label_arquivo.configure(text=caminho.split("/")[-1])

    def gerar_sql(self):

        # Verifica se um arquivo foi escolhido
        if not self.caminho_excel:
            print("Selecione um arquivo Excel.")
            return

        # Nome do hotel escolhido
        hotel = self.combo_hotel.get()

        # Busca o ID do hotel
        id_hotel = buscar_id(hotel)

        # Lê a planilha
        dados = ler_planilha(self.caminho_excel)

        # Gera o SQL
        sql = gerar_sql_manutencao(dados, id_hotel)

        # Mostra o SQL na tela
        self.textbox.delete("1.0", "end")
        self.textbox.insert("1.0", sql)

    def copiar_sql(self):

        sql = self.textbox.get("1.0", "end")

        self.clipboard_clear()
        self.clipboard_append(sql)

    def limpar(self):

        self.textbox.delete("1.0", "end")