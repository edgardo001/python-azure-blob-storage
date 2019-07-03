# ----------------------------------------------------------------------------------
# MIT License
#
# Copyright(c) Microsoft Corporation. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# ----------------------------------------------------------------------------------
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


# pip install azure-storage-blob
from azure.storage.blob import BlockBlobService, PublicAccess, ContentSettings
import os, uuid, sys
from datetime import datetime
# https://pynative.com/python-generate-random-string/
import random
import string

# ---------------------------------------------------------------------------------------------------------
# Método que crea un archivo de prueba
# Esta aplicación de muestra crea un archivo de prueba, carga el archivo de prueba al almacenamiento de Blob,
# lista los blobs en el contenedor y descarga el archivo con un nuevo nombre.
# ---------------------------------------------------------------------------------------------------------
# Documentation References:
# Associated Article - https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python
# What is a Storage Account - http://azure.microsoft.com/en-us/documentation/articles/storage-whatis-account/
# Getting Started with Blobs-https://docs.microsoft.com/en-us/azure/storage/blobs/storage-python-how-to-use-blob-storage
# Blob Service Concepts - http://msdn.microsoft.com/en-us/library/dd179376.aspx
# Blob Service REST API - http://msdn.microsoft.com/en-us/library/dd135733.aspx
# ----------------------------------------------------------------------------------------------------------

# Generador de String Aleatorio
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

# Generador de String y Digitos Aleatoreos
def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

# Generador de Numeros aleatoreos
def randomDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

# Generador de nombres aleatoreos
def generateRandonName():
    #dato.CL90010131.D01SJV3V7K_1.ci.2019-06-18.p32HM.pdf
    primero = 'dato'
    segundo = 'CL'+ randomDigits(8)
    tercero = randomString(12)
    cuarto = randomString(2)
    quinto = datetime.now().strftime("%Y-%m-%d")
    sexto = randomString(5)
    septimo = 'pdf'    
    return primero + '.' + segundo + '.' + tercero + '.' + cuarto + '.' + quinto + '.' + sexto + '.' + septimo


def run_sample():
    try:
        # Cree el BlockService que se usa para llamar al servicio Blob para la cuenta de almacenamiento
        block_blob_service = BlockBlobService(account_name='Nombre_Cuenta_de_almacenamiento', account_key='clave_de_acceso')

        # Nombre del conetenedor
        container_name ='contenedor'
        # Crea el contenedor
        #block_blob_service.create_container(container_name)

        # Establezce el permiso para que los blobs sean públicas.
        #block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)

        # Crea un archivo en Documentos para probar la carga y descarga.
        local_path=os.path.abspath(os.path.curdir)
        #local_file_name =input("Ingrese el nombre del archivo para subir: ")
        local_file_name ="demo.pdf"
        full_path_to_file =os.path.join(local_path, local_file_name)

        # En caso de generar un txt
        # Escribir texto en el archivo.
        #file = open(full_path_to_file,  'w')
        #file.write("Hello, World!")
        #file.close()

        print("Archivo temporal = " + full_path_to_file)
        print("\nSubiendo al BlobStorage como blob: " + local_file_name)

        # Generando nombre aleatoreo    
        nameRandon = generateRandonName()
        print("Random Name: " + nameRandon)
        # Upload the created file, use local_file_name for the blob name
        block_blob_service.create_blob_from_path(container_name, nameRandon, full_path_to_file,content_settings=ContentSettings(content_type='application/pdf'))

        # =====================================================================
        # Las siguientes lineas no han sido probadas, 
        # pero deben ser funcionales con algunos cambios en los nombres de descaga del archivo
        # =====================================================================

        # Lista los blobs en el contenedor
        #print("\nLista los blobs en el contenedor")
        #generator = block_blob_service.list_blobs(container_name)
        #for blob in generator:
        #    print("\t Nombre Blob: " + blob.name)

        # Descarga de blob(s).
        # Agrega '_DOWNLOADED' como prefijo a '.txt'.
        #full_path_to_file2 = os.path.join(local_path, str.replace(local_file_name ,'.txt', '_DOWNLOADED.txt'))
        #print("\nDescargando Blob a: " + full_path_to_file2)
        #block_blob_service.get_blob_to_path(container_name, local_file_name, full_path_to_file2)

        #sys.stdout.write("La muestra terminó de correr. Cuando presiona <cualquier tecla>, la muestra se eliminará y la aplicación de muestra se cerrará.")
        #sys.stdout.flush()
        #input()

        # Limpiar los recursos. Esto incluye el contenedor y los archivos temporales.
        #block_blob_service.delete_container(container_name)
        #os.remove(full_path_to_file)
        #os.remove(full_path_to_file2)
    except Exception as e:
        print(e)


# Main method.
if __name__ == '__main__':
    run_sample()



