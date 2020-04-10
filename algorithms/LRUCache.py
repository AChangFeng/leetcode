#! python3
# -*- coding:UTF-8 -*-
"""
# 146. LRU Cache
# Created on 2020/4/10 19:26
# LRUCache
# @author: ChangFeng
"""


class Node:

    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRUCache:
    """
    Dict + Double LinkedList
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.dic:
            return -1
        n = self.dic[key]
        self._remove(n)
        self._add(n)
        return n.val

    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        self._ensure_capacity()

    def _ensure_capacity(self):
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        """
        add to tail
        """
        p = self.tail.prev
        p.next = node

        self.tail.prev = node

        node.prev = p
        node.next = self.tail


from collections import OrderedDict


class LRUCache:
    """
    OrderedDict
    """

    def __init__(self, capacity):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        if key in self.cache:
            del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)


def main():
    pass


if __name__ == '__main__':
    main()
