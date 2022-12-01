const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(/\r?\n/).map((element) => [...element].map((e) => parseInt(e)))
}

async function binaryDiagnostic(fileName) {
    const diagnostic = await readFile(fileName)
    const analysis = diagnostic.reduce((previousValue, currentValue) => previousValue.map((value, index) => currentValue[index] + value))
    
    let gammaRate = analysis.map((element) => element < diagnostic.length / 2 ? 0 : 1)
    let epsilonRate = gammaRate.map((element) => element > 0 ? 0 : 1)

    gammaRate = parseInt(gammaRate.join(''), 2)
    epsilonRate = parseInt(epsilonRate.join(''), 2)
    
    return gammaRate * epsilonRate
}

const fileName = '2021/day_3_binary_diagnostic/diagnostic_report.txt'
binaryDiagnostic(fileName).then((result) => console.log(result))