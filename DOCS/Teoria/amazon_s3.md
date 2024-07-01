# <p align="center">AMAZON S3 </p>

## ¿Qué es s3?

Es un servicio de almacenamiento de objetos que son altamente escalables, duraderos y seguros que son proporcionados por AWS. Son esenciales para poder almacenar y recuperar cualquier cantidad de datos desde cualquier lugar de la web, esto puede ser usado para una gran variedad de casos como pueden ser copias de seguridad, restauración, archivado, aplicaciones empresariales y móviles y grandes conjuntos de datos.

## ¿Cómo almacenar datos en AWS S3?
Primero se crea un bucket con su respectivo nombre, esto viene a ser el contenedor principal de Amazon S3 que es usado para almacenar los objetos , por lo cual el nombre debe de ser único a nivel global, puede contener minúsculas, números, puntos (.) y guiones(-). Luego identificamos la región más cercana al usuario donde se podrá ubicar el bucket  y de esa manera poder minimizar la latencia. Una vez que ya hemos creado el bucket, subimos los objetos como archivos, vídeos, documentos, backups, etc, donde estos se dividen en datos y metadatos. Asimismo, cada objeto tiene una clave única (nombre de clave) que actúa como su identificador dentro del bucket. Esta clave puede incluir prefijos que simulan una estructura de carpetas.

### Ejemplo de almacenamiento:
Para acceder a los objetos de S3 se lo puede hacer mediante la URLs públicas si los permisos lo permiten o mediante credenciales de acceso para de esa manera poder mantener la seguridad. Por ejemplo, si se tiene una imagen llamada ‘phonto/puppy.jpg’ se almacena en un bucket DOC-EXAMPLE-BUCKET en ra región Oeste de EE.UU(Oregón) se puede dirigir con la URL https://DOC-EXAMPLE-BUCKET.s3.us-west-2.amazonaws.com/photo/pyppy.jpg, pero recuerde que una vez creado el bucket no se podrá cambiar ni el nombre ni la región 

## Seguridad:
Amazon S3 cuenta con diversas opciones para gestionar la seguridad y el acceso a los datos. Puedes utilizar políticas de bucket para definir permisos a nivel de bucket, o listas de control de acceso (ACLs) para definir permisos a nivel de objeto. Además, S3 proporciona varias opciones de cifrado para proteger los datos en reposo, incluyendo el cifrado del lado del servidor con claves gestionadas por S3 (SSE-S3), con claves gestionadas por AWS KMS (SSE-KMS), o con claves proporcionadas por el cliente (SSE-C).

## Recuperación de datos:
Para gestionar mejor los datos a largo plazo, Amazon S3 también ofrece opciones como el versionado y las reglas de ciclo de vida. Habilitar el versionado permite mantener múltiples versiones de un objeto, lo cual es útil para la recuperación en caso de eliminaciones accidentales o cambios no deseados. Las reglas de ciclo de vida permiten definir políticas para la migración automática de objetos entre diferentes clases de almacenamiento (por ejemplo, desde S3 Standard a S3 Glacier) o para la eliminación de objetos después de un período determinado.
En resumen, Amazon S3 se destaca por sus ventajas en escalabilidad, alta disponibilidad y durabilidad de datos, seguridad robusta y fácil integración con otros servicios de AWS y aplicaciones de terceros. Ofrece un modelo de costos basado en el uso, sin costos iniciales, y permite elegir entre diferentes clases de almacenamiento según las necesidades específicas de acceso y costos. Estos beneficios hacen de S3 una opción atractiva y poderosa para almacenar y gestionar datos en la nube.
