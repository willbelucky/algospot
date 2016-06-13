var input = [];
require('readline')
.createInterface(process.stdin, {})
.on('line', function(line) {
  input.push(line.trim());
}).on('close', function() {
  for (var i = 1; i <= +input[0]; i++)
    console.log('Hello, ' + input[i] + '!');
});