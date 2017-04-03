class HuffmanHeap(object):
    """
    old: the old list of Huffmantrees, sorted.
    new:  the new list of Huffmantrees, sorted.
    """

    def __init__(self, old, new=None):
        self.old = old
        self.new = new

    def enqueue(self, item):
        """
        push a Huffmantree into the new list
        :param item: a Huffmantree
        :return: None
        """
        self.new.append(item)

    def dequeue(self):
        """
        pop out the smallerst item from the heap
        :return: the smallest item; if the heap is empty, return None
        """
        if len(self.old) == 0 and len(self.new) != 0:
            item = self.new.pop(0)
        elif len(self.new) == 0 and len(self.old) != 0:
            item = self.old.pop(0)
        elif len(self.new) != 0 and len(self.old) != 0:
            if self.old[0].get_freq() >= self.new[0].get_freq():
                item = self.new.pop(0)
            else:
                item = self.old.pop(0)
        else:
            print("old and new are both empty!")
            return None
        return item
