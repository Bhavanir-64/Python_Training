//array = [1, 2, "ram", 22.4];
//console.log(array);

//for (let i of array) {
//console.log(i);
//}

//a = 10;
//b = "10";
//console.log(a == b);
//console.log(a === b);

//let str = "";
//for (let i = 1; i < 6; i++) str += i + " ";
//console.log(str);

array = [1, 2, 9, 6, 7];
console.log(array);
array.push(10);
console.log(array);
array.pop();
console.log(array);
array[1] = 5;
console.log(array);
console.log(array.length);
let str = "";
for (let i in array) str += i + " ";
console.log(str);
let st = "";
for (let i of array) st += i + " ";
console.log(st);
array = [1, 2, 9, 6, 7];
array.unshift(8);
console.log(array);
array.shift(2);
console.log(array.includes(6));
console.log(array.indexOf(6));
console.log(array.slice(0, 3));
array.splice(1, 2);
console.log(array);