import csv
import sys
from django.db import transaction
from django.core.exceptions import ValidationError
from oficina.models import Oficina

def run(*args):
    if not args:
        print("Error: Favor de proporcionar la ruta al archivo CSV.")
        print("Uso: ./manage.py runscript importar_oficinas --script-args<ruta_al_archivo>")
        sys.exit(1)

    csv_file = args[0]
    try: 
        with open(csv_file, 'r' , encoding='utf-8') as f:
            reader = csv.DictReader(f)
            oficina_a_crear = []

            for row in reader:
                nombre = row.get('nombre')
                nombre_corto = row.get('nombre_corto')

                if not nombre or not nombre_corto:
                    print(f"Error en la fila {row}. Falta un campo")
                    continue

                try:
                    oficina = Oficina(nombre=nombre, nombre_corto=nombre_corto)
                    oficina.full_clean()  # Validador
                    oficina_a_crear.append(oficina)
                except ValidationError as e:
                    print(f"Error de validación en la fila {row},Detalles: {e}")
                except Exception as e:
                    print(f"Error inesperado en la fila {row},Detalles: {e}")
            
            with transaction.atomic():
                Oficina.objects.bulk_create(oficina_a_crear)
                print(f"Importacion de {len(oficina_a_crear)} oficinas completada exitosamente.")
    
    except FileNotFoundError:
        print(f"Error. No se encontro el archivo {csv_file}")
    except Exception as e:
        print(f"Ocurrió un error inesperado en la importación")