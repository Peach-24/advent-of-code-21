const fs = require('fs')
fs.readFile('real_input.txt', 'utf-8', (err, data) => {
    if (err) throw err;
    let dataArray = data.split("\n")
    let numbers = dataArray.map((str) => parseInt(str))
    let increased = 0;

    for (let i = 0; i < numbers.length; i++) {

        let firstWindowSum = numbers[i] + numbers[i+1] + numbers[i+2];
        let secondWindowSum = numbers[i+1] + numbers[i+2] + numbers[i+3];
        
        if(Number.isInteger(secondWindowSum) && Number.isInteger(firstWindowSum)) {
            if (secondWindowSum > firstWindowSum) {
                    increased += 1;
            } 
        } 
    }

    console.log(increased);
});