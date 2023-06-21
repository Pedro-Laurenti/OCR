import os
import img2pdf

# Diretório da pasta contendo as imagens
diretorio = "C:\\path\\to\\pdf.pdf"

# Lista os arquivos na pasta
arquivos = os.listdir(diretorio)

# Ordena os arquivos por ordem alfabética (opcional)
arquivos = sorted(arquivos)

# Lista para armazenar os caminhos completos das imagens
caminhos_imagens = []

# Loop pelos arquivos na pasta
for arquivo in arquivos:
    # Verifica se o arquivo é uma imagem
    if arquivo.endswith(".jpg") or arquivo.endswith(".jpeg") or arquivo.endswith(".png"):
        # Caminho completo para a imagem
        caminho_imagem = os.path.join(diretorio, arquivo)
        caminhos_imagens.append(caminho_imagem)

# Caminho do arquivo PDF de saída
caminho_pdf = "C:\\path\\to\\pdf.pdf"

# Converte as imagens para PDF
with open(caminho_pdf, "wb") as pdf_output:
    pdf_output.write(img2pdf.convert(caminhos_imagens))

print("PDF gerado com sucesso!")