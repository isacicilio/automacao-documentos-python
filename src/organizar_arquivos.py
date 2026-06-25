import os
import shutil


def organizar_documentos():

    origem = "../documentos"

    destino_pdf = "../resultado/PDF"

    destino_outros = "../resultado/Outros"


    os.makedirs(destino_pdf, exist_ok=True)

    os.makedirs(destino_outros, exist_ok=True)



    for arquivo in os.listdir(origem):

        caminho = os.path.join(origem, arquivo)


        if arquivo.endswith(".pdf"):

            shutil.move(
                caminho,
                destino_pdf
            )

        else:

            shutil.move(
                caminho,
                destino_outros
            )


    print("Documentos organizados!")