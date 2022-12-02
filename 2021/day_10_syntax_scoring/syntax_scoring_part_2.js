const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(/\r?\n/)
}

async function autocomplete(fileName) {
    const navigation_subsystem = await readFile(fileName)
    let stack = []
    let score = []
    for (const line of navigation_subsystem) {
        let incomplete = true
        for (const symbol of line) {
            if(isOpening(symbol))
                stack.push(symbol)
            else {
                const lastOpenBracket = stack.pop()
                if(isClosing(lastOpenBracket, symbol))
                    continue
                incomplete = false
                break
            }
        }
        if(incomplete) {
            stack = stack.reverse()
            let sum = 0
            for (const symbol of stack) {
                sum = (sum * 5) + symbolScore(symbol)
            }
            score.push(sum)
        }
        incomplete = true
        stack = []
    }
    const sortedScore = score.sort((a, b) => a - b)
    return sortedScore[Math.floor(sortedScore.length / 2)]
}

const isOpening = (symbol) => ['(', '[', '{', '<'].includes(symbol)
const symbolScore = (symbol) => ['(', '[', '{', '<'].indexOf(symbol) + 1

function isClosing(previousSymbol, currentSymbol) {
    const open = ['(', '[', '{', '<']
    const closed = [')', ']', '}', '>']
    const index = open.indexOf(previousSymbol)
    return currentSymbol == closed[index]
}

const fileName = '2021/day_10_syntax_scoring/navigation_subsystem.txt'
autocomplete(fileName).then((result) => console.log(result))