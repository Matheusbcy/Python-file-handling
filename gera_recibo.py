from fpdf import FPDF
from num2words import num2words
from datetime import date

# 1 - Variaveis

cliente = input("Informe o nome do cliente: \n")
consulta = input("Informe o tipo de consulta: \n")
vlr = input("Informe o valor da consulta: \n")
vlr_msg = f"{vlr} reais"
vlr_extenso = num2words(float(vlr), lang="pt_BR")
vlr_extendo_msg = f"{vlr_extenso} reais"
data = date.today()
dia = data.day
mes = data.month
ano = data.year

# 2 - Layout do Recibo

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "", 20)
pdf.image("dados/rec.jpg", x=0, y=0)
pdf.text(162, 45, vlr_msg)
pdf.text(80, 108, vlr_extendo_msg)
pdf.text(80, 135, consulta)
pdf.text(80, 86, cliente)
pdf.set_text_color(255,255,255)
pdf.text(30, 193, str(dia))
pdf.text(50, 193, str(mes))
pdf.text(70, 193, str(ano))
nome_arquivo = f"{cliente.strip()}_{dia}_{mes}_{ano}.pdf"
pdf.output(f"{nome_arquivo}.pdf")
print("Recibo gerado com sucesso!")