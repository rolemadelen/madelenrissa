type Index = number;
type IndexOrNull = Index | null;
type NumberOrNull = number | null;

interface IMinHeap {
  parent(i: Index): Index;
  leftChild(i: Index): Index;
  rightChild(i: Index): Index;
  getMin(): IndexOrNull;
  update(i: Index, newVal: number): void;
  insert(x: number): void;
  delete(i: Index): void;
  extract(): IndexOrNull;
  heapify(i: Index): void;
}

class MinHeap implements IMinHeap {
  private arr: NumberOrNull[];

  constructor() {
    this.arr = [];
  }

  // returns the index of the parent of the element at ith index
  parent(i: Index): Index {
    return Math.floor((i - 1) / 2);
  }

  // returns the index of the left child
  leftChild(i: Index): Index {
    return 2 * i + 1;
  }

  // returns the index of the right child
  rightChild(i: Index): Index {
    return 2 * i + 2;
  }

  // returns the Minimum key (key at root) frcom Min heap
  getMin(): number {
    return this.arr[0];
  }

  // inserts a new key 'x' in the Min heap
  insert(x: number): void {
    // the new key is initially inserted at the end
    let arr = this.arr;
    arr.push(x);

    let i = arr.length - 1;
    while (i > 0 && arr[this.parent(i)] > arr[i]) {
      let p = this.parent(i);
      [arr[i], arr[p]] = [arr[p], arr[i]];
      i = p;
    }
  }

  // update values of key at index 'i' to new_val
  update(i: Index, newVal: number) {
    let arr = this.arr;
    arr[i] = newVal;

    while (i !== 0 && arr[this.parent(i)] > arr[i]) {
      let p = this.parent(i);
      [arr[i], arr[p]] = [arr[p], arr[i]];
      i = p;
    }
  }

  // removes the root which in this case contains the Minimum element
  extract(): IndexOrNull {
    let arr = this.arr;

    if (arr.length === 1) {
      return arr.pop();
    }

    // storing the Min element to remove it
    const root = arr[0];
    arr[0] = arr[arr.length - 1];
    arr.pop();
    this.heapify(0);

    return root;
  }

  // deletes a key at given index i
  delete(i: Index): void {
    // it increases the value of the key to infinity and then removes the Minimum value
    this.update(i, this.arr[0] - 1);
    this.extract();
  }

  // heapifies a sub-tree taking the given index as the root
  heapify(i: Index): void {
    let arr = this.arr;
    let n = arr.length;
    if (n === 1) {
      return;
    }
    let l = this.leftChild(i);
    let r = this.rightChild(i);
    let smallest = i;
    if (l < n && arr[l] < arr[i]) smallest = l;
    if (r < n && arr[r] < arr[smallest]) smallest = r;
    if (smallest !== i) {
      [arr[i], arr[smallest]] = [arr[smallest], arr[i]];
      this.heapify(smallest);
    }
  }

  bfs(): void {
    let q: number[] = [0];
    let str = "";
    const size = this.arr.length;

    while (q.length) {
      let curr = q.shift();
      let left = this.leftChild(curr);
      let right = this.rightChild(curr);
      str += `${this.arr[curr]} `;

      let l = left < size ? this.arr[left] : null;
      let r = right < size ? this.arr[right] : null;

      if (l) q.push(left);
      if (r) q.push(right);
    }

    console.log(str);
  }
}
