import { readFileSync, writeFileSync } from 'node:fs'
;(() => {
  const oldDef = readFileSync('./def.txt', 'utf-8')
    .split('\n')
    .map((x) => x.split(',')?.[0])
    .filter(Boolean)
  const newDef = readFileSync('./def.full.txt', 'utf-8')
    .split('\n')
    .filter((x) => {
      const id = x.split(',')?.[0]
      if (id === '') return false
      return !oldDef.includes(id)
    })

  writeFileSync('./def.new.txt', newDef.join('\n'))
})()
