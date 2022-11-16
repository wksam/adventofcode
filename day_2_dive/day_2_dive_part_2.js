const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(/\r?\n/)
        .map((element) => element.split(' '))
        .map((element) => [element[0], parseInt(element[1])])
}

async function controlSubmarine(fileName) {
    const commands = await readFile(fileName)
    const [position, depth,] = commands.reduce((previousValue, currentValue) => {
        switch (currentValue[0]) {
            case 'down':
                previousValue[2] += currentValue[1]
                break
            case 'up':
                previousValue[2] -= currentValue[1]
                break
            default:
                previousValue[0] += currentValue[1]
                previousValue[1] += currentValue[1] * previousValue[2]
                break
        }
        return previousValue
    }, [0, 0, 0])
    return position * depth
}

const fileName = 'day_2_dive/planned_course.txt'
controlSubmarine(fileName).then((result) => console.log(result))