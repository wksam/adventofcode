const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(/\r?\n/).map((output) => output.split(' | ').map((digit) => digit.split(' ')))
}

async function find1478(fileName) {
    const notes = await readFile(fileName)
    
    let count = 0
    for (const [, digits] of notes) {
        for (const digit of digits) {
            switch(digit.length) {
                case 2:
                case 3:
                case 4:
                case 7:
                    count++
            }
        }
    }

    return count
}

const fileName = 'day_8_seven_segment_search/notes.txt'
find1478(fileName).then((result) => console.log(result))