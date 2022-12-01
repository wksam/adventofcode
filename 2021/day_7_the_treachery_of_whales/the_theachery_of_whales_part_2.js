const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(',').map(element => parseInt(element)).sort((a, b) => a - b)
}

async function leastFuelPossible(fileName) {
    const crabsPosition = await readFile(fileName)
    let minFuel = Infinity
    let maxPosition = crabsPosition[crabsPosition.length - 1]
    let minPosition = crabsPosition[0]

    for (let position = minPosition; position < maxPosition; position++) {
        let fuel = 0
        for (const crabPosition of crabsPosition) {
            let n = Math.abs(crabPosition - position)
            let cost = Math.floor(n * (n + 1) / 2)
            fuel += cost
        }
        minFuel = Math.min(minFuel, fuel)
    }
    
    return minFuel
}

const fileName = '2021/day_7_the_treachery_of_whales/crabs_position.txt'
leastFuelPossible(fileName).then((result) => console.log(result))