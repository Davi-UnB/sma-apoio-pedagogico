from pathlib import Path
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling_core.types.doc import ImageRefMode


diretorio = Path("../materiais/")
arquivos = [f for f in diretorio.iterdir() if f.is_file() and not f.name.startswith(".")]
saida = Path("./saidas/")
saida.mkdir(parents=True, exist_ok=True)

pipeline_options = PdfPipelineOptions()
pipeline_options.images_scale = 2.0
pipeline_options.generate_picture_images = True
pipeline_options.generate_table_images = True

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
)

def converterPdfParaMd(arquivo, saida):
    nomedoarquivo = arquivo.name
    result = converter.convert(arquivo)
    md_path = saida / nomedoarquivo.replace(".pdf", ".md")
    result.document.save_as_markdown(
        filename=md_path,
        image_mode=ImageRefMode.REFERENCED
    )

def main():
    for arquivo in arquivos:
        converterPdfParaMd(arquivo, saida)

if __name__ == "__main__":
    main()
    
