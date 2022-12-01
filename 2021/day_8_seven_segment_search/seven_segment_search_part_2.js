const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(/\r?\n/).map((output) => output.split(' | ').map((digit) => digit.split(' ')))
}

async function decodeOutputValues(fileName) {
    const notes = await readFile(fileName)

    let sum = 0
    for (const note of notes) {
        const signalPattern = decodeSignalPattern(note.shift().map(alphabeticalOrder))
        const fourDigits = note.shift().map(alphabeticalOrder)
        sum += parseInt(fourDigits.reduce((previousValue, currentValue) => previousValue.concat(signalPattern.indexOf(currentValue)), ''))
    }
    return sum
}

function decodeSignalPattern(numbers) {
    const decoded = Array(10)

    const orderedByLength = numbers.sort((a, b) => a.length - b.length)
    decoded[1] = orderedByLength.shift()
    decoded[7] = orderedByLength.shift()
    decoded[4] = orderedByLength.shift()
    decoded[8] = orderedByLength.pop()

    const sizeOfFive = orderedByLength.splice(0, 3)
    
    decoded[9] = findNumber(orderedByLength, decoded[4])
    removeFromArray(orderedByLength, decoded[9])
    
    decoded[0] = findNumber(orderedByLength, decoded[1])
    removeFromArray(orderedByLength, decoded[0])

    decoded[6] = orderedByLength.pop()

    decoded[3] = findNumber(sizeOfFive, decoded[1])
    removeFromArray(sizeOfFive, decoded[3])

    decoded[5] = findNumber(sizeOfFive, decoded[4], 1)
    removeFromArray(sizeOfFive, decoded[5])

    decoded[2] = sizeOfFive.pop()
    
    return decoded
}

function findNumber(NumbersSegments, numberSegment, rest = 0) {
    for (const number of NumbersSegments) {
        let count = 0
        for (const segment of numberSegment) {
            if(!number.includes(segment)) {
                if(rest == 0)
                    break
                else
                    continue
            }
            count++
        }
        if(count == numberSegment.length - rest)
            return number
    }
}

function removeFromArray(array, value) {
    const index = array.indexOf(value)
    array.splice(index, 1)
}

const alphabeticalOrder = (letters) => [...letters].sort().join('')

const fileName = '2021/day_8_seven_segment_search/notes.txt'
decodeOutputValues(fileName).then((result) => console.log(result))