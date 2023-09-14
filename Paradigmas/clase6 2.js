/*const lista = [5,2,8,9,6,22,90,7,65,44]
const lista2 = [10,9,8,7,6,5,4,3,2,1]
function estaOrdenada(cual){

    return cual.every(i => cual[i==0?i:i-1] > cual[i])
}
console.log(estaOrdenada(lista))
console.log(estaOrdenada(lista2))
*/
const r1 = [55,20230901]
const r2 = [57,20230902]
const r3 = [59,20230903]
const r4 = [56,20230904]
const r5 = [47,20230905]

const r = [r1,r2,r3,r4,r5]

const consulta = r.filter(n => n[0]>55).map(l=>l[1])
//const diasdeconsulta = consulta.forEach(x => console.log(x[1]))
const formateo = consulta.forEach(x => console.log(x.toString().substring(0,4)+"-"+x.toString().substring(5,6)+"-"+x.toString().substring(7,8)))

const menor = Math.min(...r[0])
console.log(menor)
const sumaregistros = r.map(l => l[0]).reduce((a,b)=>a+b,0)
console.log(sumaregistros)