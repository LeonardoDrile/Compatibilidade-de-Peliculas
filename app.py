import pandas as pd
import customtkinter as ctk

# Carrega os dados da planilha
df = pd.read_excel("tabela_peliculas_tabela_formatada.xlsx")

# Função de busca
def buscar_modelo():
    termo = entrada.get().strip().lower()
    resultados = df[df["Modelo"].str.lower().str.contains(termo)]
    texto_resultado.configure(state="normal")
    texto_resultado.delete("1.0", "end")
    
    if not resultados.empty:
        for index, row in resultados.iterrows():
            texto_resultado.insert("end", f"📱 Modelo: {row['Modelo']}\n")
            texto_resultado.insert("end", f"🔗 Compatíveis:\n{row['Compatíveis']}\n")
            texto_resultado.insert("end", "\n" + "-" * 50 + "\n\n")

    else:
        texto_resultado.insert("end", "❌ Nenhum modelo encontrado.")
    
    texto_resultado.configure(state="disabled")

# Interface
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Buscar Películas Compatíveis")
app.geometry("600x500")

label = ctk.CTkLabel(app, text="Digite o modelo:", font=("Arial", 16))
label.pack(pady=10)

entrada = ctk.CTkEntry(app, width=400, placeholder_text="Ex: note 12")
entrada.pack(pady=5)

botao = ctk.CTkButton(app, text="🔍 Pesquisar", command=buscar_modelo)
botao.pack(pady=10)

texto_resultado = ctk.CTkTextbox(app, width=550, height=350, font=("Arial", 12))
texto_resultado.pack(pady=10)
texto_resultado.configure(state="disabled")

app.mainloop()
