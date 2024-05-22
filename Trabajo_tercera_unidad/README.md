# Trabajo Tercera Unidad
<p align="justify">
Bienvenid@, en este trabajo se encontrara un codigo en el que se procesa toda la informacion de estudios DICOM, asi mismo como su visualizacion con NILEARN.
La idea del README es proporcionarle al usuario una guia de como utilizar el codigo y explicar su funcionamiento.
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
</p>        

## **Paso 2 - Obtencion los datos necesarios para realizar la prueba**
<p align="justify">
En la carpeta del trabajo se encontraran tres achivos .zip los cuales se deben descargar y descomprimir para ser utilizados dentro del codigo. Los nombres de los archivos .zip que necesitan ser descomprimidos son:
 
1) **'0001'**
2) **'0002'**
3) **'0003'**
</p>

## **Paso 3 - Explicacion de metodos y atributos de la clase 'Estudio'**
<p align="justify">
Primero que todo, creamos una clase principal llamada 'Estudio',esta clase estara encargada de la anonimizacion de los datos, la visualizacion de las imagenes con NILEARN y la conversion de datos DICOM a NIFTI, esta clase sera la unica de la que al momento de hacer las pruebas se crearan objetos, siguiendo esta linea de pensamiento las otras clases que se van a crear seran solo para procesar los datos y para organizar las funcionalidades dentro del codigo.
 
 **_PD: Para trabajar en este codigo se recomienda usar el relative path donde sea posible_**

- Los atributos de clase que se piden en la clase **'Estudio'** son, la ruta de la carpeta en la que se encuentra el estudio (**'ruta_carpetaEstudio'**), o sea, los datos DICOM, el otro atributo que se pide es la ruta de la carpeta actual en la que se esta trabajando (**'path_carpetaTrabajo'**), esta sera necesaria para los metodos de mas adelante. Fuera de los atributos de clase que se piden, se crean otros dos, el primero es (**'self.imgCarpeta'**) este atributo me genera una lista por medio de la libreria **OS** la cual contiene el nombre de todos los archivos dentro de la carpeta del estudio, o sea, esta lista contiene todas las imagenes .dcm del estudio; Ya el segundo atributo de clase es (**'self.idEstudio'**) su finalidad es obtener el Id del paciente del estudio, para realizar lo anterior este atributo usa el metodo **dcmread** de la libreria **pydicom** para leer un archivo de los que se encuentran en el atributo (**'self.imgCarpeta'**), para poder hacer esto se utiliza el metodo **'os.path.join'** que lo que hace es unir dos path, por esa razon se le pone como argumentos la ruta de la carpeta donde esta el estudio y el nombre del archivo que deseo leer, en este caso tomo el primer archivo(cabe aclarar que se puede tomar cualquier archivo de la lista de un mimso estudio, ya que todos tiene el mismo 'Header'), luego el metodo **'os.path.join'** me une las dos rutas y me crea el path completo del archvio que deseo leer, este paso es necesario ya que el metodo **'pydicom.dcmread'** pide como argumento la ruta completa del archivo que se desea leer, ya como ultimo paso, se usa el metodo **'.StudyID'** que es propia de los archivos DICOM, con esta 'Palabra clave' se busca el Id del archivo.

Ahora, se explicaran los metodos de la clase **'Estudio'** uno por uno:

- **_'Metodo anonimizar'_**: Este metodo tiene como objetivo la anonimizacion de los datos sensibles del pacientes, tales como, el Id, la fecha de nacimiento, el nombre y el genero del paciente. Este metodo en vez de cambiarme los datos en la carpeta original, crea otra carpte dentro de la carpeta que se esta trabajando con todos los datos ya anonimizados, para esto era necesario el atributo de clase (**'path_carpetaTrabajo'**). Este metodo tiene varios atributos internos, pero son simples, los atributos son:

     1) **_'nombreEstudio_anonimus'_**: Pide el nombre o el codigo por el que se va a reconocer la nueva carpeta anonimizada.
     2) **_'lista_nombreCarpeta1'_**: Me crea una lista con los nombres de los archivos que estan dentro de la carpeta que estoy trabajando. 
     3) **_'nuevaCarpeta_anonimus'_**: Se usa de nuevo el metodo **'os.path.join'** para juntar el path de la carpeta en la que se esta trabajando y el nombre que se le puso en la variable **_'nombreEstudio_anonimus'_** para asi generar un nuevo path.
     4) **_'ruta_nuevaCarpeta_anonimus'_**: Este atributo usa el metodo **_'os.path.abspath'_**, me entrega la ruta completa de la carpeta que le ponga como argumento, en este caso el argumento es el nombre de la carpeta que estoy creando.

  Luego, se hace estructura de condicionales para la creacion de la carpeta en la que se van a guardar los nuevos datos anonimizados, este proceso se realiza para evitar que salga un error, dado que se usa el metodo **_'os.mkdir(**'nuevaCarpeta_anonimus'**)'_**, el cual tiene como  argumento el atributo **_'nuevaCarpeta_anonimus'_**, esto me va a crear una nueva carpeta en la carpeta en la que estoy trabajando, el error que puede salir es que si se intenta crear una carpeta con el mismo nombre de una carpeta que ya exista saldra un error. Despues, de que la carpeta sea creada pasamos como tal a la parte de anonimizacion de los datos en la que usamos la libreria **_'random'_** y se usa en especifico el metodo **_'random.randint()'_** que lo que hace es que me genera un numero random dentro del rango de valores que se pasen como argumentos, ya para esta parte es muy sencillo, se crean tres nuevos atributos:

  1) **_'id', 'name', 'sex'_**: Los 3 atributos tiene una codificacion con letras y entre estas un numero random en un rango de 1 a 4560, luego etos valores seran usados para cambiar los valores que traen los archivos .dcm para asi completar su anonimizacion

Para la anonimizacion de hace un for en un rango del valor de las archivos totales que hayan dentro del estudio, luego dentro del for se descarga cada archivo y para cambiar sus valores lo tratamos como un diccionario, se crea un nuevo atributo **_'archivo'_** donde se descargan los archivos DICOM y se realizan los cambios de la siguiente manera **_'archivo['palabra clave del valor que se desea cambiar'] = 'Nuevo valor'_** y aqui el valor nuevo seran los atributos anteriormente creados que contienen un codigo junto a un numero random, cabe resaltar que para la fecha de nacimiento se reemplazara por un valor nulo en todos los casos, ya por ultimo, se guardan los archivos con el metodo **_'archivo.save_as('ruta donde se desea guardar')'_**, en este caso el argumento es la ruta de la carpeta del estudio unida con el nombre del archivo .dcm por medio del metodo **_'os.path.join()'_**

- **_'Metodo convertirEstudio()'_**: En este metodo vamos a usar la libreria (**_'dicom2nifti'_**), este metodo es necesario para convertir los archivos DICOM a formato NIFTI, este proceso se realiza ya que es beneficioso por varias razones, como, que al convertir los archivos a NIFTI el peso de los datos se reduce en gran magnitud, ya que los datos DICOM, tienen que estar en una carpeta y son demasiados archivos por carpeta, por otro lado, al convertirlos a NIFTI es un solo archivo por estudio, cabe resaltar que en en la carpeta del estudio todos los archivos .dcm deben pertenecer a un solo estudio, si hay varios estudios en una sola carpeta, nos saldra un error, y por ultimo el beneficio mas importante es que al pasar los datos a formato NIFTI podemos usar la libreria **_'Nilearn'_** para visualizar las imagenes de una forma mas estructurada.

  1) El primer paso de este metodo es basicamente el mismo del metodo anterior donde se pide un nombre para una nueva carpeta, se validá que no haya ninguna carpeta con el mismo nombre en la carpeta general donde se esta trabajando, si todo sale bien, se procede a crear la carpeta donde se va a guardar el nuevo archivo en formato NIFTI, este paso es necesario ya que el metodo qye se va a utilizar (**_'dicom2nifti.convert_directory'_**), necesita la ruta de la carpeta donde se va a guardar el archivo convertido a NIFTI y la carperta donde estan los datos tipo DICOM que van a ser convertidos.
  2)  Ya como ultimo paso llamamos al metodo (**_'dicom2nifti.convert_directory(argumento1,argumento2)'_**) y como argumento1 le proporcionamos la ruta de la carpeta con los datos DICOM y como argumento2 le proporcionamos la ruta de la carpeta anteriormente creado donde se va a guardar el archivo NIFTI ya procesado.

Cabe recalcar que se usa un try - except en el metodo (**_'dicom2nifti.convert_directory'_**) para evitar errores desconocidos.

- **_'Metodo visualizarNilearn(ruta_ArchivoNifti)'_**: En este metodo se utiliza la libreria **_'Nilearn'_** y sus metodos, se pide un atributo de instancia que es la ruta del archivo NIFTI que se desea visualizar, se nos pide mostrar el estudio de tres formas:

  1) Un solo plano [Axial(Eje z), Coronal(Eje y), Sagital(Eje x)]
  2) Los tres planos
  3) Mosaico
  
Se usan los metodos **_'nilearn.image.load_img(ruta_ArchivoNifti)'_** este metodo me procesa el archivo Nifti y me obtiene toda la informacion necesaria para graficar, el otro metodo que se usa es **_'plotting.plot_anat(imagen,display_mode = 'Plano o forma en la que se desea visualizar la imagen', title = 'Titulo que se le quiera poner a la grafica')'_** este metodo me plotea la imagen antriormente procesada, me permite cambiar la forma de visualizacion y ponerle titulos a las imagenes.

1) El metodo tiene dos menus, uno principal y otro secundario, el menu principal le permite simplemente al usuario elegir que tipo de vista desea observar, ya el usuario selecciona una opcion y por medio de condicionales anillados y estructurados, llega a la opcion deseada, especificamente si el usuario ingresa la opcion numero 1, el codido entra a lo que seria el menu secundario, ya que es necesario que el usuario determine cual de los tres planos desea observar, luego de nuevo por condicionales anillados y estrucutrados se lleva a la parte de mostrar la imagen por medio del metodo **_'plotting.plot_anat()'_** (Metodo explicado anteriormente), este metodo es usado en todos lo casos de los dos menus para mostrar la imagen.
2) En cada menu que se hace, se agrega un **_'Try - Except'_** para evitar que el codigo se caiga si ingreso un valor tipo str, o se usa la funcion **_'raise'_** para llamar a acolacion otro error que seria si el usuario ingresa un valor que no se encuentra dentro de las opciones del menu.
3) Cabe recalcar que todo este proceso de los menus no se hicieron dentro de un **_'while True'_** ya que al momento de graficar la imagen pedida no aparece hasta que el ciclo se cierre.  
</p>  

## **Paso 4 - Explicacion de metodos y atributos de la clase 'Paciente'**
Lo primero que se debe explicar es el hecho de que la clase **_'Paciente'_** es heredada de la clase **_'Estudio'_**, o sea que **_'Paciente'_** es una clase hija de **_'Estudio'_**, se programo de esta manera ya que la clase **_'Paciente'_** necesita los mismos atributos de instancia que **_'Estudio'_**, lo segundo que se debe mencionar, es que la clase **_'Paciente'_** va estar encargada de tener un diccionario donde se van a almacenar los estudios separados por pacientes, esta parte va a ser filtrada por el id del paciente que traiga cada estudio. Todo esto lo va a hacer la clase **_'Paciente'_**

- 
