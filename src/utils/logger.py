import logging
from pathlib import Path

Path("logs").mkdir(exist_ok=True)


logging.basicConfig(

    filename="logs/processo.log",

    level=logging.INFO,

    format="%(asctime)s - %(levelname)s - %(message)s"

)


def registrar(mensagem):

    logging.info(mensagem)