export class AdjacencyMatrix {
    vertex: number;
    matrix: number[][] | null[][];
    constructor(v: number) {
        this.vertex = v;
        this.matrix = new Array(v);
        for (let i = 0; i < v; ++i) {
            this.matrix[i] = new Array(v).fill(null);
        }
    }

    addEdge(u: number, v: number) {
        this.matrix[u][v] = 1;
        this.matrix[v][u] = 1;
    }

    removeEdge(u: number, v: number) {
        this.matrix[u][v] = null;
        this.matrix[v][u] = null;
    }

    print() {
        for (let i = 0; i < this.vertex; ++i) {
            process.stdout.write(`${i}: `);
            for (let j = 0; j < this.vertex; ++j) {
                if (this.matrix[i][j]) {
                    process.stdout.write(`${j} → `);
                }
            }
            console.log();
        }
    }
}