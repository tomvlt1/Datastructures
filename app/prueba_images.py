import pandas as pd

def add_autonumeric_id_proyect(file_name):
    """
    Añade una columna 'id_proyect' autoincremental al archivo CSV especificado.
    
    Parameters:
    file_name (str): El nombre del archivo CSV al que se añadirá la columna.
    
    """
    try:
        # Cargar el dataset desde el archivo CSV
        dataset = pd.read_csv(file_name)
        
        # Verificar si la columna 'id_proyect' ya existe
        if 'id_proyect' in dataset.columns:
            print(f"La columna 'id_proyect' ya existe en '{file_name}'. No se realizará ningún cambio.")
            return
        
        # Crear una lista de IDs autoincrementales comenzando desde 1
        dataset['id_proyect'] = range(1, len(dataset) + 1)
        
        # Guardar el dataset actualizado de vuelta al mismo archivo CSV
        dataset.to_csv(file_name, index=False)
        
        print(f"La columna 'id_proyect' ha sido añadida exitosamente a '{file_name}'.")
        
    except FileNotFoundError:
        print(f"El archivo '{file_name}' no se encontró. Por favor, verifica el nombre y la ruta del archivo.")
    except pd.errors.EmptyDataError:
        print(f"El archivo '{file_name}' está vacío.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Uso de ejemplo
file_name = "generated_project_database.csv"
add_autonumeric_id_proyect(file_name)


