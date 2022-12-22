/**
 * case 1. Tree Data가 연결 리스트 형태로 주어질 경우
 * 재귀함수로 각 노드 방문
 */


class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?:number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = (val === undefined ? 0 :val)
    this.left = (left === undefined? null :left)
    this.right = (right === undefined? null :right)
  }
}

function maxDepth(root: TreeNode|null) : number {
  if (root === null) {
    return 0
  }
  return maxDepth(root.left) + 1
  // case 1-1 Input과 같이, 이진 트리의 빈 공간에 Null 값이 든 노드가 들어 있는 경우
  // 시간 복잡도 log(N) 

  // return Math.max(maxDepth(root.right), maxDepth(root.left)) + 1
  // case 1-2. Null 노드 없이 값이 있는 노드만 연결 된 경우
  //  시간 복잡도 N (노드의 개수)
}


/**
 * case 2. Tree Data가 리스트 형태로 이진트리 노드값이 로 주어질 경우
 * 이진 트리의 Level 당 최대 노드 수가 2의 level-1 승임을 이용
 * 시간복잡도 log(N) 
 */

function maxDepth2(TreeArray:Array<string| number>) {
  const l = TreeArray.length
  let c = 1
  let cnt = 0
  while (l >= c) {
    c *= 2
    cnt += 1
  }
  return cnt
}
