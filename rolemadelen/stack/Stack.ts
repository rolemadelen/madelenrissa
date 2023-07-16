import { Node, NodeType } from "../linked-list/Node";

interface IStack<T> {
  top(): T | null;
  isEmpty(): boolean;
  push(data: T): void;
  pop(): NodeType<T>;
}

export class Stack<T> implements IStack<T> {
  private topNode: NodeType<T> = null;
  private size = 0;

  /* O(1) */
  top(): T | null {
    if (this.topNode) return this.topNode.value;

    return null;
  }

  /* O(1) */
  isEmpty(): boolean {
    return this.size === 0;
  }

  /* O(1) */
  push(data: T) {
    const newNode = new Node(data);
    newNode.next = this.topNode;
    this.topNode = newNode;
    this.size += 1;
  }

  /* O(1) */
  pop(): NodeType<T> {
    if (this.isEmpty()) return null;

    let removedNode: NodeType<T> = null;
    if (this.topNode) {
      removedNode = this.topNode;
      this.topNode = this.topNode.next;
    }

    this.size -= 1;
    return removedNode;
  }

  /* O(n), n = number of data in stack */
  printAll() {
    let curr = this.topNode;

    while (curr) {
      process.stdout.write(`${curr.value} `);
      curr = curr.next;
    }
  }
}
