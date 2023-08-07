export type TreeNodeType<T> = TreeNode<T> | null;

export class TreeNode<T> {
    left: TreeNodeType<T> = null;
    right: TreeNodeType<T> = null;
    constructor(public data: T) {}
}

export class BST<T> {
  private root: TreeNodeType<T>;

  constructor(value: T | null = null) {
    if (null === value) this.root = null;
    else this.root = new TreeNode<T>(value);
  }

  insert(value: T): void {
    this.root = this.insertHelper(value, this.root);
  }

  private insertHelper(value: T, node: TreeNodeType<T> = this.root): TreeNode<T> {
    if (null === node) {
      return new TreeNode<T>(value);
    }

    if (node && value < node.data) {
      node.left = this.insertHelper(value, node.left);
    } else if (node && value >= node.data) {
      node.right = this.insertHelper(value, node.right);
    }

    return node;
  }

  search(value: T, node: TreeNode<T> = this.root): boolean {
    if (!node) {
      return false;
    } else {
      if (value === node.data) return true;

      if (value < node.data) {
        return this.search(value, node.left);
      } else {
        return this.search(value, node.right);
      }
    }
  }

  preorder(node: TreeNodeType<T> = this.root) {
    if (null === node) return;
    
    process.stdout.write(`${node.data} `);
    this.preorder(node.left);
    this.preorder(node.right);
    if(node === this.root) console.log();
  }

  inorder(node: TreeNodeType<T> = this.root) {
    if (null === node) return;
    
    this.inorder(node.left);
    process.stdout.write(`${node.data} `);
    this.inorder(node.right);
    if(node === this.root) console.log();
  }

  postorder(node: TreeNodeType<T> = this.root) {
    if (null === node) return;
    
    this.postorder(node.left);
    this.postorder(node.right);
    process.stdout.write(`${node.data} `);
    if(node === this.root) console.log();
  }

  bfs(): void {
    let q = [this.root];

    while(q.length > 0) {
      let curr = q.shift();

      process.stdout.write(`${curr.data} `)

      if(curr.left) q.push(curr.left);
      if(curr.right) q.push(curr.right);
    }
    console.log();
  }

  getMin(): T | undefined {
    if(!this.root) return undefined;

    let curr = this.root;
    while(curr && curr.left) {
      curr = curr.left;
    }

    return curr.data
  }

  getMax(): T | undefined {
    if(!this.root) return undefined;

    let curr = this.root;
    while(curr && curr.right) {
      curr = curr.right;
    }

    return curr.data
  }

  existInTree(value: T): boolean {
    if(!this.root) return false;
    
    let curr = this.root;
    while(curr) {
      if(curr.data === value) return true;
      else if(curr.data > value) curr = curr.left;
      else curr = curr.right;
    }

    return false;
  }
}