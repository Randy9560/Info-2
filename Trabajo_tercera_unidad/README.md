# Trabajo Tercera Unidad
<p align="justify">
Bienvenid@, en este trabajo se encontrara un codigo en el que se procesa toda la informacion de estudios DICOM, asi mismo como su visualizacion con NILEARN.
La idea del README es proporcionarle al usuario una guia de como utilizar el codigo y explicar su funcionamiento.
</p>


## **Instrucciones**
<p align="justify">
La guia constara de 6 pasos para todo el procesamiento de informacion y visualizacion de imagenes.
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
En la carpeta del trabajo se encontraran tres achivos .zip los cuales se deben descargar y descomprimir para ser utilizados dentro del codigo, cabe resaltar que al momento de descomprimir los archivos .zip, se entregará un carpeta con el nombre del archivo .zip y dentro de esta carpeta habrá otra carpeta con el mismo nombre y ya dentro de esta si estaran todos los datos, se recomienda para el correcto funcionamiento del codigo, sacar la carpeta donde estan los datos de donde esta guardada y pegarla en el archivo de la carpeta donde se esta trabajando, dejando asi solo una carpeta con el nombre del archivo .zip y que dentro de esta ya esten directamente los datos. Los nombres de los archivos .zip que necesitan ser descomprimidos son:
 
1) **'0001'**
2) **'0002'**
3) **'0003'**
</p>

## **Paso 3 - Explicacion de metodos y atributos de la clase 'Estudio'**
<p align="justify">
Primero que todo, creamos una clase principal llamada 'Estudio',esta clase estara encargada de la anonimizacion de los datos, la visualizacion de las imagenes con NILEARN y la conversion de datos DICOM a NIFTI, esta clase sera la unica de la que al momento de hacer las pruebas se crearan objetos, siguiendo esta linea de pensamiento las otras clases que se van a crear seran solo para procesar los datos y para organizar las funcionalidades dentro del codigo. Dentro de esta clase se llaman a funciones de otras clases, como por ejemplo, Paciente.agregar_estudioPaciente y Paciente.añadirDatos_list que son relaciones de dependencia entre clases. 
 
 **_PD: Para trabajar en este codigo se recomienda usar el relative path donde sea posible_**

- Los atributos de clase que se piden en la clase **'Estudio'** son, la ruta de la carpeta en la que se encuentra el estudio (**'ruta_carpetaEstudio'**), o sea, los datos DICOM, el otro atributo que se pide es la ruta de la carpeta actual en la que se esta trabajando (**'path_carpetaTrabajo'**), esta sera necesaria para los metodos de mas adelante. Fuera de los atributos de clase que se piden, se crea otro atributo, (**'self._imgCarpeta'**) este atributo esta protegido, ya que me genera una lista por medio de la libreria **OS** la cual contiene el nombre de todos los archivos dentro de la carpeta del estudio, o sea, esta lista contiene todas las imagenes .dcm del estudio.

Ahora, se explicaran los metodos de la clase **'Estudio'** uno por uno:

- **_'Metodo verDiccionario()'_**: Este metodo como tal me llama a otro metodo de la clase **_'Paciente'_**, que lo que hace es como tal visualizarme el diccionario el cual es un atributo de clase que esta dentro de esta misma clase, el metodo que se llama en la clase **_'Estudio'_** que pertenece a la clase **_'Paciente'_** es **_'Paciente.mostrarDic()'_**, este metodo como tal no representa ningun punto pedido en el trabajo pero como tal es necesario para que se pueda observar el correcto funcionamiento de algunos metodos del codigo.

- **_'Metodo informacionEstudio'_**: Este metodo es muy parecido al anterior, es un metodo que llama a otro de la clase **_'SistemaGestion'_**, este metodo me muestra toda la informacion del estudio, o en particular de la imagen que va a ser visualizada con NILEARN, esta funcion se va a llamar en el **_'Metodo visualizarNilearn(ruta_ArchivoNifti) '_**, cada vez que se vaya a plotear una imagen, el nombre del metodo que es llamado desde la clase **_'SistemaGestion'_** se llama **_'SistemaGestion._manejoEstudios'_**, cabe recarlcar que el metodo anterior esta protegido, pero esta parte sera explicado en el apartado de este metodo en el apartado de la clase **_'SistemaGestion'_**.

- **_'Metodo _anonimizar'_**: Este metodo es protegido ya que no se desea que cualquiera pueda acceder a este metodo debido a que trabaja con la anonimizacion de los datos sensibles del pacientes, tales como, el Id, la fecha de nacimiento, el nombre y el genero del paciente. Este metodo en vez de cambiarme los datos en la carpeta original, crea otra carpeta dentro de la carpeta que se esta trabajando con todos los datos ya anonimizados, para esto era necesario el atributo de clase (**'path_carpetaTrabajo'**). Este metodo tiene varios atributos internos, pero son simples, los atributos son:

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
Lo primero que se debe explicar es el hecho de que la clase **_'Paciente'_** es heredada de la clase **_'Estudio'_**, o sea que **_'Paciente'_** es una clase hija de **_'Estudio'_**, se programo de esta manera ya que la clase **_'Paciente'_** necesita los mismos atributos de instancia que **_'Estudio'_**, lo segundo que se debe mencionar, es que la clase **_'Paciente'_** va estar encargada de tener un diccionario donde se van a almacenar los estudios separados por pacientes, esta parte va a ser filtrada por el id del paciente que traiga cada estudio, o sea que el diccionario va a tener una estrucutra Clave:valor, donde la clave sera el Id del paciente y el valor seran sus estudios. Todo esto lo va a hacer la clase **_'Paciente'_**

- Como se explico anteriormente la clase tiene como tal los mismos atributos de instancia de la clase **_'Estudio'_**, a diferencia de esta, la clase **_'Paciente'_** tiene un atributo de **_'Clase'_**, el cual es el diccionario donde se van a almacenar los pacientes con sus IDs y sus estudios(**_'estudiosPaciente'_**).

- **_'Metodo _obtencionID()'_**: Este metodo es protegigo ya que obtiene el Id del paciente del estudio, el metodo realiza un proceso muy sencillo, se crea un atributo interno llamado **_'Archivo'_** donde se descarga por el metodo **_'pydicom.dcmread()'_** y **_'os.path.join()'_** el contenido de un archivo .dcm del estudio, este proceso es el mismo que el de la clase anterior, luego al atrituto **_'Archivo'_** se le aplica un metodo respectivo de los archivos DICOM para obtner informacion del **_'Header'_** por medio de palabras claves, la palabra clave que se uso fue **_'archivo.PatientID'_**, eso con el fin de obtener el ID del paciente que esta en el estudio, ya por ultimo simplemente se retrona el atritubo **_'archivo'_** para ser usado en otro metodo dentro de la misma clase.

- **_'Metodo añadirDatos_list()'_**: Este metodo se podria considerar un metodo de asociacion o dependencia ya que es necesario para que la clase **_'SistemaGestion'_** pueda funcionar correctamente, ya que esta clase necesita tener acceso a los IDs registrado, de parte principal se tuvo la idea de llamar a al atributo de clase de la clase **_'Paciente'_** en la clase **_'SistemaGestion'_**, pero por mas procedimientos que realizaramos el codigo no queria funcionar, entonces se ideó este metodo que simplemente en un atributo interno(**_'iD1'_**) llama al metodo **_'_obtencionID()'_**, entonces en este atributo se guarda el iD del paciente que se obtuvo desde la carpeta del estudio, y ya para finalizar, simplemente por condicionales se agrega este ID a la lista que pertenece a la clase **_'SistemaGestion'_**, cabe resaltar que se usan los condicionales, para no volver a agregar IDs que ya esten dentro de la lista. 

- **_'Metodo agregar_estudioPaciente()'_**: Este metodo seria como la parte mas importante y sustancial de la clase **_'Paciente'_**, ya que realiza la funcion ams importante de esta clase, la cual es realizar la separacion y filtrado de los estudios dependiendo de sus ID.

  1) Lo primero que se hace es crear dos atributos internos los cuales son **_'iD' y 'llaves'_**, el primero va a llamar al metodo anteriomente creado **_'obtencionID()'_**, lo que va a producir que dentro de este atributo quede guardado el Id del paciente correspondiente al **_'Header'_** de los archivos DICOM del estudio y el segundo me va a crear una lista que contenga las llaves del diccionario **_'estudioPaciente'_**, que seran los IDs de los pacientes registrados, esto se hace mediante el metodo particular de los diccionarios **_'Paciente.estudiosPacientes.keys()'_**, cabe resaltar que se llama asi el atributo y no con **_'self.'_**, esto es debido a que el diccionario es un atributo de clase.
  2) Luego, se realiza un proceso de filtramiento de los datos por medio de condicionales como **_'if' y 'else'_**, lo que se pide es que si el iD obtenido esta dentro de la lista **_'llaves'_**, me cree primero que todo otro atributo llamado **_'comprobante'_**, que lo que va a tener guardado son los valores(En este caso los estudios de un paciente en especifico) que tenga guardado la clave(Que en este caso es el ID del paciente obtenido anteriormente) dentro del diccionario, entonces se crea otro condicional anillado donde se le pida comprobar que si dentro del atributo **_'comprobante'_** esta el path de la carpeta del estudio que se le asigno, cabe resaltar que este condicional esta hecho de esta manera, ya que se planteo guardar a los nuevos estudios mediante su path; Entonces, si el path del estudio que ingrese ya esta dentro del atributo **_'comprobante'_**, se le dice al codigo que no haga nada, sino que siga adelante, pero si el path no esta, se le pide al codigo que le agrege a ese mismo ID otro valor que en este caso sera este path, cabe resaltar que esta parte de condicionales del codigo se realizo, con el fin poder diferenciar estudios que sean de un paciente o de otro; Ahora por ultimo si el iD no esta dentro de la lista llaves se le pide al codigo que me agrege el iD y lo iguale a la ruta del archivo DICOM de este mismo, creando asi aun nuevo paciente con un nuevo estudio asignado.
 
- **_'Metodo mostrarDic()'_**: Este metodo simplemente me imprime la informacion del diccionario, ya que no puedo acceder a ella por fuera del codigo.   
