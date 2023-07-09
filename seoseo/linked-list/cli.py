import time

from sll import *

start = time.time()  # save start time
def printTime(start):
    print("runtime :", time.time() - start)  # current time - start time = runtime

# CLI
def getData(msg):
    print(msg, end = ">>> ")
    value = input()
    return int(value) if value.isdigit() else value

myList = LinkedList()

while True:
    menu = """
    -----------------------
    실행할 명령어를 선택하세요.

    [0] 연결 리스트의 상태 출력
    [1] 처음에 노드 추가    [2] 끝에 노드 추가    [3] 노드 검색
    [4] 첫 노드 꺼내기    [5] 마지막 노드 꺼내기    [6] 특정 위치에 노드 삽입
    [7] 노드 삭제        [8] 연결 리스트 뒤집기
    [9] 끝내기

    """
    print(menu, end=" >>> ")
    command = int(input())
    print("-----------------------")
    print()

    if command == 0:
        start = time.time()
        print(myList)
        printTime(start)
    elif command == 1:
        start = time.time()
        myList.pushFront(getData("추가할 값(정수, 문자)을 입력하세요."))
        printTime(start)
    elif command == 2:
        start = time.time()
        myList.pushBack(getData("추가할 값(정수, 문자)을 입력하세요."))
        printTime(start)
    elif command == 3:
        value = getData("검색할 값을 입력하세요.")
        start = time.time()
        if value in myList:
            print(f"{value}(이)가 리스트에 있습니다.")
        else:
            print(f"{value}(이)가 리스트에 없습니다.")
        printTime(start)
    elif command == 4:
        start = time.time()
        print(myList.popFront())
        printTime(start)
    elif command == 5:
        start = time.time()
        print(myList.popBack())
        printTime(start)
    elif command == 6:
        index = getData("값을 추가할 인덱스를 입력하세요.")
        start = time.time()
        myList.insert(index, getData("추가할 값을 입력하세요."))
        printTime(start)
    elif command == 7:
        value = getData("삭제할 값을 입력하세요.")
        start = time.time()
        if myList.remove(value):
            print(f"{value}(을)를 정상적으로 삭제했습니다.")
        else:
            print(f"{value}(이)가 리스트에 없습니다.")
        printTime(start)
    elif command == 8:
        start = time.time()
        myList.reverse()
        printTime(start)
        print("리스트를 뒤집었습니다.")
        print(myList)
    elif command == 9:
        break

start = time.time()
print("myList getFront() : "+str(myList.getFront()))
printTime(start)
print("myList getBack() : "+str(myList.getBack()))
printTime(start)
print("\n\nFinish for without Tail Pointer\n\n")

