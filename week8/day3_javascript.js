console.log('Getting Started with JavaScript');

console.log('--------------------------------');

var myNumber = 13.8/90.34;
console.log(myNumber);

console.log('--------------------------------');

var myArray = [10, 'Robbie', [10, 93, 22], 'Atticus'];
console.log(myArray);
console.log(myArray[2][1]);

console.log('--------------------------------');

// for item in array: //(Python way)

for (var i = 0; i < myArray.length; i++) {
  var item = myArray[i];
  console.log(item);
}

console.log('--------------------------------');

// //Object Literals --> Dictionary in Python

var myObject = {
  'myName': 'Robbie',
  'myAge': 23,
};

console.log(myObject['myName'])

console.log('--------------------------------');

var myFunc = function(x, y){
  return x * y;
};

console.log(myFunc(9, 4));

console.log('--------------------------------');

var sillyArray = [9, 10, 2334, 65, 7];

var loopFunc = function(item) {
  console.log(item);
};

sillyArray.forEach(loopFunc);

console.log('--(see more of below in the field)--');

sillyArray.forEach(function(item){
  console.log(item);
});

console.log('--------------------------------');
