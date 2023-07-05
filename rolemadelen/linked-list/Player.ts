import { SinglyLinkedList } from "./SLLWithTail";

class Mob {
  constructor(
    //
    public readonly name: string,
    private readonly damage: number
  ) {}

  attack(player: Player) {
    player.damaged.pushBack(this.damage);
    console.log(
      `${this.name} attacked ${player.getName()}! (Dealt ${this.damage} damage)`
    );
  }
}

class Player {
  private level = 1;
  private hp = 100;
  readonly damaged: SinglyLinkedList<number>;

  constructor(
    //
    private readonly name: string
  ) {
    this.damaged = new SinglyLinkedList<number>();
  }

  getName() {
    return this.name;
  }

  getHP() {
    return this.hp;
  }

  ready() {
    let accum = 0;
    while (!this.damaged.isEmpty()) {
      const dmg = this.damaged.popFront();
      this.hp -= dmg!.value;
      accum += dmg!.value;

      if (this.hp <= 0) {
        this.damaged.clear();
        this.hp = 0;
        return accum;
      }
    }
    return accum;
  }

  revive() {
    this.hp = 100;
  }
}

const greenSnail = new Mob("Green Snail", 1);
const blueSnail = new Mob("Blue Snail", 3);
const redSnail = new Mob("Red Snail", 5);

const madelen = new Player("madelen");

let turn = Math.floor(Math.random() * 50) + 1;
while (turn) {
  switch (Math.floor(Math.random() * 3) + 1) {
    case 1: {
      greenSnail.attack(madelen);
      break;
    }
    case 2:
      blueSnail.attack(madelen);
      break;
    case 3:
      redSnail.attack(madelen);
  }
  turn -= 1;
}

console.log("Accumulated damage: ", madelen.ready());
console.log("Your HP: ", madelen.getHP());
if (madelen.getHP() === 0) {
  console.log("You died.");
} else {
  console.log("You Survived!");
}
