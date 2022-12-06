const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(/\r?\n/).map((line) => [...line].map((a) => parseInt(a)))
}

async function flashCounter(fileName) {
    const octopuses = await readFile(fileName)

    let steps = 0
    while (true) {
        steps++
        let overloaded = addEnergy(octopuses)
        addFlashes(overloaded, octopuses)
        if(isAllFlash(octopuses))
            break
    }

    return steps
}

function isAllFlash(octopuses) {
    for (let y = 0; y < octopuses.length; y++) {
        for (let x = 0; x < octopuses[y].length; x++) {
            if(octopuses[y][x] != 0)
                return false
        }
    }
    return true
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

function addFlashes(overloaded, octopuses) {
    for (const position of overloaded)
        addAdjacentEnergy(position, octopuses)
}

function addAdjacentEnergy(position, octopuses) {
    const [y, x] = position
    if (x - 1 >= 0) {
        // West
        if (octopuses[y][x - 1] > 0) 
            increaseEnergy([y, x - 1], octopuses)
        // Northwest
        if (y - 1 >= 0 && octopuses[y - 1][x - 1] > 0) 
            increaseEnergy([y - 1, x - 1], octopuses)
    }
    if (y - 1 >= 0) {
        // North
        if (octopuses[y - 1][x] > 0) 
            increaseEnergy([y - 1, x], octopuses)
        // Northeast
        if (x + 1 < octopuses[y].length && octopuses[y - 1][x + 1] > 0) 
            increaseEnergy([y - 1, x + 1], octopuses)
    }
    if (x + 1 < octopuses[y].length) {
        // East
        if (octopuses[y][x + 1] > 0) 
            increaseEnergy([y, x + 1], octopuses)
        // Southeast
        if (y + 1 < octopuses.length && octopuses[y + 1][x + 1] > 0)
            increaseEnergy([y + 1, x + 1], octopuses)
    }
    if (y + 1 < octopuses.length) {
        // South
        if (octopuses[y + 1][x] > 0) 
            increaseEnergy([y + 1, x], octopuses)
        // Southwest
        if (x - 1 > -1 && octopuses[y + 1][x - 1] > 0)
            increaseEnergy([y + 1, x - 1], octopuses)
    }
}

function increaseEnergy(position, octopuses) {
    const [y, x] = position
    octopuses[y][x]++
    if (octopuses[y][x] > 9) {
        octopuses[y][x] = 0
        flashes = addAdjacentEnergy(position, octopuses)
    }
}

const fileName = '2021/day_11_dumbo_octopus/octopuses.txt'
flashCounter(fileName).then((result) => console.log(result))