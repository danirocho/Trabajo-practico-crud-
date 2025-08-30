import csv
import sys
from django.db import transaction
from django.core.exceptions import ValidationError
from oficina.models import Oficina
from persona.models import Persona

def run(*args):
    if not args:
        print("Error: Favor de proporcionar la ruta al archivo CSV.")
        print("Uso: ./manage.py runscript importar_personas --script-args<ruta_al_archivo>")
        sys.exit(1)

    csv_file = args[0]

    oficinas_map = {oficina.nombre_corto: oficina for oficina in Oficina.objects.all()}

    try: 
        with open(csv_file, 'r' , encoding='utf-8') as f:
            reader = csv.DictReader(f)
            persona_a_crear = []

            for row in reader:
                nombre = row.get('nombre')
                apellido = row.get('apellido')
                edad = row.get('edad')
                oficina_nombre_corto = row.get('oficina_nombre_corto')

                if not nombre or not edad:
                    print(f"Error en la fila {row}. Falta el nombre o la edad")
                    continue

                try:
                    edad = int(edad)
                except (ValueError, TypeError):
                    print(f"Error en la fila {row}. La edad debe ser un numero valido")
                    continue

                oficina_obj = None
                if oficina_nombre_corto:
                    oficina_obj = oficinas_map.get(oficina_nombre_corto)
                    if not oficina_obj:
                        print(f"Warning: No existe oficina mencionada{row}")
                        print(f"se creara la persona sin oficina")
                
                try:
                    persona = Persona(
                    nombre=nombre,
                    apellido=apellido,
                    edad=edad,
                    oficina=oficina_obj)
                    persona.full_clean()
                    persona_a_crear.append(persona)
                except ValidationError as e:
                    print(f"Error de validacion en la fila {row}. Detalles: {e}")
                except Exception as e:
                    print(f"Error inesperado en la fila {row}. Detalles: {e}")
            with transaction.atomic(): 
                Persona.objects.bulk_create(persona_a_crear)
                print(f"se importaron {len(persona_a_crear)} registros") 

    except FileNotFoundError:  
        print(f"Error: No se encontro el archivo {csv_file}")
    except Exception as e:
        print(f"Ocurrio un error inesperado en la importacion")