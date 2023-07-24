import { Node, NodeType } from "../linked-list/Node";

interface IQueue<T> {
  getFront(): NodeType<T>;
  getRear(): NodeType<T>;
  enqueue(data: T): void;
  dequeue(): NodeType<T>;
}

export class Queue<T> implements IQueue<T> {
  private front: NodeType<T> = null;
  private rear: NodeType<T> = null;
  private size = 0;

  /* O(1) */
  getFront(): NodeType<T> {
    return this.front;
  }

  getRear(): NodeType<T> {
    return this.rear;
  }

  /* O(1) */
  enqueue(data: T) {
    const newNode = new Node(data);
    if (!this.rear) {
      this.front = newNode;
      this.rear = newNode;
      this.front.next = this.rear;
    } else {
      this.rear.next = newNode;
      this.rear = newNode;
    }

    this.size += 1;
  }

  /* O(1) */
  dequeue(): NodeType<T> {
    if (!this.front) return null;

    const removedNode = this.front;
    this.front = this.front.next;
    this.size -= 1;

    return removedNode;
  }

  /* O(n), n = number of data in Queue */
  printAll() {
    let curr = this.front;

    while (curr) {
      process.stdout.write(`${curr.value} `);
      curr = curr.next;
    }
  }
}
