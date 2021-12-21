console.log('Part 1:', part1())
console.log('Part 2:', part2())

function part1() {
  // 1374
  const input = getInput().split('\n').map(parseFloat)
  return zip(input, input.slice(1)).filter(([a, b]) => b > a).length
  // imperative
  // return input.reduce((count, reading, index) => {
  //   if (index === 0) return count
  //   return reading > input[index - 1] ? ++count : count
  // }, 0)
}

function part2() {
  const input = getInput().split('\n').map(parseFloat)
  return zip(input, input.slice(3)).filter(([a, b]) => b > a).length
}

function zip<A, B>(a: A[], b: B[]): Array<[A, B]> {
  return a.map((itemA, i) => [itemA, b[i]])
}

function getInput(): string {
  return Deno.readTextFileSync('../inputs/day-01.txt')
}
