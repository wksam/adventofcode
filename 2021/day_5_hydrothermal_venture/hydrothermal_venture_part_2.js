const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(/\r?\n/)
        .map(line => line.split(' -> ')
        .map(point => point.split(',')
        .map(element => parseInt(element))));
}

async function overlaps(fileName) {
    const coordinates = await readFile(fileName)
    const filteredCoordinates = coordinates.reduce((previousValue, currentValue) => {
        const x1 = currentValue[0][0], x2 = currentValue[1][0], y1 = currentValue[0][1], y2 = currentValue[1][1]
        if(x1 == x2 || y1 == y2 || Math.abs(x1 - x2) == Math.abs(y1 - y2)) previousValue.push(currentValue)
        return previousValue
    }, [])
    
    const xMaxSize = Math.max(...filteredCoordinates.map(line => line.map(point => point[0])).flat()) + 1
    const yMaxSize = Math.max(...filteredCoordinates.map(line => line.map(point => point[1])).flat()) + 1
    const diagram = Array(xMaxSize).fill(null).map(() => Array(yMaxSize).fill(0))
    
    for (const line of filteredCoordinates) {
        if(line[0][0] == line[1][0]) {
            for (let y = Math.min(line[0][1], line[1][1]); y <= Math.max(line[0][1], line[1][1]); y++)
                diagram[y][line[0][0]]++
        }
        else if(line[0][1] == line[1][1]) {
            for (let x = Math.min(line[0][0], line[1][0]); x <= Math.max(line[0][0], line[1][0]); x++)
                diagram[line[0][1]][x]++
        } else {
            line.sort((a, b) => a[0] - b[0])
            if(line[0][1] > line[1][1])
                for (let x = line[0][0], y = line[0][1]; x <= line[1][0]; x++, y--)
                    diagram[y][x]++
            else
                for (let x = line[0][0], y = line[0][1]; x <= line[1][0]; x++, y++)
                    diagram[y][x]++
        }
    }

    return diagram.reduce((previousValue, currentValue) => 
        previousValue += currentValue.reduce((previousValue, currentValue) => 
            currentValue > 1 ? previousValue += 1 : previousValue
        , 0)
    , 0)
}

const fileName = 'day_5_hydrothermal_venture/lines_of_vents.txt'
overlaps(fileName).then((result) => console.log(result))