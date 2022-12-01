const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(',').map(element => parseInt(element)).sort((a, b) => a - b)
}

async function leastFuelPossible(fileName) {
    const crabsPosition = await readFile(fileName)
    const median = crabsPosition[Math.floor((crabsPosition.length - 1) / 2)]
    return crabsPosition.reduce((previousValue, currentValue) => previousValue + Math.abs(currentValue - median), 0)
}

const fileName = '2021/day_7_the_treachery_of_whales/crabs_position.txt'
leastFuelPossible(fileName).then((result) => console.log(result))