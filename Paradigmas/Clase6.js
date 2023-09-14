/*un kilo de milanesas rebozadas: 2600 pesos.*/
const kiloMilas = {
    consPrecio(){
        return 2600
    }
}
//una botella de salsa de tomates: 900 pesos.
const botTomate = {
    consPrecio(){
        return 900
    }
}
//un microondas: 42000 pesos.
const microondas = {
    consPrecio(){
        return 42000
    }
}
//un kilo de cebollas: 250 pesos.
//una compu: 500 dólares. Para saber el precio en pesos, multiplicar por la cotización del dólar. 
//Agregar un objeto dolar al que se le pueda preguntar el precioDeVenta(), alcanza con que devuelva un valor fijo.
//un "pack comida" que incluye un plato (que puede ser tira de asado, fideos o milanesas) y un aderezo 
//(que puede ser la botella de salsa de tomates o el kilo de cebollas. Precio: la suma del precio de sus componentes.