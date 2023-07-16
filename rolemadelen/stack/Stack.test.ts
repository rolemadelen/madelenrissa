import { Stack } from "./Stack";

describe("Stack", () => {
  test("Stack is Empty", () => {
    const stack = new Stack<number>();
    expect(stack.isEmpty()).toBe(true);
  });

  test("Stack is NOT Empty", () => {
    const stack = new Stack<string>();
    stack.push("hello");
    expect(stack.isEmpty()).toBe(false);
  });

  test('top returns "null"', () => {
    const stack = new Stack<number>();
    expect(stack.top()).toBe(null);
  });

  test('top returns "Hello"', () => {
    const stack = new Stack<string>();
    stack.push("Hello");
    expect(stack.top()).toBe("Hello");
  });

  test('top returns "World"', () => {
    const stack = new Stack<string>();
    stack.push("Hello");
    stack.push("World");
    expect(stack.top()).toBe("World");
  });

  test('pop returns "World"', () => {
    const stack = new Stack<string>();
    stack.push("Hello");
    stack.push("World");
    expect(stack.pop()!.value).toBe("World");
  });

  test('pop returns "World"', () => {
    const stack = new Stack<string>();
    stack.push("Hello");
    expect(stack.pop()!.value).toBe("Hello");
  });

  test('pop returns "null"', () => {
    const stack = new Stack<string>();
    expect(stack.pop()).toBe(null);
  });
});
