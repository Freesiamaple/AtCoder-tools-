class UnionFind():
    # 初期化
    def __init__(self, n):
        self.par = [-1] * n
        self.rank = [0] * n
        self.siz = [1] * n

        # 新たな配列
        self.min_node = [i for i in range(n)]



    # x と y が同じグループに属するか (根が一致するか)
    def issame(self, x, y):
        return self.root(x) == self.root(y)

    # x を含むグループと y を含むグループを併合する
    def unite(self, x, y):
        # x 側と y 側の根を取得する
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: return False # すでに同じグループのときは何もしない
        # union by rank
        if self.rank[rx] > self.rank[ry]: # ry 側の rank が小さくなるようにする
            rx, ry = ry, rx
        self.par[ry] = rx # ry を rx の子とする
        if self.rank[rx] == self.rank[ry]: # rx 側の rank を調整する
            self.rank[rx] += 1
        self.siz[rx] += self.siz[ry] # rx 側の siz を調整する

        # min_node の更新
        self.min_node[rx] = min(self.min_node[rx], self.min_node[ry])
        
        return True
    
    # 追加: x を含む根付き木の中での頂点番号の最小値
    def get_min_node(self, x):
        return self.min_node[self.root(x)]

# 頂点数と辺数の入力
N, T,L = map(int, input().split())

# 要素数 N の Union-Find を用意する
uf = UnionFind(N)

# 各辺 (a, b) に対して unite(a, b) を実行
for i in range(T):
    # 辺 (a, b) の入力
    a, b = map(int, input().split())

    # unite
    uf.unite(a, b)

# 各頂点 k について答える
for k in range(N):
    print(uf.get_min_node(k))