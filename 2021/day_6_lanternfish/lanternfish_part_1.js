const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(',').map(element => parseInt(element))
}

async function lanternfishAnalyzer(fileName) {
    let lanternfishes = await readFile(fileName)
    loop(80, () => {
        const counter = lanternfishes.filter((laternfish => laternfish == 0)).length
        lanternfishes = lanternfishes.map((laternfish) => laternfish != 0 ? laternfish - 1 : 6)
        lanternfishes = lanternfishes.concat(Array(counter).fill(8))
    })
    return lanternfishes.length
}

const loop = (times, callback) => [...Array(times)].forEach(callback)

const fileName = '2021/day_6_lanternfish/lanternfishes.txt'
lanternfishAnalyzer(fileName).then((result) => console.log(result))