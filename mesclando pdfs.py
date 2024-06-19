import PyPDF2
import os

#função para mesclar os pdfs
mesclar = PyPDF2.PdfMerger()


listaArquivos = os.listdir("arquivos")
listaArquivos.sort()
print(listaArquivos)

#buscando os arquivos para a mesclagem e realizando-a
for arquivo in listaArquivos:
    if ".pdf" in arquivo:
        mesclar.append(f"pdfs/{arquivo}")

mesclar.write("resultado Mesclagem.pdf")