def nqueen(n):
    cols = set()
    positive = set()
    negative = set()

    res = []
    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in cols or (r -c) in negative or (r+c) in positive:
                continue

            cols.add(c)
            positive.add(c +r)
            negative.add( r - c)
            board[r][c] = "Q"

            backtrack( r  + 1)

            cols.remove(c)
            positive.remove(c +r)
            negative.remove( r - c)
            board[r][c] = "."

    backtrack(0)
    return res

q = nqueen(4)
for i, s in enumerate(q):
    print(i + 1)
    for rows in s:
        print(rows)
    print()