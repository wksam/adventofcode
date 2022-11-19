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
    let lastBoard;
    for (const lastDrawn of drawNumbers) {
        for (let boardIndex = setOfBoards.length - 1; boardIndex >= 0; boardIndex--) {
            let indexMark = -1
            for(const line of setOfBoards[boardIndex]) {
                indexMark = line.findIndex((element) => element == lastDrawn)
                if(indexMark != -1) {
                    line[indexMark] = -1
                    if(checkVertically(setOfBoards[boardIndex], indexMark) || checkHorizontally(line))
                        lastBoard = setOfBoards.splice(boardIndex, 1)
                    break
                }
            }
        }
        if(setOfBoards.length == 0) {
            return sumAllUnmarked(lastBoard.flat()) * lastDrawn
        }
    }
}

function checkVertically(board, indexMark) {
    for (const line of board)
        if(line[indexMark] != -1)
            return false
    return true
}

function checkHorizontally(line) {
    for (const element of line)
        if(element != -1)
            return false
    return true
}

function sumAllUnmarked(board) {
    return board.reduce((previousValue, currentValue) => 
        previousValue += currentValue.reduce((p, c) => p += c != -1 ? c : 0, 0), 0)
}

const toInt = (element) => parseInt(element)

const fileName = 'day_4_giant_squid/set_of_boards.txt'
lifeSupportRating(fileName).then((result) => console.log(result))