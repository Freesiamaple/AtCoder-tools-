# スタックオーバーフローを防ぐ
import sys
sys.setrecursionlimit(10 ** 6)

# 頂点 v を根とする部分木を探索
# p := 頂点 v の親
# depth[v] := 頂点 v の深さ
# chs[v] := 頂点 v の子頂点のリスト
def rec(v, p, depth, chs):
    # 頂点 v の深さを求める
    if v == 0:
        # 根の場合
        depth[v] = 0
    else:
        # 根以外の場合は親頂点の深さ + 1
        depth[v] = depth[p] + 1

    # 頂点 v の各子頂点を探索
    for ch in chs[v]:
        # 子頂点 ch を根とした部分木を再帰的に探索
        # 子頂点 ch の親は v である
        rec(ch, v, depth, chs)

# 頂点数の入力
N = int(input())

# 親頂点リスト
P = list(map(int, input().split()))

# 各頂点の子頂点リストを作る
chs = [[] for v in range(N)]
for v in range(1, N):
    # 頂点 v の親
    p = P[v - 1]

    # 親 p の子頂点リストに頂点 v を挿入
    chs[p].append(v)

# 根頂点 (0) から再帰的に探索
# 根頂点 0 の親は便宜的に -1 とする
depth = [0] * N
rec(0, -1, depth, chs)

# 出力
for d in depth:
    print(d)