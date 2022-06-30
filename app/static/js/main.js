/*

1) La propiedad de ventana de solo lectura pageYOffset es un alias para scrollY;
como tal, devuelve el número de píxeles que el documento se desplaza actualmente
a lo largo del eje vertical (es decir, hacia arriba o hacia abajo) con un valor
de 0.0, lo que indica que el borde superior del documento está actualmente alineado
con el borde superior de la ventana.

2) let te permite declarar variables limitando su alcance (scope) al bloque,
declaración, o expresión donde se está usando. Lo anterior diferencia let de la
palabra reservada var , la cual define una variable global o local en una función
sin importar el ámbito del bloque.

Si no scrollo, ubicacionPrincipal >= desplazamientoActual >  -> se ve el nav(0px)
Cuando scrolle, c -> se esconde el nav(-100px)

3) AOS.init(); --> inicializa la clase AOS(Animate On Scroll). Anima la aparición
de los elementos de un listado: noticias, productos, contactos,etc.

Para que AOS funcione, agregar al html la siguiente libreria:
<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">

La segunda iamgen se achica(zoom-out) hacia(up) arriba en 2 segundos(data-aos-duration="2000")
<img src="img/segundaIlustracion.svg" alt="" data-aos="zoom-out-up" data-aos-duration="2000">

Los articulos se agrandan(zoom-in) en forma inmediata(sin transiciones)
<div class="articulo" data-aos="zoom-in-right">

*/

let ubicacionPrincipal = window.pageYOffset; //0(sin desplazamiento)

  AOS.init();


window.addEventListener("scroll", function(){
    let desplazamientoActual = window.pageYOffset;
    if(ubicacionPrincipal >= desplazamientoActual){
        document.getElementsByTagName("nav")[0].style.top = "0px"
    }else{
        document.getElementsByTagName("nav")[0].style.top = "-100px"
    }
    ubicacionPrincipal= desplazamientoActual; //200

})
