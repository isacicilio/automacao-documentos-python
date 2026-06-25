from pypdf import PdfReader



def extrair_texto(caminho):


    leitor = PdfReader(caminho)


    texto = ""


    for pagina in leitor.pages:

        texto += pagina.extract_text()


    return texto