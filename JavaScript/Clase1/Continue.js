for( let contando = 0; contando <=  10; contando++){
    if (contando % 2 !== 0){
        continue;//Ir a la siguiente iteración
    }
    console.log(contando);
}
console.log("Termina el ciclo");