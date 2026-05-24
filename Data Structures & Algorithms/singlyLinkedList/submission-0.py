class LinkedList:
    
    def __init__(self):
        self.llist = []
    
    def get(self, index: int) -> int:
        return self.llist[index] if len(self.llist) > index else -1

    def insertHead(self, val: int) -> None:
        self.llist.insert(0, val)

    def insertTail(self, val: int) -> None:
        self.llist.append(val)

    def remove(self, index: int) -> bool:
        if len(self.llist) > index:
            self.llist.pop(index)
            return True
        return False

    def getValues(self) -> List[int]:
        return self.llist
