type Index = number;
type IndexOrNull = Index | null;
type NumberOrNull = number | null;

interface IMaxHeap {
  heapify(i: Index): void;
  parent(i: Index): Index;
  leftChild(i: Index): Index;
  rightChild(i: Index): Index;
  extract(): IndexOrNull;
  update(i: Index, newVal: number): void;
  getMax(): IndexOrNull;
  delete(i: Index): void;
  insert(x: number): void;
}

class MaxHeap implements IMaxHeap {
  private arr: NumberOrNull[];

  constructor() {
    this.arr = [];
  }

  // heapifies a sub-tree taking the given index as the root
  heapify(i: Index): void {
    let arr = this.arr;
    const left = this.leftChild(i);
    const right = this.rightChild(i);
    let largest = i;

    if (left < arr.length && arr[left] > arr[i]) {
      largest = left;
    }
    if (right < arr.length && arr[right] > arr[largest]) {
      largest = right;
    }
    if (largest !== i) {
      [arr[i], arr[largest]] = [arr[largest], arr[i]];
      this.heapify(largest);
    }
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

  // removes the root which in this case contains the maximum element
  extract(): IndexOrNull {
    let arr = this.arr;
    let size = arr.length;

    if (size === 1) {
      return arr.pop();
    }

    // storing the max element to remove it
    const root = arr[0];
    arr[0] = arr[size - 1];
    arr.pop();
    this.heapify(0);
    return root;
  }

  // update values of key at index 'i' to new_val
  update(i: Index, newVal: number) {
    let arr = this.arr;
    arr[i] = newVal;

    while (i !== 0 && arr[this.parent(i)] < arr[i]) {
      let p = this.parent(i);
      [arr[i], arr[p]] = [arr[p], arr[i]];
      i = p;
    }
  }

  // returns the maximum key (key at root) frcom max heap
  getMax(): number {
    return this.arr[0];
  }

  // deletes a key at given index i
  delete(i: Index): void {
    // it increases the value of the key to infinity and then removes the maximum value
    this.update(i, Infinity);
    this.extract();
  }

  // inserts a new key 'x' in the max heap
  insert(x: number): void {
    let arr = this.arr;
    arr.push(x);

    let i = arr.length - 1;
    while (i > 0 && arr[this.parent(i)] < arr[i]) {
      let p = this.parent(i);
      [arr[i], arr[p]] = [arr[p], arr[i]];
      i = p;
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

      let l = left < size ? left : null;
      let r = right < size ? right : null;

      if (l) q.push(left);
      if (r) q.push(right);
    }

    console.log(str);
  }
}
