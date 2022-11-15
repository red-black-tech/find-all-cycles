# A Simple Search Algorithm to Find the Elementary Circuits of a Graph

> Roni Lazimi

## Introduction
An innefficient but simple algorithm is presented for finding all circuits in a graph. The algorithm is a rewriting of Tiernan's algorithm. The correctness is the same as that of Tiernan's algorithm - it works because of the clever realization Tiernan had that filtering search with the condition `w > s` will ensure all circuits found are unique.


## The Algorithm: Enumerate Circuits
```
input: directed graph as an adjacnency list, eg a triangle: [[1],[2],[0]]
output: a list of all cycles with the duplicate vertices ommitted
```

```
def enumerate_circuits(G):

    paths = []
    P = []

    def path_extension():

        #EC2 - path extension
        for w in G[P[-1]]:
            if (
                w > s
                and w not in P
            ):
                P.append(w)
                path_extension()
                #EC4 - vertex_closure:
                P.pop()
            
            #EC3 - circuit confirmation:
            if w == s:
                paths.append(list(P))

    #EC5 - advance initial vertex
    for s in range(len(G)):
        P = [s]
        path_extension()

    return paths
```

## Overview of Tiernan's Algorithm and Why this Shares the Same Correctness:
This algorithm works by finding all elementary circuits and saving whichever ones are cycles. Although it may not appear like it, Tiernan's algorithm does the exact same thing as well.

The fundamental difference between Tiernan's algorithm and this one is in how backtracking is performed. Specifically the difference is in the looping on the neighbors of the latest vertex in the current branch P. Tiernan does not recurse within the loop - instead he finds an eligible vertex to branch to, finishes the loop, then branches. This requires him to keep an extra data structure, H, for avoiding selection of the same candidate for branching.

This algorithm does not need H, because the for loop takes its place by queueing up unique neighbors to recurse into, without going back on them. In other words this algorithm avoids the problem as opposed to having to maintain a separate data structure to solve it.

## Notes
I've annotated this algorithm with `EC#` so that readers can map the parts of this algorithm to the equivalent parts in Tiernan's algorithm for easier understanding of Tiernan's algorithm.

Below is a quick diff of `EC#` in this algorithm and `EC#` in Tiernan's algorithm:
- `EC1`: unchanged
- `EC2`: search is simplified to two conditions, from Tiernan's 3, by the fact that the forloop plays the role of H in terms of deciding how to branch
- `EC3`: unchanged
- `EC4`:
    - if condition removed because implicitly goes to vertex advancement after popping when len(P)==1
    - updates to H not needed anymore
    - doesn't execute until EC3 does at least once
- `EC5`: unchanged
- `EC6`: unchanged

I developed this algorithm by stripping away some code from Tarjan's circuit enumeration algorithm and proving that it still works the same way as Tiernan's algorithm.

## References:
- [Tiernan's Circuit Enumeration Algorithm](./papers/tiernan.pdf)
- [Tarjan's Circuit Enumeration Algorithm](./papers/tarjan.pdf)