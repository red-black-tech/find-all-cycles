def enumerate_circuits(G):

    paths = []
    memo = [False for _ in G]
    P = []

    def path_extension():

        for w in G[P[-1]]:

            if w == s:
                paths.append(list(P))

            if (
                w > s
                and not memo[w]
            ):
                P.append(w); memo[w] = True
                path_extension()
                P.pop(); memo[w] = False

    for s in range(len(G)):
        P = [s]; memo[s] = True
        path_extension()

    return paths