const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(',').map(element => parseInt(element))
}

async function lanternfishAnalyzer(fileName) {
    const lanternfishes = await readFile(fileName)
    let report = Array(9).fill(0)
    for (const age of lanternfishes)
        report[age]++
    
    loop(256, () => {
        const counter = report[0]
        const laternfish = report.shift()
        report[6] += laternfish
        report[8] = counter
    })

    return report.reduce((accumulator, currentValue) => accumulator += currentValue, 0)
}

const loop = (times, callback) => [...Array(times)].forEach(callback)

const fileName = 'day_6_lanternfish/lanternfishes.txt'
lanternfishAnalyzer(fileName).then((result) => console.log(result))