// 시간복잡도 N 
function sol(brackets: string) {
  const arr = brackets.split('') // 문자열 Array객체로 변환
  const bracketDict = {
    ')' : '(' ,
    '}' : '{' ,
    ']' : '[' 
  }

  const stack : string[] = []
  // 괄호가 제대로 닫히기 위해서는, 가장 최근의 여는 괄호가 닫는 괄호와 매치되어야 한다.
  // Array 객체 순환하며, 여는 괄호면 stack에 담고,
  // 닫는 괄호면, stack에서 가장 최근의 여는 괄호를 pop 시켜, 매치되는지 확인한다. 
  for (let val of arr) {  
    if (val === '(' || val ===  '{' || val ===  '[') {
      stack.push(val)
    }
    else {
      if (stack.length === 0|| stack.pop() !== bracketDict[val]) {
        return false
      }
    }
  }
  if (stack.length != 0)
    return false
  return true
}
console.log(
  sol('{{}}}}'),
  sol('{()}'),
  sol('{}()[]'),
);