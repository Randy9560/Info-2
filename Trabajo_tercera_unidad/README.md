# Trabajo Tercera Unidad
<p align="justify">
Bienvenid@, en este trabajo se encontrara un codigo en el que se procesa toda la informacion de estudios DICOM, asi mismo como su visualizacion con NILEARN.
La idea del README es proporcionarle al usuario una guia de como utilizar el codigo
</p>


## **Instrucciones**
<p align="justify">
La guia constara de x pasos para todo el procesamiento de informacion y visualizacion de imagenes.
</p>

## **Paso 0 - Definicion del problema**
<p align="justify">
Se desea crear un codigo, el cual resiva estudios, los cuales seran archivos DICOM, y se desea que su informacion sea procesada, ademas de esto, se desea tener una base de datos interna
que me identifique estudios dependiendo de pacientes, especificamente hablando se desea identificar los estudios con el ID del paciente, y poder asiganr eliminar o consultar informacion
de un paciente en especifico usando como filtrador el ID del paciente, ademas de esto, se desea lograr la visualizacion de los estudios por medio de la libreria NILEARN.
</p>

## **Paso 1 - Configiracion del entorno de trabajo**
<p align="justify">
 Para preparar el entorno es muy ideal, que se tengan instaladas todas las librerias necesarias para correr el codigo, en este apartado se mencionaran las librerias utilizadas, 
 asi mismo se enseñara como instalarlas y llamarlas al codigo:

 - Las librerias utilizadas son:
  
    - **Manipulación y visualización de imagenes**
  
       - **nilearn**
        ```
        #Instalacion
        
         python -m pip install nilearn
        ```
        ```
        #Importacion
        
         import nilearn
        ```
      - **Se usa el metodo 'plotting' de la libreria nilearn para visualizar las imagenes**
        ```
        #Importacion
        
         from nilearn import plotting
        ```
    - **Procesamiento de datos**

      - **pydicom**
        ```
        #Instalacion
         
         python -m pip install pydicom
        ```
        ```
        #Importacion
         
         import nilearn
        ```

      - **Se usa el metodo 'dcmread' de la libreria pydicom para leer los archivos .dcm**
        ```
        #Importancion
         
         from pydicom import dcmread
        ```
    - **Conversion de datos**

      - **dicom2nifti**
        ```
        #Instalacion
        
         python -m pip install dicom2nifti
        ```
        
        ```
        #Importancion
         
         import dicom2nifti
        ```
    - **Librearias para manejo interno del codigo**
      
        Estas librerias no necesitan ser instaladas, solo necesitan ser importadas
  
      - OS, random
        ```
        #Importancion os
         
         import os
        
        #Importancion random
         
         import random
        
        ```

      
        
