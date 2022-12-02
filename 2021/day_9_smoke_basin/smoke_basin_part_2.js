const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(/\r?\n/).map((line) => line.split('').map((digit) => parseInt(digit)))
}

async function calculateBasinsSize(fileName) {
    const heightmap = await readFile(fileName)

    let basins = []
    for (let y = 0; y < heightmap.length; y++) {
        for (let x = 0; x < heightmap[y].length; x++) {
            if(isLowPoint(heightmap, x, y))
                basins.push(basinSize(heightmap, x, y))
        }
    }
    return basins.sort((a, b) => a - b)
        .slice(basins.length - 3, basins.length)
        .reduce((previousValue, currentValue) => previousValue *= currentValue, 1)
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

function basinSize(map, x, y) {
    let open = [[y, x]]
    let closed = []
    while(open.length > 0) {
        let position = open.shift()
        if(!coordinateExists(closed, position) && getValue(map, position) < 9) {
            closed.push(position)
            if(position[1] - 1 >= 0)
                open.push([position[0], position[1] - 1])
            if(position[1] + 1 < map[position[0]].length)
                open.push([position[0], position[1] + 1])
            if(position[0] - 1 >= 0)
                open.push([position[0] - 1, position[1]])
            if(position[0] + 1 < map.length)
                open.push([position[0] + 1, position[1]])
        }
    }
    return closed.length
}

const getValue = (map, position) => map[position[0]][position[1]]
const coordinateExists = (coordinates, position) => coordinates.some((coordinate) => coordinate.every((value, index) => value == position[index]))

const fileName = '2021/day_9_smoke_basin/heightmap.txt'
calculateBasinsSize(fileName).then((result) => console.log(result))