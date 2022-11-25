const fs = require('fs')

async function readFile(fileName, encoding='utf-8') {
    const data = await fs.promises.readFile(fileName, encoding)
    return data.split(',').map(element => parseInt(element))
}

async function overlaps(fileName) {
    let laternfishes = await readFile(fileName)
    loop(80, () => {
        const counter = laternfishes.filter((laternfish => laternfish == 0)).length
        laternfishes = laternfishes.map((laternfish) => laternfish != 0 ? laternfish - 1 : 6)
        laternfishes = laternfishes.concat(Array(counter).fill(8))
    })
    return laternfishes.length
}

const loop = (times, callback) => {
    [...Array(times)].forEach(callback);
};

const fileName = 'day_6_lanternfish/lanternfishes.txt'
overlaps(fileName).then((result) => console.log(result))