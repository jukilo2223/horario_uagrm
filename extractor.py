import pdfplumber

archivo_pdf = "MAESTRO DE OFERTA 2-2025.pdf"

print("Iniciando escaneo de diagnóstico en modo texto crudo...")

with pdfplumber.open(archivo_pdf) as pdf:
    # Seleccionamos solo la primera página (índice 0)
    primera_pagina = pdf.pages[0]
    
    # Extraemos el texto puro en lugar de buscar tablas
    texto = primera_pagina.extract_text()
    
    print("\n--- LO QUE LA MÁQUINA VE ---")
    print(texto)
    