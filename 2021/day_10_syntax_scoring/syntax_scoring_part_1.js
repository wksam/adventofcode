const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(/\r?\n/)
}

async function firstIllegalCharacter(fileName) {
    const navigation_subsystem = await readFile(fileName)
    let stack = []
    let score = 0
    for (const line of navigation_subsystem) {
        for (const symbol of line) {
            const numSymbol = convert(symbol)
            if(numSymbol < 0)
                stack.push(numSymbol)
            else {
                const lastOpenBracket = stack.pop()
                if(lastOpenBracket + numSymbol == 0)
                    continue
                score += numSymbol
                break
            }
        }
        stack = []
    }
    return score
}

function convert(symbol) {
    switch (symbol) {
        case '(': return -3
        case ')': return 3
        case '[': return -57
        case ']': return 57
        case '{': return -1197
        case '}': return 1197
        case '<': return -25137
        case '>': return 25137
    }
}

const fileName = '2021/day_10_syntax_scoring/navigation_subsystem.txt'
firstIllegalCharacter(fileName).then((result) => console.log(result))