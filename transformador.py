import csv
import json

print("Iniciando escaneo con el Motor Nativo de Python...")

lista_materias = []

# 1. Abrimos el archivo en modo lectura de texto puro
with open('maestro.csv', mode='r', encoding='utf-8') as archivo:
    lector = csv.reader(archivo)
    
    # 2. Iteramos fila por fila
    for numero_fila, fila in enumerate(lector):
        # Ignoramos la primera fila (los encabezados problemáticos)
        if numero_fila == 0:
            continue
            
        # Si la fila está vacía o rota, la ignoramos y pasamos a la siguiente
        if len(fila) < 4:
            continue

        # 3. Extracción de datos fijos (Sabemos que las primeras 4 son Sigla, Grupo, Materia, Docente)
        sigla = fila[0].strip()
        grupo = fila[1].strip()
        materia = fila[2].strip()
        docente = fila[3].strip()
        
        horarios = []
        
        # 4. Extracción Dinámica a prueba de balas
        # Empezamos a leer desde la columna 4 (que es el primer DIA) y saltamos de 2 en 2
        for i in range(4, len(fila), 2):
            # Verificamos que exista la pareja de Día y Hora en esta fila irregular
            if i + 1 < len(fila):
                dia = fila[i].strip()
                hora = fila[i+1].strip()
                
                # Si hay datos válidos, los partimos
                if dia != "" and hora != "":
                    try:
                        inicio, fin = hora.split('-')
                        horarios.append({"dia": dia, "inicio": inicio.strip(), "fin": fin.strip()})
                    except ValueError:
                        # Si la universidad escribió mal la hora, la máquina lo ignora sin colapsar
                        pass
                        
        # 5. Armamos el objeto JSON final
        materia_obj = {
            "sigla": sigla,
            "grupo": grupo,
            "materia": materia,
            "docente": docente,
            "horarios": horarios
        }
        lista_materias.append(materia_obj)

# 6. Carga (Load) de la base de datos limpia
with open('ofertas.json', 'w', encoding='utf-8') as f:
    json.dump(lista_materias, f, indent=4, ensure_ascii=False)

print(f"¡Extracción exitosa! Se procesaron {len(lista_materias)} materias en tu base de datos.")