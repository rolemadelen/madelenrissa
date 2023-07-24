interface IQueue<T> {
  getFront(): T | undefined;
  getRear(): T | undefined;
  isEmpty(): boolean;
  isFull(): boolean;
  enqueue(data: T): void;
  dequeue(): T | undefined;
}

export class Queue<T> implements IQueue<T> {
  private queue: (T | undefined)[];
  private front = 0;
  private rear = 0;
  public capacity: number;

  constructor(cap: number = 8) {
    this.capacity = cap;
    this.queue = new Array<T>(cap);

    if (Object.seal) {
      this.queue.fill(undefined);
      Object.seal(this);
    }
  }

  /* O(1) */
  getFront() {
    if (this.isEmpty()) {
      throw new Error("Queue is empty.");
    }

    return this.queue[this.front];
  }

  getRear() {
    if (this.isEmpty()) {
      throw new Error("Queue is empty.");
    }
    return this.queue[this.rear - 1];
  }

  isEmpty() {
    return this.front === this.rear;
  }

  isFull() {
    return this.capacity === this.rear;
  }

  /* O(1) */
  enqueue(data: T) {
    if (this.isFull()) {
      throw new Error("Queue is full.");
    }

    this.queue[this.rear] = data;
    this.rear += 1;
  }

  /* O(1) */
  dequeue() {
    if (this.isEmpty()) {
      throw new Error("Queue is empty.");
    }

    let data = this.queue[this.front];
    this.front += 1;
    return data;
  }

  /* O(n), n = number of data in Queue */
  printAll() {
    let i = this.front;
    while (i < this.rear) {
      process.stdout.write(`${this.queue[i]} `);
      i += 1;
    }
    console.log();
  }
}

const q = new Queue<number>();
q.enqueue(1);
q.enqueue(2);
q.enqueue(3);
q.printAll();
q.dequeue();
q.dequeue();
q.printAll();
q.enqueue(4);
q.enqueue(5);
q.enqueue(6);
q.printAll();
q.dequeue();
q.dequeue();
q.enqueue(17);
q.enqueue(18);
q.enqueue(19);
