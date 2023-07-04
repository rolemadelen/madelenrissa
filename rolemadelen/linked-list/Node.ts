export type NodeType<T> = Node<T> | null;

export class Node<T> {
  next: NodeType<T> = null;
  constructor(public value: T) {}
}
