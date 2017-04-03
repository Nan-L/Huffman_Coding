class HuffmanHeap(object):
    """
    old: the old list of Huffmantrees
    new:  the new list of Huffmantrees
    """

    def __init__(self, old, new=None):
        self.old = old
        self.new = new

    def enqueue(self, item):
        self.new.append(item)

    def dequeue(self):
        """
        pop out the smallerst item from the heap
        :return: the smallest item
        """
        if len(self.old) == 0:
            item = self.new.pop(0)
        if len(self.new) == 0:
            item = self.old.pop(0)
        else:
            if self.old[0] > self.new[0]:
                item = self.new.pop[0]
            else:
                item = self.old.pop[0]
        return item
