/* Singly Linked List without using a tail poniter */

type NodeType<T> = Node<T> | null;

export class Node<T> {
  public next: NodeType<T> = null;
  constructor(public value: T) {}
}

interface ILinkedList<T> {
  size(): number;
  isEmpty(): boolean;
  pushFront(data: T): void;
  pushBack(data: T): void;
  popFront(): NodeType<T>;
  popBack(): NodeType<T>;
  getFront(): T | null;
  getBack(): T | null;
  reverse(): void;
  insert(index: number, data: T): void;
  display(): void;
}

export class SinglyLinkedList<T> implements ILinkedList<T> {
  private length: number;
  private head: NodeType<T>;

  constructor() {
    this.length = 0;
    this.head = null;
  }

  size() {
    return this.length;
  }

  isEmpty() {
    return this.length === 0;
  }

  pushFront(data: T) {
    const newNode = new Node<T>(data);

    if (this.isEmpty()) {
      this.head = newNode;
    } else {
      newNode.next = this.head;
      this.head = newNode;
    }

    this.length += 1;
  }

  pushBack(data: T) {
    const newNode = new Node<T>(data);

    if (this.isEmpty()) {
      this.head = newNode;
    } else {
      let curr = this.head;
      while (curr && curr.next != null) {
        curr = curr.next;
      }
      if (curr) curr.next = newNode;
    }

    this.length += 1;
  }

  popFront(): NodeType<T> {
    if (this.isEmpty()) return null;

    const removedNode = this.head;
    this.head = this.head && this.head.next;

    this.length -= 1;
    return removedNode;
  }

  popBack(): NodeType<T> {
    if (this.isEmpty()) return null;

    let curr = this.head;
    let prev: NodeType<T> = null;

    while (curr && curr.next) {
      prev = curr;
      curr = curr.next;
    }

    let nodeTBDel: NodeType<T> = null;
    if (prev) {
      nodeTBDel = prev.next;
      prev.next = null;
      this.length -= 1;
      return nodeTBDel;
    }

    return null;
  }

  getFront(): T | null {
    if (this.head) return this.head.value;

    return null;
  }

  getBack(): T | null {
    if (this.head) {
      let curr = this.head;
      while (curr.next) {
        curr = curr.next;
      }
      return curr.value;
    }
    return null;
  }

  reverse() {
    let curr = this.head;
    let prev: NodeType<T> = null;
    let next: NodeType<T> = null;

    while (curr) {
      next = curr.next;
      curr.next = prev;
      prev = curr;
      curr = next;
    }
    this.head = prev;
  }

  insert(index: number, data: T) {
    if (index < 0 || index > this.length) {
      console.error("Error: invalid index.");
      return;
    }
    if (index === 0) return this.pushFront(data);
    if (index === this.length) return this.pushBack(data);

    let curr = this.head;
    while (curr && index - 1) {
      curr = curr.next;
      --index;
    }

    if (curr) {
      const newNode = new Node<T>(data);
      newNode.next = curr.next;
      curr.next = newNode;
      this.length += 1;
    }
  }

  display() {
    let curr = this.head;

    while (curr) {
      process.stdout.write(`${curr.value} `);
      curr = curr.next;
    }

    console.log(`(${this.length})`);
  }
}
