const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split('\n').map((value) => parseInt(value))
}

async function sumMeasurementSlidingWindow(inputPath, windowSize) {
    const inputs = await readFile(inputPath)

    let previousWindow = inputs.slice(0, windowSize).reduce((previousValue, currentValue) => previousValue += currentValue)

    let counter = 0
    let currentWindow = previousWindow
    for (let i = windowSize; i < inputs.length; i++) {
        currentWindow += inputs[i] - inputs[i - windowSize]
        if(currentWindow > previousWindow) counter++
        previousWindow = currentWindow
    }
    return counter
}

const path = 'day_1_sonar_sweep/input.txt'
sumMeasurementSlidingWindow(path, 3).then((result) => console.log(result))