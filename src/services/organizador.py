import shutil

from src.config import (
    PASTA_ENTRADA,
    PASTA_SAIDA
)

from src.utils.logger import registrar



def organizar_documentos():


    PASTA_SAIDA.mkdir(
        exist_ok=True
    )


    for arquivo in PASTA_ENTRADA.iterdir():


        if arquivo.is_file():


            extensao = arquivo.suffix.lower()


            pasta_destino = (
                PASTA_SAIDA / extensao.replace(".", "")
            )


            pasta_destino.mkdir(
                exist_ok=True
            )


            shutil.move(

                arquivo,

                pasta_destino / arquivo.name

            )


            registrar(
                f"{arquivo.name} movido"
            )


    return True