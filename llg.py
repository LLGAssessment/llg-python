#!/usr/bin/env python

import sys
import itertools

def main():
    words = set(w.strip() for w in sys.stdin)
    words.discard('')
    words = list(words)

    graph = tuple(list() for _ in xrange(len(words)))
    for i, left in enumerate(words):
        for j, right in enumerate(words):
            if left == right:
                continue
            if right[0] == left[-1]:
                graph[i].append(j)
    graph = map(tuple, graph)

    class Traverser(object):
        visited = set()
        toppath = []
        stack = []
        def traverse_paths(self, graph, position=None):
            if position is None:
                for i, _ in enumerate(graph):
                    self.traverse_paths(graph, i)
                return self.toppath
            else:
                self.visited.add(position)
                self.stack.append(position)
                if len(self.toppath) < len(self.stack):
                    self.toppath = list(self.stack)
                for w in graph[position]:
                    if w not in self.visited:
                        self.traverse_paths(graph, w)
                self.stack.pop()
                self.visited.discard(position)

    t = Traverser()
    print '\n'.join(map(lambda w: words[w], t.traverse_paths(graph)))

if __name__ == '__main__':
    main()
