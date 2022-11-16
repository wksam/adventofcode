const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split('\n').map((value) => parseInt(value))
}

async function sonarSweep(inputPath) {
    const inputs = await readFile(inputPath)

    const [,count] = inputs.slice(1).reduce((previousValue, currentValue) => 
        [currentValue, currentValue > previousValue[0] ? previousValue[1] + 1 : previousValue[1]], [inputs[0], 0])

    return count
}

const path = 'day_1_sonar_sweep/sweep_report.txt'
sonarSweep(path).then((result) => console.log(result))