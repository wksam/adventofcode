const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(/\r?\n/).map((element) => [...element].map((e) => parseInt(e)))
}

async function lifeSupportRating(fileName) {
    const diagnostic = await readFile(fileName)
    
    let position = 0
    let oxygenGeneratorRating = [...diagnostic], co2ScrubberRating = [...diagnostic]
    while(true) {
        if(oxygenGeneratorRating.length > 1)
            oxygenGeneratorRating = filterDiagnostic(oxygenGeneratorRating, position, (one, zero) => one >= zero)
        if(co2ScrubberRating.length > 1)
            co2ScrubberRating = filterDiagnostic(co2ScrubberRating, position, (one, zero) => one < zero)
        if(oxygenGeneratorRating.length == 1 && co2ScrubberRating.length == 1) break
        position++
    }
    oxygenGeneratorRating = parseInt(oxygenGeneratorRating.flat().join(''), 2)
    co2ScrubberRating = parseInt(co2ScrubberRating.flat().join(''), 2)
    return oxygenGeneratorRating * co2ScrubberRating
}

function filterDiagnostic(diagnostic, position, filter) {
    const one = diagnostic.filter((element) => element[position] == 1).length
    const digit = filter(one, diagnostic.length - one) ? 1 : 0
    return diagnostic.filter((element) => element[position] == digit)
}

const fileName = '2021/day_3_binary_diagnostic/diagnostic_report.txt'
lifeSupportRating(fileName).then((result) => console.log(result))