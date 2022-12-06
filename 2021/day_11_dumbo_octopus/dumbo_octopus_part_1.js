const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(/\r?\n/).map((line) => [...line].map((a) => parseInt(a)))
}

async function flashCounter(fileName) {
    const octopuses = await readFile(fileName)

    let flashes = 0
    for(let step = 0; step < 100; step++) {
        let overloaded = addEnergy(octopuses)
        flashes = addFlashes(overloaded, octopuses, flashes)
    }

    return flashes
}

function addEnergy(octopuses) {
    let overloaded = []
    for (let y = 0; y < octopuses.length; y++) {
        for (let x = 0; x < octopuses[y].length; x++) {
            octopuses[y][x]++
            if (octopuses[y][x] > 9) {
                octopuses[y][x] = 0
                overloaded.push([y, x])
            }
        }
    }
    return overloaded
}

function addFlashes(overloaded, octopuses, flashes) {
    for (const position of overloaded)
        flashes = addAdjacentEnergy(position, octopuses, ++flashes)
    return flashes
}

function addAdjacentEnergy(position, octopuses, flashes) {
    const [y, x] = position
    if (x - 1 >= 0) {
        // West
        if (octopuses[y][x - 1] > 0) 
            flashes = increaseEnergy([y, x - 1], octopuses, flashes)
        // Northwest
        if (y - 1 >= 0 && octopuses[y - 1][x - 1] > 0) 
            flashes = increaseEnergy([y - 1, x - 1], octopuses, flashes)
    }
    if (y - 1 >= 0) {
        // North
        if (octopuses[y - 1][x] > 0) 
            flashes = increaseEnergy([y - 1, x], octopuses, flashes)
        // Northeast
        if (x + 1 < octopuses[y].length && octopuses[y - 1][x + 1] > 0) 
            flashes = increaseEnergy([y - 1, x + 1], octopuses, flashes)
    }
    if (x + 1 < octopuses[y].length) {
        // East
        if (octopuses[y][x + 1] > 0) 
            flashes = increaseEnergy([y, x + 1], octopuses, flashes)
        // Southeast
        if (y + 1 < octopuses.length && octopuses[y + 1][x + 1] > 0)
            flashes = increaseEnergy([y + 1, x + 1], octopuses, flashes)
    }
    if (y + 1 < octopuses.length) {
        // South
        if (octopuses[y + 1][x] > 0) 
            flashes = increaseEnergy([y + 1, x], octopuses, flashes)
        // Southwest
        if (x - 1 > -1 && octopuses[y + 1][x - 1] > 0)
            flashes = increaseEnergy([y + 1, x - 1], octopuses, flashes)
    }
    return flashes
}

function increaseEnergy(position, octopuses, flashes) {
    const [y, x] = position
    octopuses[y][x]++
    if (octopuses[y][x] > 9) {
        octopuses[y][x] = 0
        flashes = addAdjacentEnergy(position, octopuses, ++flashes)
    }
    return flashes
}

const fileName = '2021/day_11_dumbo_octopus/octopuses.txt'
flashCounter(fileName).then((result) => console.log(result))