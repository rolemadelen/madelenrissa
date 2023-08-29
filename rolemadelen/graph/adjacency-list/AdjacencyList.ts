export class AdjacencyList {
  vertex: number;
  list: Array<number>[];
  constructor(v: number) {
    this.vertex = v;
    this.list = new Array(v);
    for (let i = 0; i < v; ++i) {
      this.list[i] = new Array<number>();
    }
  }

  addEdge(u: number, v: number, undirected: boolean = true) {
    this.list[u].push(v);
    if (undirected) {
      this.list[v].push(u);
    }
  }

  removeEdge(u: number, v: number, undirected: boolean = true) {
    if (this.list[u].length > 0) {
      let index = this.list[u].indexOf(v);
      this.list[u].splice(index, 1);

      if (undirected) {
        index = this.list[u].indexOf(v);
        this.list[v].splice(index, 1);
      }
    }
  }
}
