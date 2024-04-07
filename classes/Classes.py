class Node:
    def __init__(self, value=None, next_node=None) -> None:
        self.value = value
        self.next_node = next_node

    def getNext(self):
        return self.next_node

    def getValue(self):
        return self.value

    def setNext(self, next_node) -> None:
        self.next_node = next_node

    def setValue(self, value) -> None:
        self.value = value


class LinkedList:
    def __init__(self) -> None:
        self.head: Node = None
        self.size = 0

    def traverse(self):  # Imprimir la lista
        while self.head != None:
            print(self.head.getValue())
            self.head = self.head.getNext()

    def append(self, node, e):  # Agregar nodos al final de la lista
        if self.head == None:
            self.head = Node(e)
            self.size += 1
            return
        if node.next == None:
            new_node = Node(e)
            node.next = new_node
            self.size += 1
            return
        self.append(node.next, e)

    def preppend(self, e):  # Añadir nodos al comienzo
        new_node = Node(e)
        new_node.next = self.head
        self.head = new_node

    def delete_at_index(self, index):  # Eliminar nodos en un indice dado
        if index > self.size - 1:
            return
        if index == 0:
            self.head = self.head.next
        else:
            pos = 0
            node = self.head
            while pos != index - 1:
                node = node.next
                pos += 1
            aux_node = node.next.next
            node.next.next = None
            node.next = aux_node


class LinkedMatrix:
    def __init__(self) -> None:
        self.linkedMatrix: list = []
        self.size: int = 0

    def traverse(self, i=-1):
        if self.size == 0:
            return
        if i == self.size - 1:
            return
        else:
            i += 1
            self.linkedMatrix[i].traverse()
            self.traverse(i)

    def append(self, new_node: Node):
        self.linkedMatrix.append(new_node)
        self.size += 1

    def preppend(self, new_node: Node):
        self.linkedMatrix.insert(0, new_node)
        self.size += 1

    def delete_at_index(self, index):
        if index > self.size - 1:
            raise IndexError
        else:
            self.linkedMatrix.pop(index)
            self.size -= 1

    def getSize(self) -> int:
        return self.size
