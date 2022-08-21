# nova-state
&ensp;
Este proyecto lo realicé con mucho cariño y motivación.

&ensp;
&ensp;

## Pasos para correr la aplicación:

1 - Clonamos el repositorio a nuestra carpeta para el proyecto:

```git clone https://github.com/slitheryduke11/nova-state.git```

2 - Una vez en nuestro directorio, creamos el archivo **.env**, donde colocaremos los valores de las keys de EasyBroker y Django (*EASYBROKER_API_KEY* y *DJANGO_SECRET_KEY*), siendo esta última proporcionada por mí por correo.

3 - Después, creamos la carpeta que contendrá todas las librerías para el entorno local:

```python3 -m venv ./venv --prompt nova_state```

4 - Posteriormente, activamos el entorno virtual:

```source venv/bin/activate```

5 - Una vez trabajando en el entorno virtual, procedemos a instalar las dependencias:

```pip3 install -r requirements.txt```

6 - Debido a que la base de datos local utilizada no se incluye en el repositorio, es necesario aplicar una migración para poder trabajar con las variables de sesión utilizadas en el proyecto:

```python3 manage.py migrate```

7 - Finalmente, podemos correr la aplicación:

```python3 manage.py runserver```

&ensp;
&ensp;

## He aquí unos screenshots de la aplicación:
&ensp;

<kbd><img src="https://user-images.githubusercontent.com/55264175/185803323-b9cba500-92b0-47fd-aff0-efa79fb30dd8.png" /></kbd>
<p align="center">
Página principal (presentación)
</p>

&ensp;
-------------
&ensp;

<kbd><img src="https://user-images.githubusercontent.com/55264175/185803324-7de36d0c-50aa-4f74-b847-ee45939cfe43.png" /></kbd>
<p align="center">
Página principal (propiedades)
</p>

&ensp;
-------------
&ensp;

<kbd><img src="https://user-images.githubusercontent.com/55264175/185803325-a443c436-de00-45ae-b7bb-ec141c09d3fe.png" /></kbd>
<p align="center">
Página principal (paginación)
</p>

&ensp;
-------------
&ensp;

<kbd><img src="https://user-images.githubusercontent.com/55264175/185803327-901b8c31-2b1e-412d-8d76-231cb54d6d50.png" /></kbd>
<p align="center">
Página para la propiedad (presentación)
</p>

&ensp;
-------------
&ensp;

<kbd><img src="https://user-images.githubusercontent.com/55264175/185803328-e87d2d80-a8f6-460e-935e-85c54166096b.png" /></kbd>
<p align="center">
Página para la propiedad (inicio)
</p>

&ensp;
-------------
&ensp;

<kbd><img src="https://user-images.githubusercontent.com/55264175/185803329-f19a6698-46d2-4478-b337-8e50f1b6a606.png" /></kbd>
<p align="center">
Página para la propiedad (galería)
</p>

&ensp;
-------------
&ensp;

<kbd><img src="https://user-images.githubusercontent.com/55264175/185803330-ec53e22b-9684-4df2-b392-948949c0ed46.png" /></kbd>
<p align="center">
Página para la propiedad (formulario)
</p> 
 
&ensp;
&ensp;

## Notas:
 
 
&ensp;
&ensp;

Para la parte del Front-End quise mejorar un poco la presentación de los datos, donde un cambio que hice fue el de mostrar las propiedades en una serie de contenedores en lugar de una lista.
Opté por añadir links a la paginación para poder moverse entre las diferentes páginas de datos y también agregué toda la serie de imágenes por cada propiedad en su página correspondiente.

En cuanto al Back-End, reutilicé la clase de la API de EasyBroker del reto anterior, impementando ahora una clase abstracta y una subclase más especializada (siendo esta la de EasyBroker) con el fin de seguir buenas prácticas de POO.
Así mismo, organicé mi proyecto por aplicaciones, una para la página principal y otra para la página de las propiedades individuales, siendo así más sencillo y efectivo de realizar modificaciones al proyecto.

Ahora bien, me gustaría agregar unos comentarios:

- El proyecto utiliza recursos estáticos, por lo que al desactivar el modo **debug** es necesario definir el servidor que proporcionará dichos recursos. Es por ello que, si corren la aplicación en modo de producción, los estilos no se verán correctamente.

- La cantidad de funciones existentes son pocas, por lo que el total de pruebas también lo son.

- El sitio no solicita al usuario iniciar sesión, por lo que la dirección de **login** únicamente redirecciona a la página principal (esto debido a que se utilizan variables de sesión y estos se resetean cada hora).

- Con base en el punto anterior, debido a que cuando se utiliza una API y los datos solicitados de las propiedades son muchos, el tiempo de carga se prolonga. Por ello, se utilizaron variables de sesión, donde una vez obtenidos los datos, no se vuelve a llamar a la API hasta que finalice una hora y así la página solo tarda un poco al inicio. Esto solo para la obtención de todas las variables publicadas, no aplica para la obtención de propiedades individuales.

- La parte más difícil que tuve que realizar fue justamente un feature que no puede implementar (sad). Trataba de hacer que la sección de la paginación no hiciera un request por cada clic, sino que en su lugar modificara los elementos de dicha estructura desde el mismo lado del cliente.

- Por último, me gustaría mencionar que hubieron algunas características que habrían gustado implementar, y por falta de tiempo (me dejaron un proyecto pesado para este fin de semana) no pude terminar de agregarlas. Dichos features eran los siguientes:
  
  - Mensajes que indicaban cuando la creación del lead fue exitosa o no
  - Sección de contacto en la página principal
  - Manejo de situaciones donde los atributos de las propiedades estaban vacíos y poder personalizar la información presentada (ejemplo: imagen genérica para cuando no habían fotos de los inmuebles)
  - Imagen de presentación aleatoria cada vez que se cargaba la página principal
  - Añadir labels a los inputs del formulario
 

*Ojo, el hecho de que no haya implementado esas mejoras para la versión de entrega no significa que no las agregue después a la original :)*
 
 
Eso es todo.
 
¡Gracias por leerme y espero la aplicación sea de su agrado!
