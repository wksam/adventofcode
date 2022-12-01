const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(/\r?\n/).map((line) => line.split('').map((digit) => parseInt(digit)))
}

async function calculateRiskLevel(fileName) {
    const heightmap = await readFile(fileName)

    let riskLevel = 0
    for (let y = 0; y < heightmap.length; y++) {
        for (let x = 0; x < heightmap[y].length; x++) {
            if(isLowPoint(heightmap, x, y))
                riskLevel += heightmap[y][x] + 1
        }
    }

    return riskLevel
}

function isLowPoint(map, x, y) {
    if(x - 1 >= 0 && map[y][x] >= map[y][x - 1])
        return false
    if(x + 1 < map[y].length && map[y][x] >= map[y][x + 1])
        return false
    if(y - 1 >= 0 && map[y][x] >= map[y - 1][x])
        return false
    if(y + 1 < map.length && map[y][x] >= map[y + 1][x])
        return false
    return true
}

const fileName = 'day_9_smoke_basin/heightmap.txt'
calculateRiskLevel(fileName).then((result) => console.log(result))