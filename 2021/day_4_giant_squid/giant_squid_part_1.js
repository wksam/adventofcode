const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(/\r?\n/).reduce((previousValue, currentValue, currentIndex) => {
        if(currentIndex == 0)
            previousValue[0] = currentValue.split(',').map(toInt)
        else if(currentValue == '')
            previousValue[1].push([])
        else
            previousValue[1][previousValue[1].length - 1].push(currentValue.trim().split(/\s+/g).map(toInt))
        return previousValue
    }, [[],[]])
}

async function lifeSupportRating(fileName) {
    const [drawNumbers, setOfBoards] = await readFile(fileName)

    for (const lastDrawn of drawNumbers) {
        for (const board of setOfBoards) {
            let indexMark = -1
            for(const line of board) {
                indexMark = line.findIndex((element) => element == lastDrawn)
                if(indexMark != -1) {
                    line[indexMark] = -1
                    if(checkVertically(board, indexMark) || checkHorizontally(line))
                        return sumAllUnmarked(board) * lastDrawn
                }
            }
        }
    }
}

function checkVertically(board, indexMark) {
    for (const line of board)
        if(line[indexMark] != -1) return false
    return true
}

function checkHorizontally(line) {
    for (const element of line)
        if(element != -1) return false
    return true
}

function sumAllUnmarked(board) {
    return board.reduce((previousValue, currentValue) => 
        previousValue += currentValue.reduce((p, c) => p += c != -1 ? c : 0, 0), 0)
}

const toInt = (element) => parseInt(element)

const fileName = '2021/day_4_giant_squid/set_of_boards.txt'
lifeSupportRating(fileName).then((result) => console.log(result))